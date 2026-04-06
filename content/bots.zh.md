---
title: "机器人"
description: "了解 LocalGen 的 Bot 生态：从轻量示例到高阶策略规划器。"
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 60
---

## Bot 生态概览

Bot 是 LocalGen 最具代表性的部分之一，既服务于游戏体验，也服务于 AI / 策略研究。项目文档明确欢迎新的 Bot 贡献。

上游文档将 Bot 分为两大类：

1. **内置 Bot**
	- 源码位于 `src/bots/`
	- 与 LocalGen 主程序一起编译
	- 使用 C++ 编写，集成度和性能都更高

2. **外部 Bot**
	- 作为独立可执行程序存在
	- 可以使用任意语言编写
	- 通过网络协议与游戏通信，降低贡献门槛

## 当前内置 Bot 阵容

| Bot | 作者 | 状态 | 简介 |
| --- | --- | --- | --- |
| SmartRandomBot | AppOfficer / GoodCoder666 | 启用 | 最大兵力栈贪心基线 |
| ZlyBot | AppOfficer | 启用 | 单目标 BFS 启发式 |
| ZlyBot v2 | AppOfficer | 启用 | 带记忆的加权搜索 |
| ZlyBot v2.1 | AppOfficer | 启用 | 双焦点防守搜索 |
| SzlyBot | GoodCoder666 | 启用 | 地形加权 BFS 启发式 |
| GcBot | GoodCoder666 | 启用 | 自适应启发式 BFS |
| XiaruizeBot | xiaruize0911 | 启用 | 多源战略搜索 |
| KutuBot | pinkHC | 启用 | 统一战略目标规划 |
| oimBot | oimasterkafuu | 启用 | 基于 stance 的战略规划 |
| DummyBot / XrzBot / LyBot | 多位作者 | 状态不一 | 参考、禁用或实验性用途 |

## 如何参与贡献

- 阅读镜像整理后的 [Bot 贡献指南]({{< relref "docs/bot-contributions" >}})
- 查看 [内置 Bot 文档]({{< relref "docs/built-in-bots" >}}) 中的提交要求
- 如果你想做对战评测，可以继续阅读 [模拟器页面]({{< relref "simulator" >}})

## 项目对 Bot 的基本期待

- 代码清晰、可维护
- 策略有效，而不仅仅是随机占位
- 在长局中具有稳定性能
- 能提供回放、测试或基准结果作为依据

