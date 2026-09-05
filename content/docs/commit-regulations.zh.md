---
title: "写好提交信息"
description: "用简洁的提交说明记录改了什么、为什么改，让审查和回溯更轻松。"
weight: 80
doc_group: develop
---

好的提交信息，让没有参与讨论的人也能理解这次改动。LocalGen 使用带类型的简短主题；需要更多背景时，再补充正文和相关 Issue。

## 基本格式

```text
<type>(<scope>): <subject>

<body>

<footer>
```

`scope` 是可选的，例如 `ui`、`core` 或 `bots`。主题保持在 72 个字符以内，用命令式动词说明具体变化。正文解释原因与做法，每行控制在 72 个字符以内。页脚可以关联 Issue，例如 `Closes #42`，或用 `BREAKING CHANGE:` 说明不兼容变更。

## 选择合适的类型

| 类型 | 适用改动 |
| --- | --- |
| `feat` | 新功能 |
| `upd` | 更新已有功能 |
| `fix` | 修复问题 |
| `docs` | 文档 |
| `style` | 格式或样式调整 |
| `refactor` | 不改变功能的内部重构 |
| `chore` | 构建、依赖或维护工作 |
| `test` | 添加或调整测试 |
| `ci` | 持续集成 |

## 写得具体一点

主题以 `add`、`fix`、`remove`、`update` 等动词开头，除专有名词和缩写外使用小写。例如：

```text
fix(core): handle maps with too few spawn tiles

Explain why the previous behavior failed and how this change handles it.

Closes #42
```

这里的 Issue 编号仅为示例，实际提交时使用相关编号。避免 `fix stuff` 或 `changes made` 这类无法说明内容的主题。

## 让每次提交容易审查

尽量让一个提交只完成一件相关的事，并且能够独立检查或回退。大功能可以分成几个清晰的步骤持续提交，无需等到全部完成；合并前再整理可以归为一体的碎片提交。

根据协作需要进行 rebase 或 squash，让最终历史保持清楚。当前 v6 开发面向 `master`，提交目标应与所参与版本保持一致。

完整约定见项目的[提交规范](https://github.com/SZXC-WG/LocalGen-new/blob/master/docs/commit-regulations.md)。
