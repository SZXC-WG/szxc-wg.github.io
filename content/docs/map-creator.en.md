---
title: "Make a map"
description: "Draw terrain, arrange starting positions, and bring your own map into a local match."
weight: 30
doc_group: play
---

Choose **Create Map** from the main menu to start with a blank 10×10 board. Draw terrain, add spawn points, and save a `.lgmp` file to use in local matches and bot evaluations.

## Draw the board

The width and height sliders each support 1–100. Resizing preserves the area shared by the old and new dimensions.

Click to paint one tile, or right-drag to paint continuously. Left-drag pans the board, the mouse wheel zooms, and `C` fits the board to the window. Up and Down select the previous or next tool.

## Choose terrain and markers

| Tool | Effect in the game |
| --- | --- |
| Mountain | Impassable |
| Lookout | Impassable; the owner of the strongest adjacent positive army receives a 5×5 view centered on the tower |
| Observatory | Impassable; adjacent territory projects a line of sight up to eight tiles beyond the observatory |
| Desert | Occupied desert receives no global army growth at the 25-turn interval |
| Swamp | Usually loses one army per turn while occupied; ownership is lost when the army reaches zero |
| Spawn | A general's starting point; leave its label blank for flexible allocation, or assign a team label from `A`–`Z` |
| City | Set initial strength from -9999 to 9999; default 40 |
| Neutral | Set neutral strength from -9999 to 9999; zero restores a blank tile |
| Light | Toggle whether a tile is visible to every player |
| Erase | Restore a blank, unlit tile |

Placing one spawn for every intended player makes your layout easier to understand. When there are too few explicit spawns, the game tries to fill the remaining positions from zero-army blank plains.

Lettered spawn labels affect spawn-group assignment. Current Local Game matches are still free-for-all; the labels do not create allied teams in the setup UI.

## Name your map

Use the collapsible sidebar to enter a title, author, creation date and time, and plain-text description. Saving as `.lgmp` keeps this information with the map.

Local Game displays the map title with surrounding whitespace removed. It uses the filename when the title is empty, and adds filenames to distinguish duplicate titles.

## Open an existing map

The editor opens three formats:

| Format | How to use it |
| --- | --- |
| `.lgmp` | Native v6 map; reads and writes terrain and metadata |
| `.lg` | Legacy v5 map; reads and writes terrain without v6 metadata |
| Official `.json` | generals.io map; import it and save as `.lgmp` |

The **Import** button can also fetch a public generals.io map by its exact title. This requires an internet connection. Save a local `.lgmp` copy afterward to use it offline.

The JSON importer checks dimensions, tile count, title, and an ISO-8601 `created_at` value. Unknown terrain codes are marked as error tiles so you can correct them before saving.

## Save and play

You can save `.lgmp` or `.lg`, but cannot export official JSON. Use `.lgmp` for new maps. When saving `.lg`, the editor warns that the title, author, date, and description will be discarded.

Place your finished `.lgmp` in the `maps/` directory beside the `LocalGen-new` executable, then reopen **Local Game**. On macOS, the directory is inside the application bundle at `LocalGen-new.app/Contents/MacOS/maps/`.

See [maps and other files]({{< relref "docs/associated-files" >}}) for conversion and format details. To test a map over repeated matches, try the [simulator]({{< relref "docs/simulator-guide" >}}).
