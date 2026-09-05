---
title: "Meet the bots"
description: "Choose an opponent, explore different strategies, or write your first bot."
draft: false
weight: 60
---

Bots are computer-controlled opponents. LocalGen includes them with the app: choose a name to add an opponent to your match, without installing models or setting up a service.

For your first game, keep P1 set to `Human` in **Local Game** and choose bots for the other slots. To watch their strategies unfold, set P1 to a bot too and let the whole match play itself.

## Different opponents, different ideas

The current development branch compiles these 10 bots. The descriptions summarize their approaches to help you choose an opponent or explore the source. Results depend on the map, opponents, and player count.

| Bot name | Approach | Author |
| --- | --- | --- |
| SmartRandomBot | Prefer moves from the largest army stack | AppOfficer / GoodCoder666 |
| KtqBot | Make local greedy choices around one focus | ktq1124298818 / GoodCoder666 |
| ZlyBot | Combine breadth-first search with heuristics | AppOfficer |
| ZlyBot v2 | Use memory in a weighted search | AppOfficer |
| ZlyBot v2.1 | Balance a dual-focus search with defense | AppOfficer |
| SzlyBot | Account for terrain weights during search | GoodCoder666 |
| GcBot | Adapt heuristic search to the current position | GoodCoder666 |
| XiaruizeBot | Plan moves from multiple army sources | xiaruize0911 |
| KutuBot | Evaluate and select strategic objectives together | pinkHC |
| oimbot | Combine memory, threat assessment, and objective planning | oimasterkafuu |

DummyBot, XrzBot, and LyBot also have source files, but are not included in the current build list. Your downloaded version may have a different roster; check the choices in the app.

## Find a strategy that suits your map

The [simulator]({{< relref "simulator" >}}) runs batches of matches and reports win rates, average rankings, kills, and optional decision timings. Trying several maps and opponent groups reveals more about a strategy than a single win or loss.

Use the exact bot names from the table in simulator commands. Quote names containing spaces, such as `"ZlyBot v2.1"`; `oimbot` is all lowercase.

## Turn an idea into a bot

Current bots use **C++20** and compile directly into the desktop app and simulator. An implementation usually lives in one `src/bots/*.cpp` file, inherits from `BasicBot`, implements `init(...)` and `requestMove(...)`, registers with `BotRegistrar`, and joins `LOCALGEN_BOT_SOURCES` in `CMakeLists.txt`.

There is no external bot process or Python client interface yet. Read the [built-in bot reference]({{< relref "docs/built-in-bots" >}}) to get started. When you are ready to share your work, the [bot contribution guide]({{< relref "docs/bot-contributions" >}}) explains how to present your algorithm and evaluation results.
