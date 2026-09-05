---
title: "认识 Bot"
description: "挑选一个对手，观察不同策略，或者写出自己的第一个 Bot。"
draft: false
weight: 60
---

Bot 是由程序控制的对手。LocalGen 的内置 Bot 随应用一起提供，选择名称就能加入对局，无需另外安装模型或配置服务。

第一次游玩时，可以先在 **Local Game** 中保留 P1 为 `Human`，为其他位置选择 Bot。如果想观察它们的策略，也可以把 P1 改成 Bot，让整场对局自动进行。

## 不同的对手，不同的思路

当前开发分支编译了以下 10 个 Bot。这里的介绍概括了实现思路，供你挑选和阅读源码；它们的实际表现会随地图、对手和玩家数量而变化。

| Bot 名称 | 策略思路 | 作者 |
| --- | --- | --- |
| SmartRandomBot | 优先从最大的兵力栈行动 | AppOfficer / GoodCoder666 |
| KtqBot | 围绕一个目标进行局部贪心选择 | ktq1124298818 / GoodCoder666 |
| ZlyBot | 结合广度优先搜索与启发式评估 | AppOfficer |
| ZlyBot v2 | 在加权搜索中记住已探索的信息 | AppOfficer |
| ZlyBot v2.1 | 使用双焦点搜索，兼顾防守 | AppOfficer |
| SzlyBot | 在搜索中考虑地形权重 | GoodCoder666 |
| GcBot | 根据局面调整启发式搜索 | GoodCoder666 |
| XiaruizeBot | 从多个兵力来源规划行动 | xiaruize0911 |
| KutuBot | 统一评估和选择战略目标 | pinkHC |
| oimbot | 结合记忆、威胁判断与目标规划 | oimasterkafuu |

源码中还保留了 DummyBot、XrzBot 和 LyBot，但它们未加入当前构建的 Bot 列表。你下载的版本可能包含不同的阵容，以应用里的实际选项为准。

## 想知道哪种策略更适合一张地图？

用[模拟器]({{< relref "simulator" >}})运行一批对局，可以同时观察胜率、平均排名、击杀与决策耗时。多换几张地图和几组对手，比只看一局的胜负更能帮助你理解策略的特点。

模拟器使用上表中的准确名称；包含空格的名称要加引号，例如 `"ZlyBot v2.1"`。`oimbot` 使用全小写。

## 把自己的想法写成 Bot

当前 Bot 使用 **C++20**，直接编译进桌面应用和模拟器。一个实现通常放在单个 `src/bots/*.cpp` 文件中，继承 `BasicBot`，实现 `init(...)` 和 `requestMove(...)`，再通过 `BotRegistrar` 注册，并加入 `CMakeLists.txt` 的 `LOCALGEN_BOT_SOURCES`。

目前没有外部 Bot 进程或 Python 客户端接口。开始编写前，可以先读[内置 Bot 参考]({{< relref "docs/built-in-bots" >}})；准备分享成果时，再按[Bot 贡献指南]({{< relref "docs/bot-contributions" >}})整理算法说明与评测结果。
