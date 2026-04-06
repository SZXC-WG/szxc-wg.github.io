---
title: "Simulator Guide"
description: "How to use the LocalGen bot simulator for repeatable, threaded bot-vs-bot experiments."
date: 2026-04-06T17:55:08+08:00
draft: false
weight: 60
---

> Source document: [`simulator/README.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/simulator/README.md)

## Overview

`LocalGen-bot-simulator` is a lightweight CLI for evaluating bots against each other.

## Capabilities

- generates random maps using the shared core engine
- instantiates registered bots via the common bot factory
- runs repeated matches without the Qt UI
- prints aggregate summaries and optional per-game results

## Example commands

- `./LocalGen-bot-simulator --games 10 --width 20 --height 20 --steps 600 --bots XiaruizeBot GcBot`
- `./LocalGen-bot-simulator --games 10 --map maps/arena01.lgmp --steps 600 --bots XiaruizeBot GcBot`
- `./LocalGen-bot-simulator --games 50 --silent --bots XiaruizeBot GcBot`

## Custom maps

- `--map PATH` loads a custom map for every simulated game
- only v6 `.lgmp` maps are supported with this flag
- when `--map` is present, `--width` and `--height` are ignored

## Notes

- the simulator shares the same core board and game logic as the main app
- independent matches can run in parallel across CPU threads
- `--silent` suppresses startup and per-game logs, leaving the final summary table
- the summary includes FFA TrueSkill ratings and confidence intervals

