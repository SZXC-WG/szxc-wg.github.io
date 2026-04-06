---
title: "模拟器指南"
description: "说明如何使用 LocalGen Bot 模拟器进行可重复、支持多线程的 Bot 对战实验。"
date: 2026-04-06T17:55:08+08:00
draft: false
weight: 60
---

> 源文档：[`simulator/README.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/simulator/README.md)

## 概览

`LocalGen-bot-simulator` 是一个轻量级命令行工具，用于评估不同 Bot 之间的对战表现。

## 主要能力

- 使用共享核心引擎生成随机地图
- 通过统一的 BotFactory 实例化已注册 Bot
- 在不启动 Qt 界面的情况下重复运行对局
- 输出综合统计结果，也可选逐局结果

## 示例命令

- `./LocalGen-bot-simulator --games 10 --width 20 --height 20 --steps 600 --bots XiaruizeBot GcBot`
- `./LocalGen-bot-simulator --games 10 --map maps/arena01.lgmp --steps 600 --bots XiaruizeBot GcBot`
- `./LocalGen-bot-simulator --games 50 --silent --bots XiaruizeBot GcBot`

## 自定义地图

- `--map PATH` 会在每一局模拟中加载同一张地图
- 该参数只支持 v6 的 `.lgmp` 地图
- 指定 `--map` 后，`--width` 和 `--height` 会被忽略

## 说明

- 模拟器与主程序共享同一套棋盘和游戏核心逻辑
- 多场独立对局可以跨 CPU 线程并行执行
- `--silent` 会隐藏启动信息和逐局日志，仅保留最终汇总
- 汇总表中包含 FFA TrueSkill 评分与置信区间

