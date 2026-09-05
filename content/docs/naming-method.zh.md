---
title: "代码命名约定"
description: "为类型、函数和变量选择一致、易懂的名字。"
weight: 90
doc_group: develop
---

给 Bot、界面或核心逻辑添加代码时，沿用下面的命名约定，可以让新的实现更容易被其他贡献者读懂。

## 常用规则

| 对象 | 约定 | 示例 |
| --- | --- | --- |
| 命名空间 | 小写，以下划线分词 | `local_generals` |
| 类、结构体和大多数类型 | PascalCase（大驼峰） | `GameConstantsPack` |
| 简单类型别名 | 可以用单词加 `_t` | `index_t` |
| 枚举类型 | 小写加下划线，以 `_e` 结尾 | `tile_type_e` |
| 枚举值 | 大写加下划线 | `TILE_CITY` |
| 函数和变量 | camelCase（小驼峰） | `requestMove`、`playerId` |
| 常量 | 大写加下划线 | `MAX_VALUE` |
| 全局宏 | 大写加下划线 | `GLOBAL_MACRO` |

## 优先表达含义

局部变量也尽量使用能说明用途的名称，例如 `playerId`、`targetTile`。作用范围很小时，项目允许较灵活的命名，但仍应避免没有描述性的单字母名称。

对于定义后很快用 `#undef` 清除的局部宏，规则相对宽松，同样应保持名字有意义。修改已有代码时，也请观察附近的命名方式，让改动融入上下文。

这些约定面向 Qt 版 v6。原始说明见项目的[代码命名规范](https://github.com/SZXC-WG/LocalGen-new/blob/master/docs/naming-method.md)。
