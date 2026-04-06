---
title: "机器人"
description: "按照项目文档原本的说法来理解 LocalGen Bot：内置与外部的区别、投稿规则，以及性能上的基本要求。"
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 60
---

## Bot 生态概览

Bot 是 LocalGen 最迷人的部分之一。它既能让普通离线对局更耐玩，也能把整个项目变成一个真正适合 AI / 策略研究的试验场。更重要的是，项目文档明确欢迎新的 Bot 贡献。

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

| Bot | 启用状态 | 复杂度 | 近似单回合复杂度 | 简介 |
| --- | --- | --- | --- | --- |
| DummyBot | 否 | Low | $O(n)$ | 示例型启发式贪心 |
| SmartRandomBot | 是 | Low | $O(n)$ | 最大兵力栈贪心基线 |
| XrzBot | 否 | Low | $O(n)$ | 聚焦型随机贪心 |
| ZlyBot | 是 | Medium | $O(n)$ | 单目标 BFS 启发式 |
| ZlyBot v2 | 是 | Medium | $O(n \log n)$ | 带记忆的加权搜索 |
| ZlyBot v2.1 | 是 | Medium | $O(n \log n)$ | 双焦点防守搜索 |
| SzlyBot | 是 | Medium | $O(n)$ | 地形加权 BFS 启发式 |
| GcBot | 是 | Medium | $O(n)$ | 自适应启发式 BFS |
| XiaruizeBot | 是 | High | $O(kn^2)$ | 多源战略搜索 |
| KutuBot | 是 | High | $O(n \log n)$ | 统一战略目标规划 |
| LyBot | 否 | High | $O(n^2)$ | 多人局目标规划 |
| oimBot | 是 | High | $O(n^3)$ | 基于 stance 的战略规划 |

## 如何读复杂度这一列？

可以把 $n$ 理解为 Bot 在某一回合里实际考察的相关格子数，把 $k$ 理解为它同时保留的前线候选或战略分支数。

$$
T_{\text{match}} \approx \sum_{t=1}^{s} T_{\text{bot}}(n_t)
$$

这也是为什么从 $O(n)$ 提升到 $O(n \log n)$ 看起来只是“小变化”，但在长时间、大批量模拟时会被不断累计出来。

```text
src/bots/MyBot.cpp
├─ 包含 src/core/bot.h
├─ 继承 BasicBot
├─ 实现 init(...)
├─ 实现 requestMove(...)
├─ 按文档要求注册 Bot
└─ 把源文件加入 PROJECT_SOURCES
```

## 内置 Bot 投稿检查清单

上游内置 Bot README 对 `src/bots/` 中的实现有一组非常明确的要求：

1. 代码必须兼容 **C++17**。
2. 整个 Bot 实现需要放在 **单个 `*.cpp` 文件** 中。
3. 该文件需要包含 `src/core/bot.h`。
4. Bot 类需要继承 `BasicBot` 并重写 `compute`。
5. 必须通过 `REGISTER_BOT` 宏完成注册。
6. 源文件还需要被加入顶层 `CMakeLists.txt` 的 `PROJECT_SOURCES`。

## 一个更完整、更有说服力的 Bot 投稿通常还会包含

- 测试、回放或基准结果
- 对性能与内存行为的简要说明
- 足够清晰的策略深度，而不是占位型随机 Bot
- 如果是外部 Bot，还需要提供依赖、启动方式以及支持的平台信息

## 想做出更聪明的 Bot？

- 阅读镜像整理后的 [Bot 贡献指南]({{< relref "docs/bot-contributions" >}})
- 查看 [内置 Bot 文档]({{< relref "docs/built-in-bots" >}}) 中的精确提交要求
- 如果你想做大量对战评测，可以继续阅读 [模拟器页面]({{< relref "simulator" >}})

