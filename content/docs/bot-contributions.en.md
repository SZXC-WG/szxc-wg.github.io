---
title: "Build and contribute a bot"
description: "Connect your strategy to LocalGen, test it in matches and the simulator, and prepare a contribution."
weight: 70
doc_group: develop
---

You can add a new bot, improve an existing strategy, fix a bug, or reduce calculation time. Current v6 bots are C++ implementations compiled directly into the program. The same implementation runs in Local Game and the simulator.

First complete a build using [getting started]({{< relref "docs/getting-started" >}}), then read the project's [contribution guide](https://github.com/SZXC-WG/LocalGen-new/blob/master/CONTRIBUTING.md) and [bot directory guide](https://github.com/SZXC-WG/LocalGen-new/blob/master/src/bots/README.md). Some older instructions are still being updated; the API and registration method below follow the current source.

## Create an implementation file

Create a uniquely named `.cpp` under `src/bots/` and keep your implementation in that file. The project currently requires **C++20**. Inherit from `BasicBot` and implement both required methods:

```cpp
#include "core/bot.h"
#include "core/game.hpp"

class MyBot : public BasicBot {
public:
    void init(index_t playerId,
              const GameConstantsPack& constants) override {
        // Store the player identity and initialize this match's state.
    }

    void requestMove(const BoardView& boardView,
                     const std::vector<RankItem>& rank) override {
        // Use the current view and ranking to add actions to moveQueue.
    }
};

static BotRegistrar<MyBot> myBotRegistrar("MyBot");
```

This skeleton demonstrates the interface; it does not yet contain a strategy. `core/bot.h` resolves to `src/core/bot.h` through the project's existing include directories.

`init()` receives the player ID and rule constants for the match. `requestMove()` receives the current board view and ranking. Add planned moves to the inherited `moveQueue`. To handle game events, you can also override `onWin`, `onCapture`, `onSurrender`, and `onText`.

## Register and include it in the build

Register a unique runtime name with `BotRegistrar`. The current API has no `REGISTER_BOT` macro. Capitalization and spaces in the registered name are preserved in menus and command-line arguments.

Add your source to `LOCALGEN_BOT_SOURCES` in the top-level `CMakeLists.txt`, keeping the existing entries:

```cmake
set(LOCALGEN_BOT_SOURCES
    # Keep the existing bot source files here.
    src/bots/MyBot.cpp
)
```

The desktop app and simulator share this list. After rebuilding, check that `MyBot` appears in Local Game, then run an evaluation:

```bash
./LocalGen-bot-simulator --games 50 --steps 1000 --latency --bots MyBot GcBot
```

## Test your strategy

Build both Debug and Release, and use Release for performance comparisons. Alongside default random maps, try different dimensions, custom maps, several opponents, and different player counts. Check memory use and calculation time in long games so state does not grow without bounds.

A useful evaluation report includes:

- the exact command, source revision, and build environment;
- match count, half-turn limit, and map dimensions or the chosen `.lgmp`;
- win rate, OpenSkill, average rank, and kills;
- execution time measured with `--latency`;
- known failure cases, worst-case per-turn complexity, and memory needs.

The simulator has no seed option, and a fixed map does not guarantee identical runs. Use several sufficiently large batches when describing a strategy. The [simulator guide]({{< relref "docs/simulator-guide" >}}) explains the output in detail.

## Prepare a pull request

Describe the problem your strategy addresses, its main approach, and your test results. Keep the code readable and explain decisions where they are difficult to infer. Update the bot roster documentation too. The project welcomes deliberate strategies; a random-move placeholder is not suitable as a finished bot contribution.

Development contributions target the v6 `master` branch. External executable bots, arbitrary-language clients, and network bot protocols are not yet connected in this version.
