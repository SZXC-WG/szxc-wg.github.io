---
title: "Built-in Bots"
description: "Submission requirements and current roster overview for bots compiled into LocalGen itself."
date: 2026-04-06T17:55:08+08:00
draft: false
weight: 70
---

> Source document: [`src/bots/README.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/src/bots/README.md)

## Overview

This part of the project hosts bots that are compiled directly into the LocalGen executable.

## Current bot overview

| Bot | Author | Enabled | Complexity summary |
| --- | --- | --- | --- |
| DummyBot | AppOfficer | No | Example heuristic greedy bot |
| SmartRandomBot | AppOfficer / GoodCoder666 | Yes | Largest-stack greedy |
| XrzBot | xiaruize0911 | No | Focused random greedy |
| ZlyBot | AppOfficer | Yes | Single-focus BFS heuristic |
| ZlyBot v2 | AppOfficer | Yes | Memory-aware weighted search |
| ZlyBot v2.1 | AppOfficer | Yes | Dual-focus defensive search |
| SzlyBot | GoodCoder666 | Yes | Terrain-weighted BFS heuristic |
| GcBot | GoodCoder666 | Yes | Adaptive heuristic BFS |
| XiaruizeBot | xiaruize0911 | Yes | Multi-source strategic search |
| KutuBot | pinkHC | Yes | Unified strategic objective planner |
| LyBot | pinkHC | No | Multiplayer objective planner |
| oimBot | oimasterkafuu | Yes | Stance-based strategic planner |

## Requirements for a new built-in bot

1. It must be written in C++ compatible with the project.
2. It must stay within the C++17 feature set.
3. The implementation should live in a single `*.cpp` file.
4. That file must include `src/core/bot.h`.
5. The class must inherit from `BasicBot` and override `compute`.
6. The bot must be registered with `REGISTER_BOT`.

## Submission checklist

1. Place the file in `src/bots/`.
2. Choose a clear and unique filename.
3. Add it to the top-level `CMakeLists.txt` source list.
4. Submit a pull request.

