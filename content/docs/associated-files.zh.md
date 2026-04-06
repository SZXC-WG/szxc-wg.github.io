---
title: "关联文件"
description: "整理 LocalGen 地图、回放与配置文件格式的参考说明。"
date: 2026-04-06T17:55:08+08:00
draft: false
weight: 50
---

> 源文档：[`docs/associated-files.md`](https://github.com/SZXC-WG/LocalGen-new/blob/master/docs/associated-files.md)

## 文件格式参考

| 扩展名 / 文件名 | 文件类型 | 说明 |
| --- | --- | --- |
| `.lg` | 地图文件 | 适用于 LG v5 的旧地图文件，通常需要配套 ini 文件。 |
| `.lgmp` | 地图文件 | 适用于 LG v6 的原生地图格式，不再依赖配套 ini，可能采用 JSON 风格结构。 |
| `.lgr` | 回放文件 | 普通回放文件，存储的信息量大致接近 generals.io replay。 |
| `.lgra` | 高级回放文件 | 在 `.lgr` 基础上额外记录更多细节，例如每回合的移动队列等。 |
| `settings.lgsts` | 配置文件 | 适用于 LG v5 的设置文件，默认通常为隐藏状态。 |
| `config.lgs6` | 配置文件 | 适用于 LG v6 的配置文件，默认应隐藏，且大概率采用 JSON 格式。 |

这些文件格式对于玩家、地图作者、回放分析者以及工具开发者都很重要。

