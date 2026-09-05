---
title: "认识内置 Bot"
description: "选择离线对手，了解各个 Bot 的策略和可用名称。"
weight: 40
doc_group: play
---

LocalGen 自带十个已启用的 Bot，下载后即可在本地对局中选择。你也可以让它们彼此对战，观察不同策略如何展开。

## 当前可选对手

下面的名称同时用于本地对局与模拟器。策略和复杂度来自项目的 [Bot 概览](https://github.com/SZXC-WG/LocalGen-new/blob/master/src/bots/README.md)，用于理解实现，并不代表强弱排名。

| Bot | 作者 | 策略 | 单回合复杂度估计 |
| --- | --- | --- | --- |
| `SmartRandomBot` | AppOfficer / GoodCoder666 | 围绕最大兵力栈的贪心策略 | O(n) |
| `KtqBot` | ktq1124298818 / GoodCoder666 | 围绕单一目标的局部贪心 | O(n) |
| `ZlyBot` | AppOfficer | 单目标 BFS 启发式搜索 | O(n) |
| `ZlyBot v2` | AppOfficer | 带记忆的加权搜索 | O(n log n) |
| `ZlyBot v2.1` | AppOfficer | 双焦点防守搜索 | O(n log n) |
| `SzlyBot` | GoodCoder666 | 考虑地形权重的 BFS | O(n) |
| `GcBot` | GoodCoder666 | 自适应启发式 BFS | O(n) |
| `XiaruizeBot` | xiaruize0911 | 多源战略搜索 | O(kn²) |
| `KutuBot` | pinkHC | 统一战略目标规划 | O(n log n) |
| `oimbot` | oimasterkafuu | 带记忆的威胁与目标规划 | O(n²) |

这里的 `n` 是地图格子数，`k` 是多源规划器考虑的候选兵力栈数。复杂度是粗略的单回合最坏情况估计；实际地图中的耗时通常有所不同。

源码中还保留了三个未加入当前构建的实现：

| Bot | 作者 | 策略 | 单回合复杂度估计 |
| --- | --- | --- | --- |
| DummyBot | AppOfficer | 示例型启发式贪心 | O(n) |
| XrzBot | xiaruize0911 | 聚焦型随机贪心 | O(n) |
| LyBot | pinkHC | 多人局目标规划 | O(n²) |

## 在命令行中选择 Bot

名称区分大小写，并保留空格。包含空格的名称需要用引号包起来：

```bash
./LocalGen-bot-simulator --games 20 --bots "ZlyBot v2.1" GcBot
```

`oimbot` 的运行时名称全为小写。如果名称拼错，模拟器会打印可用名称并退出。完整用法见[模拟器指南]({{< relref "docs/simulator-guide" >}})。

## Bot 如何接入项目

内置 Bot 继承 `BasicBot`，实现 `init()` 和 `requestMove()`，将行动放入继承的移动队列。还可以通过 `onWin`、`onCapture`、`onSurrender`、`onText` 钩子接收事件。

每个 Bot 使用 `BotRegistrar` 注册名称，并在顶层 `CMakeLists.txt` 的 `LOCALGEN_BOT_SOURCES` 中启用。桌面应用与模拟器共享这份列表，因此单独把文件放入 `src/bots/` 还不会让它出现在菜单中。

想加入自己的策略，可以从[编写并贡献 Bot]({{< relref "docs/bot-contributions" >}})开始。
