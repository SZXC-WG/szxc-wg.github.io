---
title: "Simulator"
description: "Use the LocalGen bot simulator for reproducible bot-vs-bot testing on random or custom maps, without the Qt UI in the loop."
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 70
---

## What the simulator is for

`LocalGen-bot-simulator` is the tool you reach for when you want evidence instead of guesswork. It is a lightweight command-line companion for **bot-vs-bot evaluation**.

It uses the same core board and game logic as the main application, but removes the Qt user interface so you can focus on benchmarking, regression checking, and large-scale comparison runs.

## What it can do

- generate random maps
- load custom `.lgmp` maps
- instantiate registered bots through the shared bot system
- run repeated matches in parallel
- report aggregate win-rate and TrueSkill-style summaries

## Why contributors use it

The bot contribution guide repeatedly asks for evidence: replays, tests, and performance notes. The simulator is the cleanest way to collect that evidence when you want to compare multiple strategies under consistent settings, share meaningful benchmarks, and prove that a new idea is more than a lucky streak.

## Example usage

```bash
./LocalGen-bot-simulator --games 10 --width 20 --height 20 --steps 600 --bots XiaruizeBot GcBot
./LocalGen-bot-simulator --games 10 --map maps/arena01.lgmp --steps 600 --bots XiaruizeBot GcBot
./LocalGen-bot-simulator --games 50 --silent --bots XiaruizeBot GcBot
```

## A simple evaluation formula

When comparing two bots over many games, a first-pass headline metric is still the win rate:

$$
	ext{win-rate} = \frac{W}{W + L} \times 100\%
$$

If you keep the map size fixed, a rough experiment budget can be thought of as:

$$
T_{\text{suite}} \approx G \times S \times T_{\text{turn}}(n)
$$

where $G$ is the number of games, $S$ is the step limit, and $T_{\text{turn}}(n)$ is the average per-turn bot cost on a board of effective size $n$.

## Practical notes

- `--map` loads the same custom map for each simulation
- only v6 `.lgmp` maps are supported by that flag
- independent matches can run across CPU threads
- `--silent` suppresses banner and per-game noise, leaving the summary table

For more detail, read the mirrored [Simulator Guide]({{< relref "docs/simulator-guide" >}}).

