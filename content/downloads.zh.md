---
title: "下载"
description: "按 README 的原始引导来下载：以 GitHub Releases 为准，普通玩家优先稳定版，同时谨慎看待仍在进行中的 v6 主线。"
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 20
---

## 官方下载入口

上游 README 直接把用户引导到 GitHub Releases，因此这里仍然是获取 LocalGen 构建产物的标准入口：

- [打开 LocalGen GitHub Releases](https://github.com/SZXC-WG/LocalGen-new/releases)

本网站的 [版本发布页面]({{< relref "releases" >}}) 会整理版本时间线，并链接回对应的 GitHub 下载页。

## 你看到的是哪条分支？

README 里还有一个非常重要的提醒：**`master` 分支对应的是正在推进中的 v6 重构，不等同于已经完成的最终用户发布版**。

- 如果你只是想下载一个更稳妥的版本，请优先从 **GitHub Releases** 开始。
- 如果你想跟进未来的 Qt 方向，则需要关注 **`master` / `v6.x`**，并接受它仍在开发中的事实。

## 稳定版与预览版怎么选？

### 对大多数玩家

如果你想获得更稳妥的体验，请优先从 **GitHub 上最新稳定版** 开始。

### 对测试者和贡献者

如果你希望尽早体验新功能，可以使用预览版或开发版，例如：

- 最新 Bot 和玩法改动
- 新的地图、回放或工具行为
- UI 与平台相关的早期更新

## 版本线说明

- **v6 / `master`** —— 正在进行中的 Qt 重构主线，也是项目未来方向
- **v5.x** —— 支撑许多历史构建和旧版稳定下载的维护分支

## 平台说明

- 新一代开发工作正在面向 **基于 Qt 的跨平台支持**。
- 较早期的很多版本主要在 **Windows 环境** 中构建。
- 某些历史版本在发布说明中明确建议：若要在 Linux 或 macOS 上运行 Windows 版本，可尝试 **Wine**。

## 启动旧版本前请注意

多个历史版本提到需要安装随包附带的字体，例如 **Quicksand** 或 **Freestyle Script**。如果发布说明要求安装字体，请先完成这一步再启动游戏。

## 下载前还想了解更多？

- 查看 [版本历史]({{< relref "releases" >}})
- 阅读 [常见问题]({{< relref "faq" >}})
- 访问 [源码仓库](https://github.com/SZXC-WG/LocalGen-new)

