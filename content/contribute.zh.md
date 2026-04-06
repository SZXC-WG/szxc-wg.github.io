---
title: "参与贡献"
description: "按项目文档期望的方式参与协作：选对分支、为 Bot 附带证据，并使用规范的提交信息。"
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 80
---

## 如何参与贡献

LocalGen 明确欢迎社区通过 GitHub issue 和 pull request 参与项目建设。

README 里有一个很清楚的指向：如果你是在为当前重构主线提交新工作，请把目标分支放在 **`master` / `v6.x`**。

## 主要贡献路径

- 在活跃的 `master` / `v6.x` 主线上进行 **玩法与引擎开发**
- 通过 `src/bots/` 参与 **内置 Bot** 开发
- 基于网络接口探索 **外部 Bot**
- 完善 README 与指南等 **项目文档**
- 通过 issue 提交 **Bug 报告与功能建议**

## 推荐先阅读的内容

- [Bot 贡献指南]({{< relref "docs/bot-contributions" >}})
- [内置 Bot 文档]({{< relref "docs/built-in-bots" >}})
- [提交规范]({{< relref "docs/commit-regulations" >}})
- [行为准则]({{< relref "docs/code-of-conduct" >}})

## 项目希望看到的提交语言

提交规范文档建议把改动拆成小而清晰、便于审查和回滚的提交，并使用类似下面这样的前缀：

- `feat(...)` 表示新增功能
- `upd(...)` 表示更新已有行为
- `fix(...)` 表示修复问题
- `docs(...)`、`style(...)`、`refactor(...)`、`chore(...)`、`test(...)`、`ci(...)` 则用于其他更准确的类别

主题行需要简短、命令式，并且能准确说明改动内容。

```text
feat(bot): add frontier pressure heuristic
fix(simulator): correct replay summary formatting
docs(website): clarify bilingual download guidance
```

## 维护者通常会关注什么？

- 改动是否聚焦、便于审查
- 是否清楚说明改了什么、为什么这样改
- 是否遵循文档中的提交信息约定
- 对 Bot 或较大玩法改动，是否附带回放、测试或基准结果
- 如果是外部 Bot，是否写清楚依赖与运行环境

## 参与入口

- [Issues](https://github.com/SZXC-WG/LocalGen-new/issues)
- [Pull Requests](https://github.com/SZXC-WG/LocalGen-new/pulls)
- [Discussions](https://github.com/SZXC-WG/LocalGen-new/discussions)

