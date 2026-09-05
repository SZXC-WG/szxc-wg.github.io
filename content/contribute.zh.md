---
title: "参与贡献"
description: "从一个问题、一张地图或一段代码开始，一起让 LocalGen 更好用。"
draft: false
weight: 80
---

欢迎参与 LocalGen。你不必先熟悉整套代码：指出一处不清楚的文档、写下一个能复现的问题，或分享一张有趣的地图，都是很好的开始。

## 找到适合自己的入口

- **发现了问题：** 在 [Issues](https://github.com/SZXC-WG/LocalGen-new/issues)描述版本、系统、操作步骤，以及实际发生的情况。能提供截图、报错或相关地图会更有帮助。
- **有一个新想法：** 先说明你想解决什么问题、希望怎样使用它。较大的功能适合先讨论设计和范围。
- **喜欢地图和文字：** 改进地图、补充示例、修正文档和翻译，让下一个使用者少走一点弯路。
- **想写代码：** 界面、游戏逻辑、Bot、模拟器、性能、构建和打包都欢迎改进。

## 准备开发环境

新功能与日常修复以 `master` 分支的 v6 为主。v1–v4 已停止维护，v5 只接收安全问题与严重错误修复。

当前构建需要 **C++20、Qt 6.7+、CMake 3.19+ 和 Ninja 1.10+**。按照[安装与构建指南]({{< relref "docs/getting-started" >}})配置环境后，分别构建 Debug 与 Release：

```bash
cmake -B build -S . -G "Ninja Multi-Config" -DCMAKE_TOOLCHAIN_FILE=/path/to/qt.toolchain.cmake
cmake --build build --config Debug
cmake --build build --config Release
```

请把工具链路径换成实际的 Qt 安装路径。Debug 适合定位问题，Release 适合测量运行表现。

## 提交一个容易审阅的改动

让一次 Pull Request 围绕一个清楚的目的展开，说明问题是什么、改动后会怎样，以及你如何验证。涉及界面可以附截图；涉及 Bot 可以附模拟器命令和结果；行为、文件格式或依赖有变化时，也请更新对应文档。

代码风格请参考[命名约定]({{< relref "docs/naming-method" >}})，提交信息请参考[提交规范]({{< relref "docs/commit-regulations" >}})。例如：

```text
fix(ui): preserve map selection when changing player count
```

## 贡献自己的 Bot

当前项目接收随应用编译的 C++ Bot。除了可编译的实现，请简要介绍算法，并提供不同地图、玩家数量下的评测结果，说明每步耗时和长局中的稳定性。

[Bot 贡献指南]({{< relref "docs/bot-contributions" >}})介绍接入步骤，[模拟器文档]({{< relref "docs/simulator-guide" >}})帮助你准备评测。当前接口以源码中的 `BasicBot`、`BotRegistrar` 和 `CMakeLists.txt` 为准。

## 一起保持友好的讨论

欢迎不同经验和背景的贡献者。请关注问题本身，尊重彼此，给出具体、有帮助的反馈。参与前可以阅读[行为准则]({{< relref "docs/code-of-conduct" >}})和仓库中的 [CONTRIBUTING.md](https://github.com/SZXC-WG/LocalGen-new/blob/master/CONTRIBUTING.md)。
