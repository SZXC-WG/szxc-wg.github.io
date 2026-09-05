---
title: "Evaluate bots"
description: "Run repeated matches and use win rates, OpenSkill, and latency to understand a strategy."
weight: 50
doc_group: play
---

The simulator runs repeated bot matches without opening the graphical interface. It uses the same core board and game logic as the desktop app, making it useful for comparing strategies, checking performance, and testing maps.

## Run your first evaluation

Build the project using [getting started]({{< relref "docs/getting-started" >}}), then run this from `build/Release`:

```bash
./LocalGen-bot-simulator --games 10 --bots XiaruizeBot GcBot
```

In Windows PowerShell, use `./LocalGen-bot-simulator.exe`. To rebuild only the simulator, run this from the source root:

```bash
cmake --build build --config Release --target LocalGen-bot-simulator
```

By default, matches use random 20×20 maps and stop after at most 1000 half-turns each. The program prints individual outcomes followed by a summary table.

## Useful examples

Run ten matches on independently generated maps, with an explicit duration:

```bash
./LocalGen-bot-simulator --games 10 --width 20 --height 20 --steps 1000 --bots XiaruizeBot GcBot
```

Reuse one custom map. Replace this example path with your own `.lgmp`:

```bash
./LocalGen-bot-simulator --games 10 --map maps/arena01.lgmp --steps 1000 --bots XiaruizeBot GcBot
```

On macOS, bundled maps live inside the app. From `build/Release`, use `LocalGen-new.app/Contents/MacOS/maps/arena01.lgmp` for this example, or supply an absolute path to your own map.

Run a multiplayer free-for-all with four workers and measure bot execution time:

```bash
./LocalGen-bot-simulator --games 100 --threads 4 --shuffle --latency --bots SmartRandomBot KtqBot "ZlyBot v2.1" GcBot
```

Print only the final summary:

```bash
./LocalGen-bot-simulator --games 50 --silent --bots XiaruizeBot GcBot
```

## Option reference

| Option | Meaning | Default |
| --- | --- | --- |
| `--games N` | Number of independent matches | `8` |
| `--width N` | Random-map width | `20` |
| `--height N` | Random-map height | `20` |
| `--map PATH` | Use a custom v6 `.lgmp` map | unset |
| `--threads N` | Worker thread count | automatic, capped at match count |
| `--steps N` | Maximum half-turns per match | `1000` |
| `--silent` | Print only the final table | off |
| `--shuffle` | Randomize the bot-to-player-index mapping | off |
| `--latency` | Measure average `requestMove()` latency | off |
| `--bots A B ...` | Two or more registered bot names | `XiaruizeBot GcBot` |
| `--help` / `-h` | Display usage | — |

Numeric values must be positive. Bot names are case-sensitive; quote names that contain spaces. `--map` accepts `.lgmp` only, not legacy `.lg` or official JSON. With a custom map, `--width` and `--height` are ignored. The map needs enough spawn tiles or zero-army blank plains for every participant.

## How matches run

Each bot receives its own team ID, so every match is free-for-all. `--shuffle` changes player-index assignment; it does not create allied teams.

Independent matches run in parallel. Without `--threads`, the program chooses a worker count based on available CPU concurrency, using at least one worker and no more workers than matches. Per-game lines appear in completion order. Rating updates are then accumulated in game-number order, regardless of which match finished first.

## Read the summary

| Column | What it means |
| --- | --- |
| OpenSkill / OS 95% CI | Mean rating for this free-for-all evaluation and its 95% interval |
| Wins / Win Rate / Win 95% CI | Win count, win rate, and its 95% interval |
| Avg Rank | Average final rank; lower places closer to first |
| Avg Kill | Average kills per match |
| Survived | Matches in which the bot remained alive at the end |
| Avg Army / Avg Land | Average final army and land |
| Avg Latency | Average microseconds per `requestMove()` call, when `--latency` is enabled |

The table sorts by OpenSkill mean, then wins. Ratings use the full ranking from each match. Win-rate intervals use the Wilson method; OpenSkill intervals are displayed as `mu ± 1.96 × sigma`.

**At the half-turn limit, the bot ranked first is counted as the winner even if several bots remain alive.** The individual result says `leads at step limit` in that case. Include `--steps` when sharing comparisons so readers know how wins were determined.

## Make comparisons useful

There is currently no command-line seed option. Reusing a custom map reduces terrain variation, but spawn assignments may still change, so repeated runs are not guaranteed to reproduce exactly.

Try several map sizes, map types, opponent combinations, and player counts, with enough matches to see variation. Intervals help describe uncertainty in a sample; they do not remove the influence of your map and opponent choices. Publish the exact command, source revision, platform, and Release build details alongside results.

The simulator currently produces text logs and tables, with no CSV, replay, or training-asset export. See the [simulator source and README](https://github.com/SZXC-WG/LocalGen-new/tree/master/simulator) for implementation details.
