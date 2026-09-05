---
title: "Write clear commits"
description: "Explain what changed and why, so reviewing and revisiting your work is easier."
weight: 80
doc_group: develop
---

A good commit message helps someone understand a change without having followed the discussion. LocalGen uses a short subject with a type prefix. Add a body and related issue references when more context is useful.

## Basic format

```text
<type>(<scope>): <subject>

<body>

<footer>
```

The `scope` is optional, such as `ui`, `core`, or `bots`. Keep the subject under 72 characters and use an imperative verb to describe the change. Explain why and how in the body, wrapping lines at 72 characters. The footer can link an issue with `Closes #42` or describe an incompatible change with `BREAKING CHANGE:`.

## Choose a type

| Type | Use it for |
| --- | --- |
| `feat` | New features |
| `upd` | Updates to existing features |
| `fix` | Bug fixes |
| `docs` | Documentation |
| `style` | Formatting or style changes |
| `refactor` | Internal restructuring without behavior changes |
| `chore` | Build, dependency, or maintenance work |
| `test` | New or updated tests |
| `ci` | Continuous integration |

## Be specific

Start the subject with a verb such as `add`, `fix`, `remove`, or `update`. Use lowercase except for proper nouns and acronyms. For example:

```text
fix(core): handle maps with too few spawn tiles

Explain why the previous behavior failed and how this change handles it.

Closes #42
```

The issue number here is an example; use a relevant issue in your actual commit. Avoid subjects such as `fix stuff` or `changes made` that do not identify the change.

## Keep changes easy to review

Aim for one related change per commit, with a result that can be checked or reverted independently. Break large features into clear steps and commit as you go. Before merging, combine fragments that belong together.

Use rebase or squash as appropriate for the collaboration to keep the final history understandable. Current v6 development targets `master`; choose a destination that matches the version you are working on.

See the project's [commit conventions](https://github.com/SZXC-WG/LocalGen-new/blob/master/docs/commit-regulations.md) for the full guidance.
