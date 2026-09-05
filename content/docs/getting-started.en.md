---
title: "Getting started"
description: "Download LocalGen and play an offline match, then build from source when you are ready."
weight: 10
doc_group: start
---

To play your first match, download a release package for your system. Qt, CMake, and a compiler are only needed when building from source.

## Download and play

1. Visit [GitHub Releases](https://github.com/SZXC-WG/LocalGen-new/releases), read the notes for your chosen version, and download the matching system package.
2. Extract or install it as described in the release. For portable packages, keep the complete folder, including `maps/`, `fonts/`, and the bundled runtime libraries.
3. Launch LocalGen and choose **Local Game**. Start with a `Standard` 20×20 map at speed 1, leave P1 set to `Human`, and choose a bot opponent.

Continue to [your first match]({{< relref "docs/local-game" >}}) for movement and camera controls.

The rest of this page covers building Qt-based v6 from source. These instructions follow `6.0.0-dev`; packaged releases may have different features, as described in their release notes.

## Prepare a build environment {#build}

| Tool | Requirement |
| --- | --- |
| Qt | 6.7 or newer, with Widgets, SVG, Network, and Charts |
| CMake | 3.19 or newer |
| Ninja | 1.10 or newer |
| C++ compiler | C++20 support, compatible with your Qt toolchain |

Make sure your terminal can find `cmake`, `ninja`, and the compiler tools. Download or clone the [source repository](https://github.com/SZXC-WG/LocalGen-new), then locate your Qt toolchain file. It is usually at:

```text
$QT_ROOT_DIR/lib/cmake/Qt6/qt.toolchain.cmake
```

## Configure and build

Run these commands from the source root, replacing the example path with your actual Qt toolchain path:

```bash
cmake -B build -S . -G "Ninja Multi-Config" -DCMAKE_TOOLCHAIN_FILE=/path/to/qt.toolchain.cmake
cmake --build build --config Release
```

Use `--config Debug` to investigate problems. Before contributing code, check both Debug and Release builds; use Release for bot performance comparisons.

A normal build creates two programs:

| Program | Purpose |
| --- | --- |
| `LocalGen-new` | Desktop app for local matches and map editing |
| `LocalGen-bot-simulator` | Command-line tool for repeated bot evaluations |

## Find the build output

With the commands above, Release outputs are located at:

```text
Windows: build\Release\LocalGen-new.exe
Linux:   build/Release/LocalGen-new
macOS:   build/Release/LocalGen-new.app
```

The build copies `maps/` and `fonts/` beside the desktop executable. On macOS, that executable is inside `.app/Contents/MacOS/`. The app looks there for maps and loads three bundled Quicksand font files. If a font warning appears, first check that those files are present.

To check that the simulator runs, execute this from `build/Release`:

```bash
./LocalGen-bot-simulator --games 8 --bots XiaruizeBot GcBot
```

In Windows PowerShell, use `./LocalGen-bot-simulator.exe`. See the [simulator guide]({{< relref "docs/simulator-guide" >}}) for more options.

## Packaging and startup help

- **Windows:** use Qt's `windeployqt` after building to package the runtime libraries. Keep the map and font directories too.
- **macOS:** use the project script: `bash scripts/package-macos-dmg.sh build/Release/LocalGen-new.app LocalGen-new.dmg`. It handles framework deployment, package cleanup, and ad-hoc signing. The project README advises against using `macdeployqt ... -dmg` directly because it can leave the copied app with an invalid signature.
- **Linux:** if an AppImage fails on Debian/Ubuntu because the OpenGL runtime is missing, install `libopengl0` with `sudo apt install libopengl0`.

In v6, **Web Game** and **Load Replay** currently display a message that the feature is not implemented. Local Game and Map Creator are ready to use.
