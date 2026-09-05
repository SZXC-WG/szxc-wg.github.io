---
title: "Contribute"
description: "Start with a question, a map, or a few lines of code, and help make LocalGen better."
draft: false
weight: 80
---

You are welcome to contribute to LocalGen. You do not need to understand the whole codebase first: clarifying a paragraph, documenting a reproducible problem, or sharing an interesting map is a useful place to start.

## Find your starting point

- **Found a problem?** Open an [issue](https://github.com/SZXC-WG/LocalGen-new/issues) with your version, operating system, steps, and what happened. Screenshots, error messages, or a relevant map help others investigate.
- **Have an idea?** Explain the problem you want to solve and how you would use the feature. Discuss the design and scope first for larger changes.
- **Enjoy maps or writing?** Improve a map, add an example, or refine documentation and translations to make the next person's experience easier.
- **Want to code?** The interface, game logic, bots, simulator, performance, builds, and packaging all offer opportunities to help.

## Prepare your environment

New features and routine fixes target v6 on `master`. Versions 1–4 are retired; v5 only accepts security and critical bug fixes.

The current build requires **C++20, Qt 6.7+, CMake 3.19+, and Ninja 1.10+**. Follow [Installation and building]({{< relref "docs/getting-started" >}}), then build both Debug and Release:

```bash
cmake -B build -S . -G "Ninja Multi-Config" -DCMAKE_TOOLCHAIN_FILE=/path/to/qt.toolchain.cmake
cmake --build build --config Debug
cmake --build build --config Release
```

Replace the toolchain path with your actual Qt installation path. Use Debug to investigate problems and Release to measure performance.

## Make your change easy to review

Give each pull request a clear purpose. Explain the problem, the resulting behavior, and how you checked it. Screenshots help with interface changes; simulator commands and results help with bot changes. Update documentation when behavior, file formats, or dependencies change.

Follow the [naming conventions]({{< relref "docs/naming-method" >}}) and [commit guidelines]({{< relref "docs/commit-regulations" >}}). For example:

```text
fix(ui): preserve map selection when changing player count
```

## Contribute a bot

The project currently accepts C++ bots compiled with the application. Along with a working implementation, include a short algorithm explanation and evaluation results across maps and player counts. Describe per-turn timing and stability during long games.

The [bot contribution guide]({{< relref "docs/bot-contributions" >}}) covers integration; the [simulator documentation]({{< relref "docs/simulator-guide" >}}) helps you prepare an evaluation. Use the current `BasicBot`, `BotRegistrar`, and `CMakeLists.txt` source as the reference for interfaces.

## Keep the conversation welcoming

Contributors with different backgrounds and experience levels are welcome. Focus on the problem, respect each other, and offer specific, useful feedback. Read the [Code of Conduct]({{< relref "docs/code-of-conduct" >}}) and the repository's [CONTRIBUTING.md](https://github.com/SZXC-WG/LocalGen-new/blob/master/CONTRIBUTING.md) before participating.
