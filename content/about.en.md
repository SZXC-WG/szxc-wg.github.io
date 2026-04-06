---
title: "About"
description: "Understand what the README promises, how the version lines are split, and which file formats and tools matter in LocalGen."
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 10
---

## What the README promises

**Local Generals.io (LocalGen)** is an independent, open-source project built for **local-first strategy play**.

The upstream README highlights three headline use cases:

- **Play generals.io completely offline**
- **Use ready-to-run built-in bots** without extra setup
- **Battle friends over the same LAN** when you want local multiplayer instead of an online service

It also explicitly invites ideas, bug reports, and pull requests through GitHub.

## Version lines that matter

The README and release guidance make the branch split clear:

1. **`master` / `v6.x`**
   - the active development branch
   - the home of the **Qt6 rewrite**
   - where architecture, UI, tooling, and bot interfaces are being modernized

2. **`v5.x`**
   - the long-term maintenance line
   - the home of older playable releases
   - still important if you need the historical EGE-era workflow or legacy downloads

> The upstream README explicitly warns that the `master` branch is still in progress. If you want older finished builds, use the releases page rather than assuming the latest branch is a drop-in end-user build.

## Toolchain snapshot

- **Project name:** LocalGen-new
- **Current development line:** `master` / `v6.x`
- **Current version target:** `6.0.0`
- **Primary language:** C++17
- **Frameworks and tools:** Qt6, CMake, SVG assets, GitHub Actions
- **License:** GPL-3.0

## File formats worth knowing

The associated-files guide introduces several formats that show up across gameplay, tooling, and future Qt-era configuration work:

| File | Purpose | Notes |
| --- | --- | --- |
| `.lg` | v5 map file | Legacy map format that still expects paired configuration files. |
| `.lgmp` | v6 map file | The modern map format; designed to stand on its own without a paired ini file. |
| `.lgr` | Replay file | A standard replay format with roughly the same information density as generals.io replays. |
| `.lgra` | Advanced replay file | Stores the normal replay plus richer per-turn information such as queued moves. |
| `settings.lgsts` | v5 settings | Legacy hidden settings file. |
| `config.lgs6` | v6 config | The Qt-era configuration file, expected to move toward a structured format such as JSON. |

## Why the Qt rewrite matters

Across the README and contribution docs, version 6 is framed as a structural transition toward:

- **Qt-based UI modernization**
- **cleaner architecture and maintainability**
- **better platform reach** for Windows, macOS, and Linux workflows
- **a more open bot ecosystem**, including future-friendly external bot integration

## Capabilities already visible across the project

- random and authored maps
- replay support
- map creation workflows
- multiple generations of built-in bots
- a standalone bot simulator
- contribution docs for bots and development workflow

## Where to go next

- Visit the [downloads page]({{< relref "downloads" >}}) for release guidance
- Browse [releases]({{< relref "releases" >}}) for the full release history
- Open the [docs section]({{< relref "docs" >}}) for mirrored project documentation
- Read the [disclaimer]({{< relref "disclaimer" >}}) before redistributing or presenting the project publicly

