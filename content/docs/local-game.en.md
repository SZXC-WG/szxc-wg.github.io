---
title: "Your first match"
description: "Choose a map and an opponent, then learn how to move your army and follow the game."
weight: 20
doc_group: start
---

Open **Local Game** and start with a 20×20 `Standard` map, speed 1, and two players. Leave P1 as `Human`, choose a bot for the other player, and click **Start Game**.

## Adjust the match

| Setting | How it works |
| --- | --- |
| Game Speed | From 1–1000; speed 1 advances about one full turn per second |
| Show analysis | Displays live army and land charts |
| Game Map | `Standard` creates a fresh random map; other entries come from local `.lgmp` files |
| Map size | Random maps allow width and height from 1–100, defaulting to 20×20; custom maps use their stored dimensions |
| Player count | 2–16; only P1 can be `Human`, while every slot can use a bot |

To watch bots explore their strategies, set P1 to a bot as well. Local Game currently supports at most one human, and every player competes independently; there is no team selector. **Enable sounds** is currently disabled.

The speed setting targets `500 / speed` milliseconds per half-turn. Bot calculations take time, so actual speed also depends on the map, opponents, and your hardware.

## Move your army

Click one of your tiles, then use the arrow keys or `W A S D` to queue moves through neighboring tiles. An ordinary move leaves one soldier behind; press `Z` to send half the army on the next move. Mountains, lookouts, and observatories are impassable.

Press several direction keys to plan a route in advance. If a queued move is no longer legal when it is processed, the game skips it.

| Shortcut | Action |
| --- | --- |
| Arrow keys / `W A S D` | Move focus and queue an ordinary move |
| `I J K L` | Move focus only |
| Shift + arrow keys / WASD | Move focus only |
| `Z` | Send half the army on the next queued move |
| `Q` | Clear the move queue |
| `E` | Remove the last queued move and return to its starting tile |
| Space | Clear tile focus |
| `H` | Focus your general |
| `G` | Focus your general and move the camera there |
| Escape | Open surrender confirmation |

## Find your way around

| Control | Action |
| --- | --- |
| Left-drag | Pan the board |
| Mouse wheel | Zoom around the pointer |
| Touchpad scroll | Pan the board |
| Pinch gesture | Zoom |
| `9` / `0` | Zoom out / in |
| `C` | Fit and center the whole map |

Press Enter to focus the chat input, then Enter again to send non-empty text. Input is shown only when a human participates. The message panel also records system notices, captures, surrenders, and the winner for the current local match.

## Follow the game

A trailing dot on the turn label distinguishes one half-turn phase. The leaderboard shows each player's army and land. Click it to collapse or expand player names. Eliminated players are shaded, and a skull marks players with kills.

If you enabled **Show analysis**, switch between army and land, or linear and logarithmic scales. Once the human is eliminated, the full board is revealed so you can keep watching. The full map also appears when the match ends, and move input stops.

## When a custom map will not start

A match needs a valid, non-empty board and enough spawn tiles or zero-army blank plains for every player. If there are too few starting positions, reduce the player count or add spawns in the [map editor]({{< relref "docs/map-creator" >}}).

To add a map, place a `.lgmp` file in `maps/` beside the executable and reopen the Local Game dialog.
