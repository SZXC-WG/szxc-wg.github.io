---
title: "用模拟器评测 Bot"
description: "批量运行 Bot 对局，用胜率、OpenSkill 和延迟理解策略表现。"
weight: 50
doc_group: play
---

模拟器让你在不打开图形界面的情况下，连续运行多场 Bot 对战。它使用与桌面应用相同的核心棋盘和游戏逻辑，适合比较策略、检查性能，以及验证地图。

## 先运行一组对战

按[快速开始]({{< relref "docs/getting-started" >}})构建项目后，在 `build/Release` 中运行：

```bash
./LocalGen-bot-simulator --games 10 --bots XiaruizeBot GcBot
```

Windows PowerShell 中使用 `./LocalGen-bot-simulator.exe`。如果只需要重新构建模拟器，可在源码根目录运行：

```bash
cmake --build build --config Release --target LocalGen-bot-simulator
```

默认对局使用 20×20 随机地图，每局最多推进 1000 个半回合。程序会输出逐局结果，以及最终统计表。

## 常用示例

在独立生成的随机地图上运行十局，并显式设置时长：

```bash
./LocalGen-bot-simulator --games 10 --width 20 --height 20 --steps 1000 --bots XiaruizeBot GcBot
```

重复使用一张自定义地图。请把示例路径替换为自己的 `.lgmp`：

```bash
./LocalGen-bot-simulator --games 10 --map maps/arena01.lgmp --steps 1000 --bots XiaruizeBot GcBot
```

macOS 的随附地图位于应用包内。从 `build/Release` 运行时，示例路径应改为 `LocalGen-new.app/Contents/MacOS/maps/arena01.lgmp`；也可以使用自己地图的绝对路径。

运行多人混战，使用四个工作线程并记录 Bot 思考耗时：

```bash
./LocalGen-bot-simulator --games 100 --threads 4 --shuffle --latency --bots SmartRandomBot KtqBot "ZlyBot v2.1" GcBot
```

只保留最终统计表：

```bash
./LocalGen-bot-simulator --games 50 --silent --bots XiaruizeBot GcBot
```

## 参数参考

| 参数 | 含义 | 默认值 |
| --- | --- | --- |
| `--games N` | 独立对局数量 | `8` |
| `--width N` | 随机地图宽度 | `20` |
| `--height N` | 随机地图高度 | `20` |
| `--map PATH` | 使用指定 v6 `.lgmp` 地图 | 未设置 |
| `--threads N` | 工作线程数 | 自动选择，不超过对局数 |
| `--steps N` | 每局最多推进的半回合数 | `1000` |
| `--silent` | 只输出最终表格 | 关闭 |
| `--shuffle` | 随机调整 Bot 与玩家编号的映射 | 关闭 |
| `--latency` | 测量 `requestMove()` 平均延迟 | 关闭 |
| `--bots A B ...` | 两个或更多已注册 Bot 名称 | `XiaruizeBot GcBot` |
| `--help` / `-h` | 显示用法 | — |

数值参数应为正数。Bot 名称区分大小写，带空格的名称需要引号。`--map` 只接受 `.lgmp`，不接受旧版 `.lg` 或官方 JSON；指定地图后会忽略 `--width` 和 `--height`。地图需为所有参与者提供足够的出生点或零兵力空白平地。

## 理解执行过程

每个 Bot 都有独立队伍编号，因此模拟器运行自由混战。`--shuffle` 改变编号映射，不会创建盟友队伍。

独立对局会并行运行。未指定 `--threads` 时，程序根据 CPU 并发数自动选择线程数量，至少一个，最多等于比赛数。逐局结果按完成顺序输出；评分则按局号顺序汇总更新，不受完成先后影响。

## 读懂统计表

| 列 | 表示什么 |
| --- | --- |
| OpenSkill / OS 95% CI | 本次自由混战评分均值及其 95% 区间 |
| Wins / Win Rate / Win 95% CI | 胜场、胜率及胜率的 95% 区间 |
| Avg Rank | 平均最终排名，越小越靠前 |
| Avg Kill | 平均击杀数 |
| Survived | 结束时仍存活的对局数 |
| Avg Army / Avg Land | 结束时的平均兵力和领地 |
| Avg Latency | 启用 `--latency` 后，每次 `requestMove()` 的平均微秒数 |

表格先按 OpenSkill 均值排序，再按胜场排序。评分使用每局完整排名，胜率区间使用 Wilson 方法；OpenSkill 区间按 `mu ± 1.96 × sigma` 展示。

**达到半回合上限时，当前排名第一的 Bot 也会计为胜者，即使场上仍有多个存活 Bot。** 逐局日志会将这种情况写为 `leads at step limit`。因此，比较结果时请同时记录 `--steps`。

## 让评测更有参考价值

当前没有可指定的随机种子参数。重复使用同一张地图可以减少地形差异，但出生分配仍可能变化，无法保证每次运行完全复现。

比较策略时，尝试不同地图尺寸、地图类型、对手组合和玩家数量，运行足够多的比赛。区间能帮助理解样本的不确定性，但不能消除地图与对手选择的影响。发布结果时，请一并记录完整命令、源码版本、平台和 Release 构建信息。

模拟器目前输出文本日志与表格，不提供 CSV、回放或训练资产导出。更多实现说明可查看[模拟器源码与 README](https://github.com/SZXC-WG/LocalGen-new/tree/master/simulator)。
