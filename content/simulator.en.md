---
title: "Simulator"
description: "Use the LocalGen bot simulator to run repeatable bot-vs-bot evaluations without the Qt UI."
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 70
---

## What the simulator is for

`LocalGen-bot-simulator` is a lightweight command-line tool for **bot-vs-bot evaluation**.

It uses the same core board and game logic as the main application, but removes the Qt user interface so you can focus on benchmarking and comparison.

## What it can do

- generate random maps
- load custom `.lgmp` maps
- instantiate registered bots through the shared bot system
- run repeated matches in parallel
- report aggregate win-rate and TrueSkill-style summaries

## Example usage

- `./LocalGen-bot-simulator --games 10 --width 20 --height 20 --steps 600 --bots XiaruizeBot GcBot`
- `./LocalGen-bot-simulator --games 10 --map maps/arena01.lgmp --steps 600 --bots XiaruizeBot GcBot`
- `./LocalGen-bot-simulator --games 50 --silent --bots XiaruizeBot GcBot`

## Practical notes

- `--map` loads the same custom map for each simulation
- only v6 `.lgmp` maps are supported by that flag
- independent matches can run across CPU threads
- `--silent` suppresses banner and per-game noise, leaving the summary table

For more detail, read the mirrored [Simulator Guide]({{< relref "docs/simulator-guide" >}}).

