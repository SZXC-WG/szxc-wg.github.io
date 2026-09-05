---
title: "Maps and other files"
description: "Find your map folder, convert older formats, and check what v6 can read and save."
weight: 60
doc_group: play
---

Use **`.lgmp`** when creating or sharing a new map. It is the native v6 format, keeps both terrain and map information, and works directly in Local Game and the simulator.

## Supported files

| File | Purpose | Current v6 support |
| --- | --- | --- |
| `.lgmp` | Native v6 map | Editor reads and writes; Local Game and simulator read |
| `.lg` | v5 map | Editor reads and writes; not listed directly in Local Game |
| Official `.json` | generals.io map exchange | Editor imports; cannot export or start a match directly |
| `.lgr` | Standard replay | Reserved format name; loading and saving are not implemented |
| `.lgra` | Advanced replay | Reserved format name; loading and saving are not implemented |
| `settings.lgsts` | v5 settings | Historical reference |
| `settings.json` | v6 settings filename | Documented name; the app does not yet persist settings |

## Where maps go

Place valid `.lgmp` files in `maps/` beside the `LocalGen-new` executable, then reopen the Local Game dialog. The app scans this folder and displays map titles, falling back to filenames for empty titles and adding filenames for duplicates.

Windows and Linux portable folders usually contain the executable and `maps/` together. On macOS, the location is inside the application bundle: `LocalGen-new.app/Contents/MacOS/maps/`.

The simulator's `--map PATH` can read a `.lgmp` from the location you specify; it does not need to be in this folder.

## Convert an older map

Open a `.lg` or official map `.json` in the [map editor]({{< relref "docs/map-creator" >}}). Check the terrain, add a title and author, and save as `.lgmp`.

Legacy `.lg` stores only board encoding. The editor generates a title and creation time when opening it, and saving back to `.lg` discards v6 metadata. Official JSON needs valid `width`, `height`, `map`, `title`, and ISO-8601 `created_at` fields; author and description are optional. The editor can also fetch public maps with this structure by name while online.

## Inside a `.lgmp`

The format uses a Qt binary data stream, so it cannot be edited as JSON. It contains a format identifier, title, author, creation date and time, description, dimensions, and compressed tile records. Each tile includes its type, globally visible “lit” flag, and an army value or spawn-team label.

The editor supports width and height from 1–100. A map that opens successfully may still be too small for your chosen player count: starting a match also requires enough spawn tiles or zero-army blank plains.

The project's [associated-file reference](https://github.com/SZXC-WG/LocalGen-new/blob/master/docs/associated-files.md) also documents planned replay and settings filenames. Map files are currently usable; the **Load Replay** menu entry still displays a message that it is not implemented.
