---
title: "Meet the bots"
description: "Choose an offline opponent and learn how each built-in bot approaches the game."
weight: 40
doc_group: play
---

LocalGen includes ten enabled bots, ready to select in Local Game. You can play against them or watch them compete to see how their strategies unfold.

## Available opponents

These names work in both Local Game and the simulator. Strategy descriptions and complexity estimates come from the project's [bot overview](https://github.com/SZXC-WG/LocalGen-new/blob/master/src/bots/README.md). They describe implementation approaches, not a strength ranking.

| Bot | Author | Strategy | Estimated per-turn complexity |
| --- | --- | --- | --- |
| `SmartRandomBot` | AppOfficer / GoodCoder666 | Greedy moves from the largest army stack | O(n) |
| `KtqBot` | ktq1124298818 / GoodCoder666 | Local greedy moves around one target | O(n) |
| `ZlyBot` | AppOfficer | Single-focus BFS heuristic | O(n) |
| `ZlyBot v2` | AppOfficer | Weighted search with memory | O(n log n) |
| `ZlyBot v2.1` | AppOfficer | Defensive search with two focal points | O(n log n) |
| `SzlyBot` | GoodCoder666 | BFS with terrain weights | O(n) |
| `GcBot` | GoodCoder666 | Adaptive heuristic BFS | O(n) |
| `XiaruizeBot` | xiaruize0911 | Strategic search from multiple sources | O(kn²) |
| `KutuBot` | pinkHC | Unified strategic objective planning | O(n log n) |
| `oimbot` | oimasterkafuu | Threat and objective planning with memory | O(n²) |

Here, `n` is the number of map tiles and `k` is the number of candidate army stacks considered by a multi-source planner. These are rough worst-case estimates for one turn; typical maps may take less time.

Three other implementations remain in the source tree but are not included in the current build:

| Bot | Author | Strategy | Estimated per-turn complexity |
| --- | --- | --- | --- |
| DummyBot | AppOfficer | Example heuristic greedy | O(n) |
| XrzBot | xiaruize0911 | Focused random greedy | O(n) |
| LyBot | pinkHC | Multiplayer objective planning | O(n²) |

## Select a bot in the terminal

Names are case-sensitive and retain spaces. Put names containing spaces in quotes:

```bash
./LocalGen-bot-simulator --games 20 --bots "ZlyBot v2.1" GcBot
```

The runtime name `oimbot` is entirely lowercase. If a name is unknown, the simulator prints the available names and exits. The [simulator guide]({{< relref "docs/simulator-guide" >}}) covers the full command-line interface.

## How bots join the project

Built-in bots inherit `BasicBot`, implement `init()` and `requestMove()`, and add actions to the inherited move queue. They can also receive events through `onWin`, `onCapture`, `onSurrender`, and `onText` hooks.

Each bot registers its name with `BotRegistrar` and is enabled through `LOCALGEN_BOT_SOURCES` in the top-level `CMakeLists.txt`. The desktop app and simulator share this list, so placing a file in `src/bots/` alone does not make it appear in the menu.

To add your own strategy, follow [build and contribute a bot]({{< relref "docs/bot-contributions" >}}).
