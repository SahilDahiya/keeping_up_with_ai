---
title: Build a retro handheld game with Codex and ModRetro Chromatic | OpenAI Developers
kind: blog
topic: null
subtopic: null
secondary_topics: []
summary: null
triage: null
skip_reason: null
source: openai-devs
url: https://developers.openai.com/blog/build-a-game-with-modretro-chromatic/
author: null
published: '2026-11-09'
fetched: '2026-11-10T06:16:19Z'
classifier: null
taxonomy_rev: 2
words: 1155
content_sha256: fad36f884b37f71fb41ffef3ed7a9a886403f29c1c75516f6b0fabb10d0e0ce8
---

# Build a retro handheld game with Codex and ModRetro Chromatic | OpenAI Developers

With all due respect to the iPhone, the Game Boy might be the most iconic handheld device of all time. A generation of kids stomped Koopas on the bus and battled their friends in Pokémon over a link cable, all on a device that fit in your pocket. Or at least a pocket of your backpack.

With today’s powerful coding models and tools like Codex, building your own games has never been easier (or, in my opinion, more fun). But there’s something special about a game running on purpose-built hardware, like the Game Boy Color, that’s hard to replace. That’s why I am *sooo excited* to share that the [ModRetro plugin for Codex](https://developers.openai.com/modretro) lets you build Game Boy Color games and play them on a Chromatic.

[Order the special edition ModRetro Chromatic](https://openai.com/supply/shop/).

Let’s jump right in and explain how it works.

## Install the plugin

1. In the ChatGPT desktop app, select **Codex** from the **ChatGPT** dropdown.
2. Open **Plugins** and search for **ModRetro Chromatic**. Select **ModRetro Chromatic Plugin** by ModRetro, then click **Install**.
3. Open a local project folder and start a chat. Type **@** and choose the plugin so Codex knows which tools to use.
4. Ask Codex to set up the plugin and check for any missing build tools. You can build and play your first game on your computer.

## Prompt your first game

With the plugin selected in your Codex chat, describe the game you want to build. To follow along with the video, use this example prompt.

Build a top-down adventure game called Lodge Podge where a pixel beaver must chew down small trees to gather sticks to build a lodge in the center of the level.


Next, ask Codex to build the game and open the preview. You can also ask it to point you to these files in your GB Studio project folder.

- Open the `.gbsproj` file in GB Studio to edit scenes, actors, and events.
- Look in `assets/` for the sprite sheets, backgrounds, and audio used by the project.
- Run the compiled `.gbc` file in an emulator or install it on a cartridge.

![Three game screens showing pixel art of a beaver and a lodge beside a pond.](https://developers.openai.com/images/blog/build-a-game-with-modretro-chromatic/lodge-podge.webp) 

From there, play a few rounds and tell Codex what would make the game more fun. In Lodge Podge, I asked Codex to make the beaver chonkier (for maximum cuteness) and to require mud and leaves as well as sticks to build the lodge.

## What’s in the plugin

The ModRetro Chromatic plugin contains developer tools the model can use on your behalf.

### Animate a character

Ask Codex to create a sprite sheet and show you the frames side by side. To revise the animation, identify the pose or direction you want to change, then ask Codex to rebuild the preview.

![A sprite sheet with six front-, back-, and side-facing beaver poses.](https://developers.openai.com/images/blog/build-a-game-with-modretro-chromatic/walk-cycle.webp) 

### Build a map the player can walk through

Ask Codex to show you a scene’s background and collision map side by side. The collision map marks which tiles block movement. Use the background to identify the area you mean, then tell Codex which tiles to mark as blocked or walkable.

![A scene background beside the same scene with blocked tiles highlighted in red.](https://developers.openai.com/images/blog/build-a-game-with-modretro-chromatic/room-collisions.webp) 

### Play the ROM in Codex

Ask Codex to open the game preview in its built-in browser. Use the arrow keys for the Game Boy’s D-pad, **Z** for **A**, **X** for **B**, and **Enter** for **Start**. Use the toolbar above the emulator to pause or resume.

![Lodge Podge running in the Chromatic preview in Codex.](https://developers.openai.com/images/blog/build-a-game-with-modretro-chromatic/playable-preview.webp) 

### Point to the part you want to change

Choose **Annotate game** in the preview toolbar, then click the game display to freeze a frame. Select the sprite, tile, or area you want to change and describe the edit. Choose **Resume game** to return to the emulator. After Codex makes the change, ask it to rebuild the ROM and reopen the preview.

![The emulator paused with the annotation tool selected in the toolbar.](https://developers.openai.com/images/blog/build-a-game-with-modretro-chromatic/annotate-preview.webp) 

### Have Codex test a sequence of moves

You can also control the emulator from chat. Ask Codex to run the ROM, send a sequence of button presses, and capture a frame after each step. Ask for the frames side by side so you can inspect them together.

![Three emulator frames arranged side by side, each labeled with its frame number.](https://developers.openai.com/images/blog/build-a-game-with-modretro-chromatic/playtest-frames.webp) 

## Edit in GB Studio

GB Studio is a visual editor for building Game Boy games. Open your project’s `.gbsproj` file and choose **Game World**. Select a scene in the navigator to see its properties in the sidebar. You can drag an actor to a new tile or edit collisions directly on the scene. Save the project, then return to your Codex chat and ask it to rebuild and open the preview. The [GB Studio guide to scenes](https://www.gbstudio.dev/docs/project-editor/scenes/) explains how backgrounds, actors, and triggers fit together.

![GB Studio’s Game World shows the Survey stakes and Woven walls scenes for Lodge Podge.](https://developers.openai.com/images/blog/build-a-game-with-modretro-chromatic/gb-studio-game-world.webp) 

### Other development options

- **Extend a GB Studio game.** If the built-in events don’t cover a mechanic, you can add a custom event in GBVM, GB Studio’s virtual-machine language, or extend the engine in C. See the [GB Studio plugin guide](https://www.gbstudio.dev/docs/extending-gbstudio/plugins/).
- **Write the game in C with GBDK-2020.** The ModRetro plugin can compile standalone C with GBDK’s `lcc` compiler. GBDK’s [Game Boy APIs](https://gbdk.org/docs/api/) give you access to buttons, sprites, tiles, and palettes. Ask Codex to start with a game loop that reads the D-pad and moves a single sprite.
- **Write your own engine.** You can have Codex implement the game loop, scrolling, and collisions from scratch. For an assembly project, build the ROM with a separately installed toolchain such as [RGBDS](https://rgbds.gbdev.io/). Then give the resulting `.gb` or `.gbc` file to the plugin to inspect and playtest.

## Deploy to device

You’ll need a Chromatic, a compatible rewritable homebrew cartridge, and a USB data cable. Follow [ModRetro’s quickstart](https://support.modretro.com/en_us/chromatic-devday-edition-quickstart-guid-By1iOlcMg) to update the firmware and activate Developer Mode using the computer you’ll connect to the handheld.

1. Insert the cartridge, connect the Chromatic to your computer, and open the game preview in your local Codex chat.
2. Choose **Install on Chromatic**, select your connected device, and click **Install**. Read the confirmation carefully. Writing the new ROM erases the game on that cartridge and can erase its saves. The installer doesn’t back up the cartridge.
3. Choose **Confirm Install** when you’re ready. Leave the cable connected until the plugin reports success, then start the game on the Chromatic.

## “The Power of Science is Staggering!”

With the ModRetro plugin for Codex, you can prompt your way to original Game Boy Color games and use all the tools in the thriving GBC homebrew development ecosystem. This is going to be so, so much fun. You can [order your own ModRetro Chromatic](https://openai.com/supply/shop/) and [explore ModRetro’s other projects](https://modretro.com/). Happy Game Boy hacking!
