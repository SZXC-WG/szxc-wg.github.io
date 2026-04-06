---
title: "Downloads"
description: "Use the same release guidance the README gives: GitHub Releases first, stable builds for players, and caution around the in-progress v6 branch."
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 20
---

## The canonical download source

The upstream README sends users straight to the GitHub releases page. That is still the canonical place to download LocalGen builds:

- [Open LocalGen releases on GitHub](https://github.com/SZXC-WG/LocalGen-new/releases)

The [releases section]({{< relref "releases" >}}) on this site mirrors the release timeline and links back to those download pages.

## What branch are you looking at?

The README also contains an important warning: **the `master` branch is the active v6 rewrite and is not the same thing as a finished end-user release**.

- If you want something proven and historically downloadable, start with **GitHub Releases**.
- If you are tracking the future Qt direction, follow **`master` / `v6.x`** and expect active development.

## Stable vs preview builds

### For most players

Start with the **latest stable GitHub release** if you want the safest entry point.

### For testers and contributors

Use preview or development releases when you want:

- the newest gameplay or bot features
- newer map or replay behavior
- early access to UI and platform changes

## Version lines explained

- **v6 / `master`** — the active Qt rewrite and the main direction of the project
- **v5.x** — the maintenance line behind many historical and older stable downloads

## Platform notes

- Newer development work is oriented around **Qt-based cross-platform support**.
- Historical releases were often built in **Windows-first** environments.
- Some older release notes explicitly recommend **Wine** for running Windows-targeted builds on Linux or macOS.

## Before you launch an older build

Several historical releases mention bundled fonts such as **Quicksand** or **Freestyle Script**. If a release note tells you to install a font from the package, follow that instruction before launching.

## Need details before downloading?

- Read the [release history]({{< relref "releases" >}})
- Check the [FAQ]({{< relref "faq" >}})
- Visit the [source repository](https://github.com/SZXC-WG/LocalGen-new)

