---
title: "Bot simulator"
description: "Run more matches and use the results to understand and improve your strategy."
draft: false
weight: 70
---

After a bot wins one match, you might wonder: what about another map, or more opponents? **LocalGen-bot-simulator** runs batches of matches to help you explore those questions.

It shares the desktop app's game core, map loader, and bot registry. Run it from the command line without opening the game interface; multiple CPU worker threads can run independent matches at the same time.

## Run your first batch

Complete a Release build using [Installation and building]({{< relref "docs/getting-started" >}}), then run this from `build/Release`:

```bash
./LocalGen-bot-simulator --games 10 --width 20 --height 20 --steps 1000 --bots XiaruizeBot GcBot
```

In Windows PowerShell, use `./LocalGen-bot-simulator.exe` with the same arguments. This example plays 10 matches between two bots on random maps, with a limit of 1000 half-turns per match.

To use your own map or show only the final summary:

```bash
./LocalGen-bot-simulator --games 20 --map maps/arena01.lgmp --bots XiaruizeBot GcBot
./LocalGen-bot-simulator --games 50 --silent --latency --bots XiaruizeBot GcBot
```

On macOS, bundled maps live inside the app. From `build/Release`, use `LocalGen-new.app/Contents/MacOS/maps/arena01.lgmp` for this example, or supply an absolute path to your own map.

`--map` accepts v6 `.lgmp` files and overrides the random-map width and height options. Map paths are relative to the command's working directory. Bot names are case-sensitive; quote names containing spaces.

## Read the results

The summary reports OpenSkill ratings and their 95% intervals, wins, win rates and their 95% intervals, average rank, kills, final army, final land, and survival counts. Add `--latency` to measure the average duration of each `requestMove()` call.

Use these results to compare performance within your experiment. Maps, opponents, game count, and the step limit all affect the conclusion; a small sample or a single map tells only part of the story.

## Before comparing runs

- Defaults are 8 games on 20×20 maps, a limit of **1000 half-turns** per match, `XiaruizeBot GcBot` as opponents, and an automatic worker count.
- Matches use free-for-all rules. At the step limit, the bot ranked first is counted as the winner even if several bots are still alive.
- Each match prints when it finishes, so completion order may differ from game number order. `--silent` leaves only the final summary.
- `--shuffle` randomizes player index mapping. There is no command-line seed option, so separate calls cannot guarantee match-by-match reproduction.

When sharing results, record your source version, full command, map, and environment. See the [complete simulator guide]({{< relref "docs/simulator-guide" >}}) for flags and statistical details, or the [bot contribution guide]({{< relref "docs/bot-contributions" >}}) when you are ready to share a new strategy.
