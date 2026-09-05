---
title: "Frequently asked questions"
description: "Common questions about installation, offline play, maps, and bots."
draft: false
weight: 90
---

These answers cover the v6 development branch. If you use an older release, also check the notes on its download page.

## Where should I start?

Choose a package for your computer on the [download page]({{< relref "downloads" >}}), then extract or install it completely. Launch the app, choose **Local Game**, keep the first slot set to `Human`, and choose your bot opponents. The [local game guide]({{< relref "docs/local-game" >}}) explains the controls.

## Do I need an internet connection?

Local matches, editing maps on your computer, and the simulator all work offline. Map Creator's optional **Import from Generals.io** feature fetches a map from the public map API, so that operation needs a connection.

## Can I play with friends over a network or on one computer?

Current v6 does not have LAN or Web Game support. Local matches have 2–16 player slots, with only P1 offering a human player; the other slots use bots. You can also fill all slots with bots. Matches currently use free-for-all rules.

## Why do Web Game and Load Replay not work?

Both features are still in development. Their buttons currently show a message explaining that they are not implemented. The app cannot load `.lgr` or `.lgra` replays yet.

## How do I play a map I made?

Save it as `.lgmp` in Map Creator, place it in the `maps/` directory beside the executable, and reopen Local Game setup. It needs enough spawn points or empty plain tiles for the selected players.

Map Creator can also read legacy `.lg` files and generals.io map JSON, but it saves only `.lg` or `.lgmp`. Choose `.lgmp` for current local matches. See [Map Creator]({{< relref "docs/map-creator" >}}) and [file formats]({{< relref "docs/associated-files" >}}).

## What if the app reports missing fonts?

Check that you extracted the whole package and kept `fonts/` beside the executable. The app reads three Quicksand font files from that folder. Keep `maps/` too. For a DMG or AppImage, preserve the application bundle's internal structure.

## What if the Linux AppImage reports a missing OpenGL runtime?

On Debian or Ubuntu, install `libopengl0`. For other distributions, use the equivalent OpenGL runtime package. If the error continues, include the full message, distribution, and processor architecture in your report.

## Can I write a bot in Python?

Current bots use C++20 and compile with the app. There is no Python client or external bot process interface yet. Start with [Meet the bots]({{< relref "bots" >}}) and the [bot contribution guide]({{< relref "docs/bot-contributions" >}}).

## Will two simulator runs produce the same results?

Usually not. The current CLI has no option for choosing a random seed, and random map seeds come from system randomness. Recording your source version, full command, map, and environment—and running more games—helps comparison, but does not guarantee match-by-match reproduction.

## Are settings saved? Does the sound option work?

Current v6 does not persist settings between launches. You will need to configure them again after restarting. The **Enable sounds** option is visible, but sound playback is not connected yet.

## Is LocalGen an official generals.io project?

No. It is an independent community open-source project with no official affiliation to generals.io or its developers. Read the [disclaimer]({{< relref "disclaimer" >}}) for details.

## Where can I ask for help?

Report bugs or ideas in [GitHub Issues](https://github.com/SZXC-WG/LocalGen-new/issues). Include your app version, operating system, reproduction steps, and screenshots when useful. To help improve the project yourself, see [Contribute]({{< relref "contribute" >}}).
