---
title: "Naming conventions"
description: "Choose consistent, meaningful names for types, functions, and variables."
weight: 90
doc_group: develop
---

When adding a bot, UI behavior, or core logic, following the project's naming conventions helps other contributors read your code.

## Common rules

| Item | Convention | Example |
| --- | --- | --- |
| Namespace | Lowercase with underscores | `local_generals` |
| Class, struct, and most types | PascalCase | `GameConstantsPack` |
| Simple type alias | A word with the `_t` suffix is allowed | `index_t` |
| Enum type | Lowercase with underscores and an `_e` suffix | `tile_type_e` |
| Enum value | Uppercase with underscores | `TILE_CITY` |
| Function and variable | camelCase | `requestMove`, `playerId` |
| Constant | Uppercase with underscores | `MAX_VALUE` |
| Global macro | Uppercase with underscores | `GLOBAL_MACRO` |

## Express the meaning

Prefer local variable names that describe their role, such as `playerId` or `targetTile`. The project allows more flexibility in very small scopes, but still recommends avoiding single-letter names that carry little meaning.

Naming is also more flexible for local macros that are removed with `#undef` shortly after use. Keep them meaningful. When editing existing code, look at nearby names so your additions fit their context.

These conventions apply to Qt-based v6. See the original [naming guide](https://github.com/SZXC-WG/LocalGen-new/blob/master/docs/naming-method.md) for the source guidance.
