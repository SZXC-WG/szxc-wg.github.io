---
title: "About"
description: "Understand what LocalGen is, how the project is structured, and what makes the v6 rewrite important."
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 10
---

## What is LocalGen?

**Local Generals.io (LocalGen)** is an independent, open-source project that recreates the feeling of generals.io for **local and offline play**.

The project focuses on three major use cases:

- **Offline strategy gameplay** with ready-to-use built-in bots
- **LAN play** with nearby friends
- **Bot and AI experimentation** for developers who want to study or extend the game

## Project snapshot

- **Project name:** LocalGen-new
- **Current development line:** `master` / `v6.x`
- **Current version target:** `6.0.0`
- **Primary language:** C++17
- **Frameworks and tools:** Qt6, CMake, SVG assets, GitHub Actions
- **License:** GPL-3.0

## Branch strategy

LocalGen currently spans two important version lines:

1. **`master` / `v6.x`** — the active Qt-based rewrite
	- focuses on improved portability and maintainability
	- introduces a newer UI architecture
	- expands long-term room for better tooling, bots, and cross-platform support

2. **`v5.x`** — the long-term maintenance line
	- preserves older playable versions
	- remains important for stable legacy downloads
	- reflects the earlier EGE-based era of the project

## Why the v6 rewrite matters

According to the upstream repository, version 6 is not just a feature update. It is a structural transition toward:

- **Qt-based UI modernization**
- **cleaner architecture and maintainability**
- **better platform reach** for Windows, macOS, and Linux workflows
- **a more open bot ecosystem**, including future-friendly external bot integration

## Core features already visible across the project

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

