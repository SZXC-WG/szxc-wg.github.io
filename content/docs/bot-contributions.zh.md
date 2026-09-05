---
title: "编写并贡献 Bot"
description: "把自己的策略接入 LocalGen，在本地对局和模拟器中测试，再提交贡献。"
weight: 70
doc_group: develop
---

你可以编写一个新的 Bot，也可以改进现有策略、修复问题或缩短思考时间。当前 v6 使用直接编译进程序的 C++ Bot，同一个实现可以在本地对局和模拟器中运行。

开始前先按[快速开始]({{< relref "docs/getting-started" >}})完成一次构建，再阅读项目的[贡献指南](https://github.com/SZXC-WG/LocalGen-new/blob/master/CONTRIBUTING.md)和 [Bot 目录说明](https://github.com/SZXC-WG/LocalGen-new/blob/master/src/bots/README.md)。其中部分旧说明仍在整理，下面的接口和注册方式以当前源码为准。

## 创建一个实现文件

在 `src/bots/` 下创建名称唯一的 `.cpp` 文件，将实现放在这个文件中。当前工程要求 **C++20**。Bot 类继承 `BasicBot`，并实现两个必需方法：

```cpp
#include "core/bot.h"
#include "core/game.hpp"

class MyBot : public BasicBot {
public:
    void init(index_t playerId,
              const GameConstantsPack& constants) override {
        // 保存玩家身份，并初始化本局使用的状态。
    }

    void requestMove(const BoardView& boardView,
                     const std::vector<RankItem>& rank) override {
        // 根据当前视野与排行榜，将计划动作加入 moveQueue。
    }
};

static BotRegistrar<MyBot> myBotRegistrar("MyBot");
```

这个骨架只展示接口，还没有策略。`core/bot.h` 对应源码中的 `src/core/bot.h`，可以通过项目已有的包含目录找到。

`init()` 接收本局玩家编号和规则常量；`requestMove()` 接收当前视野与排行榜。移动放入继承的 `moveQueue`。如果策略需要处理游戏事件，还可以覆写 `onWin`、`onCapture`、`onSurrender` 和 `onText`。

## 注册并加入构建

使用 `BotRegistrar` 注册唯一运行时名称。当前接口没有 `REGISTER_BOT` 宏；名称的大小写与空格会原样用于菜单和命令行。

接着把源文件加入顶层 `CMakeLists.txt` 中的 `LOCALGEN_BOT_SOURCES`，例如：

```cmake
set(LOCALGEN_BOT_SOURCES
    # 保留已有 Bot 源文件。
    src/bots/MyBot.cpp
)
```

这份列表由桌面应用和模拟器共用。重新构建后，检查本地对局菜单中是否出现 `MyBot`，再跑一组模拟器对战：

```bash
./LocalGen-bot-simulator --games 50 --steps 1000 --latency --bots MyBot GcBot
```

## 测试你的策略

请同时构建 Debug 和 Release，使用 Release 进行性能比较。除了默认随机地图，也试试不同尺寸、自定义地图、多个对手和不同玩家数量。检查长局中的内存使用与计算量，避免状态无限增长。

一份有用的评测报告应包含：

- 完整命令、源码版本和构建环境；
- 对局数、半回合上限、地图尺寸或所用 `.lgmp`；
- 胜率、OpenSkill、平均排名和击杀；
- `--latency` 得到的思考耗时；
- 已知失败场景，以及单回合最坏情况复杂度与内存需求。

模拟器没有种子参数，固定地图也不能保证完全复现。因此请用多组、足量比赛描述策略表现。更多输出含义见[模拟器指南]({{< relref "docs/simulator-guide" >}})。

## 准备 Pull Request

在说明中介绍策略想解决的问题、主要做法和测试结果。保持代码可读，在不容易理解的地方解释原因；同时更新 Bot 阵容说明。项目欢迎有明确策略的实现，纯随机移动的占位代码不适合作为正式 Bot 提交。

开发工作面向 v6 的 `master` 分支。外部可执行 Bot、任意语言客户端和网络 Bot 协议尚未接入当前版本。
