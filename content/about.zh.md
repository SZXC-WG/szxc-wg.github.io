---
title: "关于 LocalGen"
description: "在自己的电脑上玩一局策略游戏，也为地图和 Bot 留一点创造的空间。"
draft: false
weight: 10
---

Local Generals.io，简称 **LocalGen**，是一款由 SZXC-WG 社区维护的开源桌面项目。它把 generals.io 风格的领土策略玩法带到本地：发展兵力、探索地图、保护自己的将军，再寻找突破对手防线的机会。

你可以与内置 Bot 离线对战，也可以编辑一张地图，或编写自己的 Bot，看看一个策略在实际对局中会怎样表现。

## 三种开始方式

### 玩一局

在 **Local Game** 中选择地图和对手，就能开始本地对局。可以由你和 Bot 对战，也可以把所有位置都设为 Bot，观察它们如何行动。排行榜与可选分析图会帮助你回顾兵力和领地的变化。

[了解本地对局]({{< relref "docs/local-game" >}})

### 做一张地图

**Map Creator** 提供地图编辑、导入和保存功能。你可以从空白棋盘开始，也可以修改已有地图，再把保存的 `.lgmp` 文件放进应用的地图目录中游玩。

[开始编辑地图]({{< relref "docs/map-creator" >}})

### 试一个策略

内置 Bot 与游戏一起编译。配套的命令行模拟器可以批量运行 Bot 对局，比较胜率、排名和决策耗时，适合验证想法或改进已有算法。

[认识 Bot]({{< relref "bots" >}}) · [使用模拟器]({{< relref "simulator" >}})

## 当前版本的范围

本站文档面向源码仓库 `master` 分支的 v6 开发版本。它已提供本地对局、地图编辑器和 Bot 模拟器；**局域网联机、Web Game 与回放加载尚未实现**。本地对局支持 2–16 个玩家位置，最多一名人类玩家，采用自由混战模式。

发布版本可能与开发分支不同。下载前请读对应的[版本说明]({{< relref "releases" >}})，其他使用问题可以在[常见问题]({{< relref "faq" >}})中查找。

## 开源，与社区一起成长

LocalGen 使用 C++20、Qt 6、CMake 与 Ninja 构建，持续集成覆盖 Windows、macOS 和 Linux。应用源码采用 GPL-3.0-or-later 许可证，随附 Quicksand 字体使用独立的 SIL Open Font License 1.1。

这个项目独立于 generals.io 及其开发者。你可以阅读[免责声明]({{< relref "disclaimer" >}})，或直接到 [GitHub 仓库](https://github.com/SZXC-WG/LocalGen-new)查看代码、报告问题和参与贡献。
