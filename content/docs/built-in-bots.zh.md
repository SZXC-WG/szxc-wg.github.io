---
title: "内置 Bot 文档"
description: "说明哪些 Bot 会直接编译进 LocalGen，以及提交新内置 Bot 的基本要求。"
date: 2026-04-06T17:55:08+08:00
draft: false
weight: 70
---

> 源文档：[`src/bots/README.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/src/bots/README.md)

## 概览

这一部分描述的是 **直接编译进 LocalGen 可执行文件** 的 Bot。

## 当前 Bot 概览

| Bot | 作者 | 是否启用 | 复杂度摘要 |
| --- | --- | --- | --- |
| DummyBot | AppOfficer | 否 | 示例型启发式贪心 Bot |
| SmartRandomBot | AppOfficer / GoodCoder666 | 是 | 最大兵力栈贪心 |
| XrzBot | xiaruize0911 | 否 | 聚焦型随机贪心 |
| ZlyBot | AppOfficer | 是 | 单目标 BFS 启发式 |
| ZlyBot v2 | AppOfficer | 是 | 带记忆的加权搜索 |
| ZlyBot v2.1 | AppOfficer | 是 | 双焦点防守搜索 |
| SzlyBot | GoodCoder666 | 是 | 地形加权 BFS 启发式 |
| GcBot | GoodCoder666 | 是 | 自适应启发式 BFS |
| XiaruizeBot | xiaruize0911 | 是 | 多源战略搜索 |
| KutuBot | pinkHC | 是 | 统一战略目标规划 |
| LyBot | pinkHC | 否 | 多人局目标规划 |
| oimBot | oimasterkafuu | 是 | 基于 stance 的战略规划 |

## 新内置 Bot 的要求

1. 必须使用与项目兼容的 C++ 编写。
2. 代码应限制在 C++17 特性范围内。
3. 实现应放在单个 `*.cpp` 文件中。
4. 该文件必须包含 `src/core/bot.h`。
5. Bot 类必须继承 `BasicBot` 并重写 `compute`。
6. 必须通过 `REGISTER_BOT` 完成注册。

## 提交清单

1. 将文件放入 `src/bots/`。
2. 使用清晰且不冲突的文件名。
3. 将该文件加入顶层 `CMakeLists.txt` 的源文件列表。
4. 提交 Pull Request。

