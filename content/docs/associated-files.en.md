---
title: "Associated Files"
description: "Reference for LocalGen-related map, replay, and configuration file formats."
date: 2026-04-06T17:55:07+08:00
draft: false
weight: 50
---

> Source document: [`docs/associated-files.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/docs/associated-files.md)

## File format reference

| Extension / file name | Type | Notes |
| --- | --- | --- |
| `.lg` | Map file | Legacy LocalGen v5 map file; typically paired with an ini file. |
| `.lgmp` | Map file | Native LocalGen v6 map format; does not require the paired ini workflow and may use JSON-style structure. |
| `.lgr` | Replay file | Standard replay format, roughly comparable to generals.io replay information density. |
| `.lgra` | Advanced replay file | Stores the normal replay data plus extra details such as per-turn move queues. |
| `settings.lgsts` | Settings file | LocalGen v5 settings file; typically hidden by default. |
| `config.lgs6` | Settings file | LocalGen v6 configuration file; expected to be hidden and likely JSON-based. |

These file types matter for players, map authors, replay analysis, and tooling contributors alike.

