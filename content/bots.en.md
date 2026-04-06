---
title: "Bots"
description: "Explore the LocalGen bot ecosystem, from lightweight examples to advanced strategic planners."
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 60
---

## Bot ecosystem overview

Bots are one of the defining features of LocalGen. They support both gameplay and AI experimentation, and the project explicitly invites new bot contributions.

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

| Bot | Author | Status | Summary |
| --- | --- | --- | --- |
| SmartRandomBot | AppOfficer / GoodCoder666 | Enabled | Largest-stack greedy baseline |
| ZlyBot | AppOfficer | Enabled | Single-focus BFS heuristic |
| ZlyBot v2 | AppOfficer | Enabled | Memory-aware weighted search |
| ZlyBot v2.1 | AppOfficer | Enabled | Dual-focus defensive search |
| SzlyBot | GoodCoder666 | Enabled | Terrain-weighted BFS heuristic |
| GcBot | GoodCoder666 | Enabled | Adaptive heuristic BFS |
| XiaruizeBot | xiaruize0911 | Enabled | Multi-source strategic search |
| KutuBot | pinkHC | Enabled | Unified strategic objective planner |
| oimBot | oimasterkafuu | Enabled | Stance-based strategic planner |
| DummyBot / XrzBot / LyBot | multiple authors | Mixed | Reference, disabled, or experimental roles |

## Contribution paths

- Read the mirrored [Bot Contributions]({{< relref "docs/bot-contributions" >}}) guide
- Check the [Built-in Bots]({{< relref "docs/built-in-bots" >}}) document for submission requirements
- Explore the [simulator page]({{< relref "simulator" >}}) if you want to benchmark bots head-to-head

## What LocalGen expects from serious bots

- readable, maintainable code
- meaningful strategy rather than placeholder random moves
- reliable performance across long games
- evidence such as replays, tests, or benchmark results

