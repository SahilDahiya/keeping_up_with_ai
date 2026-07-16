---
title: Building SQL-powered MCP tools with DataFusion
kind: blog
topic: agents
subtopic: tool-use
secondary_topics: []
summary: Builds an MCP tool exposing a single run_query function that hands the LLM
  arbitrary SQL, backed by Apache DataFusion as an embeddable SQL engine, arguing
  SQL (stable, declarative, ubiquitous in training data) is an excellent agent interface;
  maps a nested-tree TODO model into relational tables to demonstrate.
triage: null
skip_reason: null
source: pydantic
url: https://pydantic.dev/articles/select-star-from-clickbait
author: Marc
published: '2026-06-03'
fetched: '2026-07-16T22:03:23Z'
classifier: claude
taxonomy_rev: 2
words: 1982
content_sha256: 1a2d2192395bf33cde8c03769255f267ee6c1940ef02fd0f748bc148a9da05d0
---

# Building SQL-powered MCP tools with DataFusion

Like many people, I have a TODO app. Mine's not particularly special, but it has the two properties that every serious developer's "productivity" application must have: An audience of one and ridiculously overengineered features. It's been around for a long time (1337 commits, as of this writing), a [perpetual stew](https://en.wikipedia.org/wiki/Perpetual_stew) of personal software that grows features of interesting technology, including CRDTs, bloom filters, immutable in-memory trees and novel but niche graphical user interfaces.

It was the ever-patient piece of software dedicated to what could be called life-long learning, and its time had come to go the way of all things these days, which is to grow an MCP interface, so that while I may not have real users, I'd at least have imaginary ones. The field of TODO APIs is not a particularly exciting one and a model-compatible way of addressing it could look like every other REST interface we've been building for ages, but what if there was a better, more exciting way using an ancient language that both the grey beards of yore as well as the newfangled machine spirits would be trained in?


I am talking, of course, about SQL. We (and thus, by extension, every LLM) have seen a ton of it, since it recently turned 50 years old. If you think about it for a second, SQL is an extraordinarily good fit for agent interaction, a declarative language that is incredibly stable and well-known, made for querying data. I am not speaking in hypotheticals here, [Pydantic Logfire's MCP server](https://pydantic.dev/docs/logfire/integrations/llms/mcp/), which allows an agent to query logs automatically when you get paged at 5.30 am on a Saturday, is one of the most beloved features of our platform, according to real customers! Naturally my TODO app must have a similar feature.

The machine behind Logfire's SQL powers is, of course [DataFusion](https://datafusion.apache.org/), an embeddable SQL engine particularly well suited for OLAP databases (but it does not discriminate). This is especially handy since our TODO app's model is not a boring old database, but an infinitely nestable tree, as it has grown into more of an [outliner](https://en.wikipedia.org/wiki/Outliner) in recent times. Our challenge will be defining an MCP interface with a single usable function: `run_query`, which takes arbitrary SQL and feeds it to our TODO contraption. Let's get started!


Many journeys begin with a database schema and this one is no different. While our replicated TODO trees are neat, SQL requires a more traditional view, the good old relational table. Here is a definition for our TODO model:

```
use datafusion::arrow::datatypes::{DataType, Field, Schema};
fn nodes_schema() -> Schema {
    Schema::new(vec![
        Field::new("id", DataType::FixedSizeBinary(16), false),
        Field::new("parent", DataType::FixedSizeBinary(16), true),
        Field::new("position", DataType::Int32, false),
        Field::new("text", DataType::Utf8, true),
        Field::new("priority", DataType::Int8, true),
        Field::new("done", DataType::Boolean, true),
        Field::new("target", DataType::FixedSizeBinary(16), true),
    ])
}
```
The `parent` link is what makes it a tree. Here's a sample branch:

```
* [ ] Create daemon that randomly pages co-workers with P1 priority
* [ ] Write blog post
  +-- due date: June 2nd
  +-- [x] Add clickbait title
  +-- [ ] Plug company
  |   +-- [x] in opening
  |   +-- [ ] in closing
  +-- [ ] Sneak slightly controversial content past marketing
```
And what it looks like in the database:

| id | parent | pos | text | priority | done | 
|---|---|---|---|---|---|
| 6efb47d | 3a0add4 | 6 | Create daemon that randomly pages co-wor... | 0 | false | 
| 1778631 | 3a0add4 | 7 | Write blog post | 0 | false | 
| dc3a740 | 1778631 | 0 | due date: June 2nd | 0 | NULL | 
| e31086b | 1778631 | 1 | Add clickbait title | 0 | true | 
| 8287fac | 1778631 | 2 | Plug company | 0 | false | 
| 744fe0d | 8287fac | 0 | in opening | 0 | true | 
| b1af8b6 | 8287fac | 1 | in closing | 0 | false | 
| c60d803 | 1778631 | 3 | Sneak slightly controversial content pas... | 0 | false | 

The `position` field indicates the relative position among child nodes of a parent. We are also using [Snowflake-style](https://en.wikipedia.org/wiki/Snowflake_ID) UUIDv7s here. I prefer to use [short IDs](https://crates.io/crates/uuid-suffix) for these, based on suffixes.


Once we have a schema, we can wire up a `TableProvider`, which is the interface DataFusion uses to make a table available to the engine.

```
pub struct NodesTableProvider {
    tree: Arc<ActionTree>,
    schema: SchemaRef,
    // column defaults, etc.
}
#[async_trait]
impl TableProvider for NodesTableProvider {
    fn schema(&self) -> SchemaRef {
        Arc::clone(&self.schema)
    }
    async fn scan(
        &self,
        state: &dyn Session,
        projection: Option<&Vec<usize>>,
        filters: &[Expr],
        limit: Option<usize>,
    ) -> Result<Arc<dyn ExecutionPlan>> {
        let batch = tree_to_record_batch(&self.tree)?;
        let mem = MemTable::try_new(Arc::clone(&self.schema), vec![vec![batch]])?;
        mem.scan(state, projection, filters, limit).await
    }
    // ...
}
```
The table provider has to provide an in-memory table, which is helpfully provided in the form of `MemTable`. We just supply the function `tree_to_record_batch` that turns our in-memory `ActionTree` into a bunch of records and delegate to `MemTable`'s implementation.

```
pub fn tree_to_record_batch(tree: &ActionTree) -> Result<RecordBatch, SqlError> {
    let mut ids: Vec<[u8; 16]> = Vec::new();
    let mut parents: Vec<Option<[u8; 16]>> = Vec::new();
    let mut positions: Vec<i32> = Vec::new();
    let mut texts: Vec<Option<String>> = Vec::new();
    let mut priorities: Vec<Option<i8>> = Vec::new();
    let mut dones: Vec<Option<bool>> = Vec::new();
    let mut targets: Vec<Option<[u8; 16]>> = Vec::new();
    for (_path, node) in tree.dfs() {  // depth-first iter
        let id = node.id();
        ids.push(*id.as_bytes());
        parents.push(tree.parent_id(id).map(|p| *p.as_bytes()));
        positions.push(tree.find_path(id).and_then(|p| p.position()).unwrap_or(0) as i32);
        match node.data() {
            NodeData::Content { text, priority, todo } => {
                texts.push(Some(text.clone()));
                priorities.push(Some(*priority));
                dones.push(*todo);
                targets.push(None);
            }
            NodeData::Link { target } => {
                texts.push(None);
                priorities.push(None);
                dones.push(None);
                targets.push(Some(*target.as_bytes()));
            }
        }
    }
    // Convert byte arrays to the format FixedSizeBinaryArray expects
    let id_values: Vec<Option<&[u8]>> = ids.iter().map(|b| Some(b.as_slice())).collect();
    let parent_values: Vec<Option<&[u8]>> = parents
        .iter()
        .map(|o| o.as_ref().map(|b| b.as_slice()))
        .collect();
    let target_values: Vec<Option<&[u8]>> = targets
        .iter()
        .map(|o| o.as_ref().map(|b| b.as_slice()))
        .collect();
    RecordBatch::try_new(
        Arc::new(nodes_schema()),
        vec![
            Arc::new(FixedSizeBinaryArray::try_from_sparse_iter_with_size(id_values.into_iter(), 16)?),
            Arc::new(FixedSizeBinaryArray::try_from_sparse_iter_with_size(parent_values.into_iter(), 16)?),
            Arc::new(Int32Array::from(positions)),
            Arc::new(StringArray::from(texts)),
            Arc::new(Int8Array::from(priorities)),
            Arc::new(BooleanArray::from(dones)),
            Arc::new(FixedSizeBinaryArray::try_from_sparse_iter_with_size(target_values.into_iter(), 16)?),
        ],
    )
}
```
Note that DataFusion is a *columnar* storage engine. Instead of storing row after row, a `RecordBatch` stores column after column. This is great for data locality when you only need certain fields.

If a query is submitted, it is analyzed and executed by the database engine, where all the higher-level transformations and SQL stuff is taken care of for us already. The lowest-level primitive we have to implement is a linear table scan, which is essentially iterating over all of our virtual rows that we construct from the tree, where we earlier just deferred to `mem.scan()`.

With that in place, we can already query the data, including

```
> SELECT text, done FROM nodes WHERE done = false LIMIT 5
Create daemon that randomly pages co-workers with P1 priority   false
Write blog post                                                 false
Plug company                                                    false
in closing                                                      false
Sneak slightly controversial content past marketing             false
```
filtering and paging,

```
> SELECT text FROM nodes WHERE text LIKE '%company%'
Plug company
```
search,

```
> SELECT done, COUNT(*) as count FROM nodes GROUP BY done
true   2
false  5
NULL   1
```
and aggregation. Try getting that up in 15 minutes using a REST API!

The MCP interface is compact and easy to write (example uses the [ mercutio](https://crates.io/crates/mercutio) crate):

```
tool_registry! {
    enum Tools {
        Sql("sql", "Queries nodes using SQL") {
            /// SQL query string.
            q: String,
            /// Output format.
            format: Option<OutputFormat>,
        },
    }
}
```
`OutputFormat` allows returning results as space-separated text (default), JSON arrays, or a markdown document view for rendering node trees.


Along the way to making everything relational-algebra-shaped, we lost our nice tree properties. This would make it cumbersome to write expressions like "give me all items under a given root" to display a subtree:

```
 WITH RECURSIVE subtree AS (
      SELECT * FROM nodes WHERE id = uuid('019e8a0f-67db-72f1-832e-3dcd01778631')
      UNION ALL
      SELECT n.* FROM nodes n
      JOIN subtree s ON n.parent = s.id
  )
  SELECT * FROM subtree
```
It's impressive we get recursive common table expressions for free from DataFusion, and the agent might not have issues writing that but it's a mouthful. We can make its life easier for such a common operation by adding user-defined functions:

```
/// Table function that returns subtree rows.
///
/// - `tree()` -- full tree
/// - `tree(UUID)` -- subtree from node
/// - `tree(UUID, INT)` -- with depth limit
struct TreeFunc {
    tree: Arc<ActionTree>,
}
fn dfs_from(tree: &ActionTree, id: &Uuid) -> Vec<(usize, Uuid)> {
    tree.get(id)
        .map(|subtree| subtree.dfs().map(|(path, node)| (path.len(), *node.id())).collect())
        .unwrap_or_default()
}
impl TableFunctionImpl for TreeFunc {
    fn call(&self, args: &[Expr]) -> Result<Arc<dyn TableProvider>, DataFusionError> {
        let root_id = if args.is_empty() {
            *self.tree.id()
        } else {
            Self::parse_uuid(&args[0])?
        };
        let max_depth = args.get(1).map(Self::parse_depth).transpose()?.flatten();
        let nodes: Vec<_> = dfs_from(&self.tree, &root_id)
            .into_iter()
            .filter(|(depth, _)| max_depth.map_or(true, |max| (*depth as i64) <= max))
            .collect();
        let batch = self.build_batch(nodes)?;  // same schema as `nodes` table
        Ok(Arc::new(MemTable::try_new(batch.schema(), vec![vec![batch]])?))
    }
}
// Registration
ctx.register_udtf("tree", Arc::new(TreeFunc::new(tree)));
```
Now our query is much simpler:

```
SELECT * FROM tree(uuid('019e8a0f-67db-72f1-832e-3dcd01778631'))
```
Other user-defined functions turn almost all remaining complex tree operations into one-liners:

| Function | Description | 
|---|---|
| `uuid(TEXT)` | Parse UUID string to binary | 
| `uuid7()` | Generate new UUIDv7 | 
| `resolve(TEXT)` | Resolve UUID suffix (4-32 hex chars) to full UUID | 
| `s(UUID)` | Last 7 hex chars of UUID | 
| `s(TEXT)`/`s(TEXT, N)` | Truncate text to N chars (default 60) or first newline | 
| `checkbox(BOOL)` | `true`->`[x]`,`false`->`[ ]`,`NULL`-> empty | 
| `depth(UUID)` | Depth from root (root = 0) | 
| `path(UUID)` | Sortable path string (e.g. `0000.0001`) | 
| `ancestors(UUID)` | Array of ancestor UUIDs `[root, ..., parent]` | 
| `iter(UUID)` | Array of subtree UUIDs in DFS order | 
| `tree(UUID)` | Subtree as virtual table (UDTF) | 


Reading data is all fun and games, but for the true AI assistant experience, we want the model to be able to insert or update records, too. This involves writing a function that can translate e.g. a row-insertion back into a tree operation:

```
// Called from `InsertExec::execute()`:
fn process_batch(batch: &RecordBatch, tree: &mut ActionTree) -> Result<Vec<Change>> {
    let mut changes = Vec::new();
    // Downcast columns to their concrete array types
    let id_array = batch.column(0).as_any().downcast_ref::<FixedSizeBinaryArray>().unwrap();
    let parent_array = batch.column(1).as_any().downcast_ref::<FixedSizeBinaryArray>().unwrap();
    let position_array = batch.column(2).as_any().downcast_ref::<Int32Array>().unwrap();
    let text_array = batch.column(3).as_any().downcast_ref::<StringArray>().unwrap();
    for row in 0..batch.num_rows() {
        let node_id = extract_uuid_from_binary(id_array, row)?;
        let parent_id = extract_uuid_from_binary(parent_array, row)?;
        let text = text_array.value(row);
        // Translate SQL INSERT into tree operation
        let create_change = Change {
            id: Some(node_id),
            action: Some(Action::CreateNode(CreateNode {
                parent: Some(parent_id),
                content: text.to_string(),
                after: position_to_after(tree, &parent_id, position_array.value(row)),
            })),
        };
        apply_change(tree, &create_change);
        changes.push(create_change);
        // Handle optional priority and done columns similarly...
    }
    Ok(changes)
}
```
It might look a little strange, but remember our tree is based on a sequence of edit operations (a [grow-only set](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type#G-Set_(Grow-only_Set))) and never mutated directly, thus the song-and-dance of creating a `Change` and applying it.

Updates work almost exactly the same, since our tree is updated through creating additional `Action`s on it, the pattern is identical, just create a change and apply it. The `UPDATE` code is not shown here, but we can try it out with an example query:

```
-- be sure to slap a tracing span on there and ship it to Logfire!
> UPDATE nodes SET done = true WHERE text = 'in closing'
1
```

Wiring up DataFusion is a little lengthy at (compile-)times and to do it efficiently at scale requires some serious engineering. Once done, the power you gain is immense: A connected LLM can ask complex questions in a language it already understands, and the time spent designing interfaces goes effectively to zero. [Optimize your MCP interface](https://pydantic.dev/articles/engineering-mcp-tools-for-token-efficiency) and all of a sudden operations that took multiple iterations and large amounts of your context boil down to a single query with compact results. With all of that time saved, we can finally tackle that last TODO.

*If you'd rather not hand-roll SQL-over-MCP for your own data, that's what  Logfire does for your traces and logs, in a lot less than 1337 commits.*
