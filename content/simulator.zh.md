---
title: "Bot 模拟器"
description: "让 Bot 多打几局，用结果理解和改进你的策略。"
draft: false
weight: 70
---

一个 Bot 赢下一局之后，你也许会想：换一张地图呢？对手更多时呢？**LocalGen-bot-simulator** 可以批量运行 Bot 对局，把这些问题变成可以比较的结果。

模拟器与桌面应用共用游戏核心、地图加载器和 Bot 注册表。它通过命令行运行，无需打开游戏界面，并能利用多个 CPU 工作线程同时进行独立对局。

## 先跑一组对局

按照[安装与构建指南]({{< relref "docs/getting-started" >}})完成 Release 构建后，在 `build/Release` 中运行：

```bash
./LocalGen-bot-simulator --games 10 --width 20 --height 20 --steps 1000 --bots XiaruizeBot GcBot
```

Windows PowerShell 使用 `./LocalGen-bot-simulator.exe`，后面的参数相同。这个例子让两个 Bot 在随机地图上交手 10 局，每局最多运行 1000 个半回合。

想换成自己的地图，或只看最后的汇总，可以这样运行：

```bash
./LocalGen-bot-simulator --games 20 --map maps/arena01.lgmp --bots XiaruizeBot GcBot
./LocalGen-bot-simulator --games 50 --silent --latency --bots XiaruizeBot GcBot
```

macOS 的随附地图位于应用包内。从 `build/Release` 运行时，示例路径应改为 `LocalGen-new.app/Contents/MacOS/maps/arena01.lgmp`；也可以使用自己地图的绝对路径。

`--map` 接受 v6 `.lgmp` 文件；使用它时，随机地图的宽高参数会被忽略。地图路径相对于当前命令行工作目录。Bot 名称区分大小写，带空格的名称需要加引号。

## 结果能告诉你什么

汇总表包含 OpenSkill 评分及其 95% 区间、胜场、胜率及其 95% 区间，以及平均排名、击杀、最终兵力、最终领地和存活次数。加上 `--latency` 后，还会显示每次 `requestMove()` 的平均耗时。

这些结果用于比较本次实验中的表现。地图、参赛 Bot、对局数量与步数上限都会影响结论；较少的样本或单一地图，很难代表所有情境。

## 比较结果前，记住这几件事

- 默认运行 8 局，地图为 20×20，每局上限为 **1000 个半回合**，对手为 `XiaruizeBot GcBot`，线程数自动选择。
- 对局均为自由混战。达到步数上限时，即使场上还有多个 Bot 存活，当前排名第一的 Bot 仍会计为本局胜者。
- 每局完成后立即输出结果，因此屏幕上的完成顺序可能与局号不同。`--silent` 会只保留汇总表。
- `--shuffle` 可以打乱玩家编号映射。当前没有命令行随机种子选项，不能保证两次调用逐局复现。

准备分享评测时，请记录源码版本、完整命令、地图和运行环境。更多参数与统计口径见[模拟器完整指南]({{< relref "docs/simulator-guide" >}})；准备贡献新策略时，可以继续阅读[Bot 贡献流程]({{< relref "docs/bot-contributions" >}})。
