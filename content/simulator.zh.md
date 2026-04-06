---
title: "模拟器"
description: "使用 LocalGen Bot 模拟器，在不启动 Qt 界面的情况下，对随机地图或自定义地图上的 Bot 对战进行可重复实验。"
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 70
---

## 模拟器的作用

`LocalGen-bot-simulator` 是一个轻量级命令行工具，主要用于 **Bot 对 Bot 的评估与对比**。

它与主程序共用相同的棋盘 / 游戏核心逻辑，但去掉了 Qt 图形界面，因此更适合做基准测试、回归验证以及大规模自动化对局。

## 它可以做什么

- 生成随机地图
- 加载自定义 `.lgmp` 地图
- 通过共享的 Bot 注册系统实例化机器人
- 并行运行多场对局
- 输出胜率统计与类似 TrueSkill 的综合结果

## 为什么贡献者会用它

Bot 贡献文档反复强调需要提供证据，例如回放、测试记录和性能说明。想在统一条件下比较多种策略时，模拟器就是收集这些证据最干净的工具。

## 示例命令

```bash
./LocalGen-bot-simulator --games 10 --width 20 --height 20 --steps 600 --bots XiaruizeBot GcBot
./LocalGen-bot-simulator --games 10 --map maps/arena01.lgmp --steps 600 --bots XiaruizeBot GcBot
./LocalGen-bot-simulator --games 50 --silent --bots XiaruizeBot GcBot
```

## 一个简单的实验公式

如果你只是想先看两种 Bot 的表现差异，最直观的指标依然是胜率：

$$
	ext{win-rate} = \frac{W}{W + L} \times 100\%
$$

在地图规模固定时，一组模拟的大致时间预算可以写成：

$$
T_{\text{suite}} \approx G \times S \times T_{\text{turn}}(n)
$$

其中 $G$ 表示总对局数，$S$ 表示步数上限，而 $T_{\text{turn}}(n)$ 表示有效棋盘规模为 $n$ 时的平均单回合开销。

## 使用说明

- `--map` 会在每一局中加载同一张自定义地图
- 该参数目前只支持 v6 的 `.lgmp` 地图
- 独立比赛可以跨 CPU 线程并行执行
- `--silent` 会关闭横幅和逐局日志，只保留最终汇总表

更多细节请阅读镜像整理后的 [模拟器指南]({{< relref "docs/simulator-guide" >}})。

