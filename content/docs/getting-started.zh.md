---
title: "快速开始"
description: "下载 LocalGen，开启第一局离线对战；想参与开发时，再从源码构建。"
weight: 10
doc_group: start
---

想先玩一局，你只需要下载适合自己系统的发布包。Qt、CMake 和编译器是源码构建时才需要准备的工具。

## 下载并运行

1. 打开 [GitHub Releases](https://github.com/SZXC-WG/LocalGen-new/releases)，阅读所选版本的说明，下载对应系统的文件。
2. 按发布包的说明解压或安装。使用便携包时，请保留完整目录，尤其是随附的 `maps/`、`fonts/` 和运行库。
3. 启动 LocalGen，在主菜单选择 **Local Game**。保留 `Standard` 地图、20×20 尺寸和速度 1，让 P1 使用 `Human`，再选择一个 Bot，就可以开始。

接下来读[开始第一局]({{< relref "docs/local-game" >}})，了解如何移动兵力和调整视角。

本文其余部分面向想从源码构建 Qt 版 v6 的用户。文档依据 `6.0.0-dev`，发行包的功能请以该版本说明为准。

## 准备构建环境 {#build}

| 工具 | 要求 |
| --- | --- |
| Qt | 6.7 或更新版本，包含 Widgets、SVG、Network、Charts |
| CMake | 3.19 或更新版本 |
| Ninja | 1.10 或更新版本 |
| C++ 编译器 | 支持 C++20，并与所选 Qt 工具链匹配 |

确保 `cmake`、`ninja` 和编译工具能在终端中找到。下载或克隆[项目源码](https://github.com/SZXC-WG/LocalGen-new)，然后找到 Qt 工具链文件，通常位于：

```text
$QT_ROOT_DIR/lib/cmake/Qt6/qt.toolchain.cmake
```

## 配置与构建

在源码根目录运行下面两条命令，把示例路径替换为你的实际 Qt 工具链路径：

```bash
cmake -B build -S . -G "Ninja Multi-Config" -DCMAKE_TOOLCHAIN_FILE=/path/to/qt.toolchain.cmake
cmake --build build --config Release
```

排查问题时可以改用 `--config Debug`。准备提交代码时，请检查 Debug 和 Release 两种配置；比较 Bot 性能时使用 Release。

常规构建会生成两个程序：

| 程序 | 用途 |
| --- | --- |
| `LocalGen-new` | 桌面应用，用于本地对局和地图编辑 |
| `LocalGen-bot-simulator` | 命令行工具，用于批量评测内置 Bot |

## 找到构建结果

使用上面的构建命令时，Release 程序位于：

```text
Windows: build\Release\LocalGen-new.exe
Linux:   build/Release/LocalGen-new
macOS:   build/Release/LocalGen-new.app
```

构建会将 `maps/` 和 `fonts/` 复制到桌面可执行文件旁。macOS 上，这里的可执行文件位于 `.app/Contents/MacOS/` 内。应用从该位置查找地图，并加载三份随附的 Quicksand 字体；遇到字体缺失提示时，先检查这些文件是否完整。

想确认模拟器也可运行，可以在 `build/Release` 中执行：

```bash
./LocalGen-bot-simulator --games 8 --bots XiaruizeBot GcBot
```

Windows PowerShell 中请使用 `./LocalGen-bot-simulator.exe`。更多参数见[模拟器指南]({{< relref "docs/simulator-guide" >}})。

## 打包与启动问题

- **Windows：** 制作便携包时，在构建完成后使用 Qt 的 `windeployqt` 部署运行库，并保留地图和字体目录。
- **macOS：** 项目提供打包脚本：`bash scripts/package-macos-dmg.sh build/Release/LocalGen-new.app LocalGen-new.dmg`。脚本处理框架部署、包内容清理和临时签名。项目 README 提醒避免直接使用 `macdeployqt ... -dmg`，以免生成签名无效的应用副本。
- **Linux：** 在 Debian/Ubuntu 上，如果 AppImage 因缺少 OpenGL 运行时而无法启动，可安装 `libopengl0`：`sudo apt install libopengl0`。

v6 的 **Web Game** 和 **Load Replay** 按钮目前会显示尚未实现的提示。本地对局与地图编辑器已经可以使用。
