---
title: "Bot Contributions"
description: "How LocalGen v6 welcomes built-in and external bot development contributions."
date: 2026-04-06T17:55:07+08:00
draft: false
weight: 20
---

> Source document: [`docs/bot-contributions.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/docs/bot-contributions.md)

## Introduction

Bots have always been central to LocalGen. Earlier project versions made bot development much harder than it needed to be:

- bots could only be written in C++
- they had to be compiled into the main binary
- the API surface was effectively hard-coded into the source tree

Version 6 is meant to loosen those constraints and welcome a broader contributor base.

## Bot types in v6

### Built-in bots

- source lives under `src/bots/`
- compiled together with the LocalGen executable
- written in C++
- directly available in Local Game and Web Game modes

### External bots

- stand-alone executables
- may be written in any language
- communicate with LocalGen through a network protocol
- can be supervised by the game process once integrated into the external-bot list

## How you can contribute

The project welcomes:

- brand-new bots
- improvements to existing bots
- bug fixes and performance optimizations

### Contributing a built-in bot

1. Read [`src/bots/README.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/src/bots/README.md).
2. Follow the project’s C++ style rules.
3. Submit a pull request with:
	- tests and/or replay evidence
	- a short performance report

### Contributing an external bot

1. Implement the documented communication protocol.
2. Provide a working binary or reliable build script.
3. State clearly in your PR:
	- dependencies and launch instructions
	- supported operating systems and runtime environments
	- expected performance characteristics

## Community standards for bots

- keep the code clean and documented
- test on different maps and player counts
- avoid placeholder random-move bots
- stay within the game’s practical per-turn performance limits
- remain stable across long matches without obvious memory leaks

