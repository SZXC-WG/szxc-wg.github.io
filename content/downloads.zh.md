---
title: "下载 LocalGen"
description: "找到适合你电脑的版本，开始第一局本地对战。"
draft: false
layout: downloads
weight: 20
---

LocalGen 的发布说明与下载附件都在 [GitHub Releases](https://github.com/SZXC-WG/LocalGen-new/releases)。先选择一个版本，再在 **Assets** 中找到与你的系统和处理器相符的文件。

**想体验本文档介绍的功能，请留意版本号。** 本站面向 v6 开发分支，旧版程序的界面和文件格式可能不同。带有 `-dev` 或标记为预发布的版本仍在开发中。你也可以先看本站的[版本记录]({{< relref "releases" >}})。

## 选择适合电脑的文件

| 系统 | 处理器 | 文件类型 |
| --- | --- | --- |
| Windows | 常见 Intel / AMD 电脑选 x86_64；ARM 电脑选 ARM64 | `.zip` |
| macOS | Intel 芯片选 x86_64；Apple 芯片选 ARM64 | `.dmg` |
| Linux | 按系统架构选择 x86_64 或 ARM64 | `.AppImage` |

这些是当前持续集成的打包目标，**并非每个发布版本都会附带全部文件**。Windows 构建还可能区分 MSVC、MinGW 和 LLVM-MinGW，请结合附件名称及发布说明选择。

如果只是想运行游戏，请选择程序附件；GitHub 自动提供的 **Source code** 压缩包需要自行编译。

## 下载后怎么打开

- **Windows：** 完整解压 ZIP，再运行 `LocalGen-new.exe`。保留同一目录中的依赖文件，以及 `maps/`、`fonts/` 文件夹。
- **macOS：** 打开 DMG，按其中的布局将应用复制到电脑，再启动应用。
- **Linux：** 为 AppImage 添加执行权限，再运行它。若 Debian 或 Ubuntu 提示缺少 OpenGL 运行库，可安装 `libopengl0`。

启动 v6 后，选择 **Local Game** 就能配置一局离线对战。[第一次游玩]({{< relref "docs/local-game" >}})会带你认识地图、玩家和游戏操作。

## 使用开发构建

源码的 [Qt Build 工作流](https://github.com/SZXC-WG/LocalGen-new/actions/workflows/qt-build.yml)会构建开发分支，并在成功的运行中上传打包产物。它们反映对应提交的开发进度，与正式发布分开管理。

如果需要自行构建，准备支持 C++20 的编译器、Qt 6.7+、CMake 3.19+ 与 Ninja 1.10+，然后按照[安装与构建指南]({{< relref "docs/getting-started" >}})操作。**Bot 模拟器也建议从源码构建**：当前 CI 的桌面程序包没有包含模拟器可执行文件。

遇到启动或版本问题，可以先读[常见问题]({{< relref "faq" >}})，再带上系统信息、版本号和错误内容到 [GitHub Issues](https://github.com/SZXC-WG/LocalGen-new/issues)反馈。
