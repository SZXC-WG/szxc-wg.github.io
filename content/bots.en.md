---
title: "Bots"
description: "Read the bot model the same way the project docs describe it: built-in versus external, clear submission rules, and performance expectations."
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 60
---

## Bot ecosystem overview

Bots are one of the defining features of LocalGen. They matter both for ordinary offline play and for serious AI experimentation, and the project docs explicitly invite new bot contributions.

The upstream documentation distinguishes two major categories:

1. **Built-in bots**
   - stored in `src/bots/`
   - compiled into the LocalGen executable
   - written in C++ for deep integration and speed

2. **External bots**
   - separate executables written in any language
   - connected through a network-facing protocol
   - intended to broaden participation beyond C++ contributors

## Current built-in bot roster

| Bot | Enabled | Complexity | Approx. turn cost | Summary |
| --- | --- | --- | --- | --- |
| DummyBot | No | Low | $O(n)$ | Example heuristic greedy |
| SmartRandomBot | Yes | Low | $O(n)$ | Largest-stack greedy baseline |
| XrzBot | No | Low | $O(n)$ | Focused random greedy |
| ZlyBot | Yes | Medium | $O(n)$ | Single-focus BFS heuristic |
| ZlyBot v2 | Yes | Medium | $O(n \log n)$ | Memory-aware weighted search |
| ZlyBot v2.1 | Yes | Medium | $O(n \log n)$ | Dual-focus defensive search |
| SzlyBot | Yes | Medium | $O(n)$ | Terrain-weighted BFS heuristic |
| GcBot | Yes | Medium | $O(n)$ | Adaptive heuristic BFS |
| XiaruizeBot | Yes | High | $O(kn^2)$ | Multi-source strategic search |
| KutuBot | Yes | High | $O(n \log n)$ | Unified strategic objective planner |
| LyBot | No | High | $O(n^2)$ | Multiplayer objective planner |
| oimBot | Yes | High | $O(n^3)$ | Stance-based strategic planner |

## Reading the complexity column

Let $n$ denote the number of relevant tiles a bot inspects during a turn, and let $k$ denote the number of frontier candidates or strategic branches it keeps alive.

$$
T_{\text{match}} \approx \sum_{t=1}^{s} T_{\text{bot}}(n_t)
$$

That shorthand is why a jump from $O(n)$ to $O(n \log n)$ can become visible in long simulator runs: the per-turn difference compounds over hundreds of steps.

```text
src/bots/MyBot.cpp
├─ include src/core/bot.h
├─ derive from BasicBot
├─ implement init(...)
├─ implement requestMove(...)
├─ register the bot via the documented macro
└─ add the file to PROJECT_SOURCES
```

## Built-in bot submission checklist

The upstream built-in bot README expects every bot in `src/bots/` to satisfy all of the following:

1. The implementation is written in **C++17-compatible code**.
2. The full bot lives in a **single `*.cpp` source file**.
3. That file includes `src/core/bot.h`.
4. The class inherits from `BasicBot` and overrides `compute`.
5. The bot is registered through the `REGISTER_BOT` macro.
6. The source file is added to `PROJECT_SOURCES` in the top-level `CMakeLists.txt`.

## What a strong bot contribution includes

- tests, replays, or benchmark evidence
- clear notes about performance and memory behavior
- strategy deeper than a placeholder random walker
- for external bots, setup instructions plus supported runtime / OS details

## Continue reading

- Read the mirrored [Bot Contributions]({{< relref "docs/bot-contributions" >}}) guide
- Check the [Built-in Bots]({{< relref "docs/built-in-bots" >}}) document for exact submission requirements
- Explore the [simulator page]({{< relref "simulator" >}}) if you want to benchmark bots head-to-head

