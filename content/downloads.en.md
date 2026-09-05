---
title: "Download LocalGen"
description: "Find the right build for your computer and start your first local match."
draft: false
layout: downloads
weight: 20
---

Release notes and downloads live on [GitHub Releases](https://github.com/SZXC-WG/LocalGen-new/releases). Choose a release, then find the file for your operating system and processor under **Assets**.

**Check the version if you want the features described here.** This site covers the v6 development branch; older releases can have different interfaces and file formats. Versions marked `-dev` or labeled as prereleases are still in development. You can also browse this site's [release history]({{< relref "releases" >}}).

## Choose a file

| System | Processor | File type |
| --- | --- | --- |
| Windows | x86_64 for most Intel / AMD PCs; ARM64 for ARM PCs | `.zip` |
| macOS | x86_64 for Intel; ARM64 for Apple silicon | `.dmg` |
| Linux | x86_64 or ARM64, matching your system | `.AppImage` |

These are the current continuous-integration packaging targets; **individual releases may offer only some of them**. Windows builds may also distinguish MSVC, MinGW, and LLVM-MinGW. Follow the asset names and release notes.

To play the game, choose an application package. GitHub's automatic **Source code** archives require you to compile the project yourself.

## Open the app

- **Windows:** Extract the whole ZIP and run `LocalGen-new.exe`. Keep its dependency files and the `maps/` and `fonts/` folders together.
- **macOS:** Open the DMG, copy the application to your computer as indicated, and launch it.
- **Linux:** Give the AppImage execute permission, then run it. If Debian or Ubuntu reports a missing OpenGL runtime, install `libopengl0`.

In v6, choose **Local Game** to set up an offline match. [Your first local game]({{< relref "docs/local-game" >}}) introduces the maps, players, and controls.

## Use a development build

The source repository's [Qt Build workflow](https://github.com/SZXC-WG/LocalGen-new/actions/workflows/qt-build.yml) builds the development branch and uploads packages after successful runs. These artifacts reflect a particular commit and are managed separately from published releases.

To build locally, prepare a C++20 compiler, Qt 6.7+, CMake 3.19+, and Ninja 1.10+, then follow [Installation and building]({{< relref "docs/getting-started" >}}). **Build from source for the bot simulator too:** the current CI desktop packages do not include its executable.

For launch or version problems, check the [FAQ]({{< relref "faq" >}}). If you need help, report your operating system, app version, and error details in [GitHub Issues](https://github.com/SZXC-WG/LocalGen-new/issues).
