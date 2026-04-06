---
title: "Contribute"
description: "Contribute the way the project docs expect: target the right branch, attach evidence for bots, and use disciplined commit messages."
date: 2026-04-06T17:54:16+08:00
draft: false
weight: 80
---

## How to contribute

If you can improve gameplay, bots, documentation, testing, or tooling, LocalGen has room for your contribution. The project openly welcomes help, especially through GitHub issues and pull requests.

The README makes one target explicit: if you are contributing new work for the active rewrite, submit it to **`master` / `v6.x`**.

## Main contribution paths

- **Gameplay and engine work** on the active `master` / `v6.x` line
- **Built-in bot contributions** through `src/bots/`
- **External bot experiments** through the evolving network-based bot model
- **Documentation improvements** across README and project guides
- **Bug reports and feature requests** through the issue tracker

## Recommended starting points

- [Bot contribution guide]({{< relref "docs/bot-contributions" >}})
- [Built-in bots guide]({{< relref "docs/built-in-bots" >}})
- [Commit regulations]({{< relref "docs/commit-regulations" >}})
- [Code of conduct]({{< relref "docs/code-of-conduct" >}})

## Commit language the project expects

The commit regulations document recommends small, reviewable, atomic commits and a conventional subject line such as:

- `feat(...)` for new features
- `upd(...)` for updates to existing behavior
- `fix(...)` for bug fixes
- `docs(...)`, `style(...)`, `refactor(...)`, `chore(...)`, `test(...)`, or `ci(...)` when those better describe the change

Subjects should stay short, imperative, and descriptive.

```text
feat(bot): add frontier pressure heuristic
fix(simulator): correct replay summary formatting
docs(website): clarify bilingual download guidance
```

## What maintainers will look for

- changes that stay focused and reviewable
- a clear explanation of what changed and why
- adherence to the documented commit-message conventions
- replays, tests, or benchmark notes when contributing bots or major gameplay work
- for external bots, dependency and runtime notes

## Ready to join in?

- [Issues](https://github.com/SZXC-WG/LocalGen-new/issues)
- [Pull requests](https://github.com/SZXC-WG/LocalGen-new/pulls)
- [Discussions](https://github.com/SZXC-WG/LocalGen-new/discussions)

