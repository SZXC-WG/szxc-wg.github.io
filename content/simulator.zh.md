---
title: "模拟器"
description: "使用 LocalGen Bot 模拟器，在不启动 Qt 界面的情况下进行可重复的 Bot 对战评估。"
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 70
---

## 模拟器的作用

`LocalGen-bot-simulator` 是一个轻量级命令行工具，主要用于 **Bot 对 Bot 的评估与对比**。

它与主程序共用相同的棋盘 / 游戏核心逻辑，但去掉了 Qt 图形界面，因此更适合做基准测试和自动化对局。

## 它可以做什么

- 生成随机地图
- 加载自定义 `.lgmp` 地图
- 通过共享的 Bot 注册系统实例化机器人
- 并行运行多场对局
- 输出胜率统计与类似 TrueSkill 的综合结果

## 示例命令

- `./LocalGen-bot-simulator --games 10 --width 20 --height 20 --steps 600 --bots XiaruizeBot GcBot`
- `./LocalGen-bot-simulator --games 10 --map maps/arena01.lgmp --steps 600 --bots XiaruizeBot GcBot`
- `./LocalGen-bot-simulator --games 50 --silent --bots XiaruizeBot GcBot`

## 使用说明

- `--map` 会在每一局中加载同一张自定义地图
- 该参数目前只支持 v6 的 `.lgmp` 地图
- 独立比赛可以跨 CPU 线程并行执行
- `--silent` 会关闭横幅和逐局日志，只保留最终汇总表

更多细节请阅读镜像整理后的 [模拟器指南]({{< relref "docs/simulator-guide" >}})。

