---
title: "Bot 贡献指南"
description: "说明 LocalGen v6 如何欢迎内置 Bot 与外部 Bot 的开发贡献。"
date: 2026-04-06T17:55:07+08:00
draft: false
weight: 20
---

> 源文档：[`docs/bot-contributions.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/docs/bot-contributions.md)

## 引言

Bot 一直是 LocalGen 的核心部分。但在项目早期版本中，Bot 开发的门槛较高：

- 只能使用 C++ 编写
- 必须和主程序一起编译
- 接口基本写死在源码中

v6 的目标之一，就是打破这些限制，让更多贡献者能够参与进来。

## v6 中的 Bot 类型

### 内置 Bot

- 源码位于 `src/bots/`
- 与 LocalGen 主程序一起编译
- 使用 C++ 编写
- 在 Local Game 和 Web Game 中可以直接使用

### 外部 Bot

- 作为独立可执行文件存在
- 可以用任意语言实现
- 通过网络协议与 LocalGen 通信
- 在纳入外部 Bot 列表后，可由游戏进程托管启动

## 你可以如何贡献

项目欢迎以下贡献：

- 全新的 Bot
- 对现有 Bot 的改进
- Bug 修复与性能优化

### 贡献内置 Bot

1. 阅读 [`src/bots/README.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/src/bots/README.md)。
2. 遵循项目的 C++ 风格规范。
3. 提交 Pull Request，并附带：
	- 测试或回放材料
	- 简要性能说明

### 贡献外部 Bot

1. 实现约定好的通信协议。
2. 提供可运行的二进制文件或可靠构建脚本。
3. 在 PR 中写清楚：
	- 依赖与启动方式
	- 支持的操作系统与运行环境
	- 预期性能表现

## 社区对 Bot 的基本要求

- 代码清晰，并具备必要文档
- 在不同地图和玩家数量下进行测试
- 不接受纯随机占位型 Bot
- 单回合开销应保持在引擎可接受范围内
- 长局运行中应尽量稳定，不出现明显内存泄漏

