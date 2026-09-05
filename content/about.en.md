---
title: "About LocalGen"
description: "A strategy game on your own computer, with room to create maps and explore bot ideas."
draft: false
weight: 10
---

**Local Generals.io**, or **LocalGen**, is an open-source desktop project maintained by the SZXC-WG community. It brings generals.io-style territory strategy to your computer: build your army, explore the map, protect your general, and find an opening in your opponent's defenses.

Play offline against built-in bots, create a map, or write your own bot to see how a strategy behaves in a real match.

## Three ways to start

### Play a match

Choose a map and opponents in **Local Game**. Take a player slot yourself, or fill every slot with a bot and watch them play. The leaderboard and optional analysis charts help you follow changes in army size and territory.

[Learn about local matches]({{< relref "docs/local-game" >}})

### Make a map

**Map Creator** lets you edit, import, and save maps. Start with an empty board or change an existing map, then place the saved `.lgmp` file in the app's map directory to play it.

[Start creating maps]({{< relref "docs/map-creator" >}})

### Try a strategy

Built-in bots compile with the game. The companion command-line simulator runs batches of matches and reports win rates, rankings, and optional decision timings, giving you a way to test ideas and improve algorithms.

[Meet the bots]({{< relref "bots" >}}) · [Use the simulator]({{< relref "simulator" >}})

## What is available

This site's documentation covers the v6 development version on the source repository's `master` branch. Local matches, Map Creator, and the bot simulator are available. **LAN play, Web Game, and replay loading are not implemented yet.** Local matches have 2–16 player slots, with at most one human player, and use free-for-all rules.

Published releases can differ from the development branch. Read the relevant [release notes]({{< relref "releases" >}}) before downloading, or visit the [FAQ]({{< relref "faq" >}}) for common questions.

## Open source, built by a community

LocalGen uses C++20, Qt 6, CMake, and Ninja, with continuous integration for Windows, macOS, and Linux. The application source uses GPL-3.0-or-later; the bundled Quicksand fonts have a separate SIL Open Font License 1.1.

The project is independent of generals.io and its developers. Read the [disclaimer]({{< relref "disclaimer" >}}), or visit the [GitHub repository](https://github.com/SZXC-WG/LocalGen-new) to explore the code, report a problem, or contribute.
