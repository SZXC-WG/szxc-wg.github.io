# LocalGen project website

The project overview, downloads, and English/Chinese documentation for **LocalGen**, built with **Hugo** and deployed to [GitHub Pages](https://szxc-wg.github.io/) through **GitHub Actions**.

The guides cover [LocalGen v6](https://github.com/SZXC-WG/LocalGen-new) and were checked against source commit `34b2a5c`. Feature descriptions follow the implementation; check each release's notes for differences in packaged builds.

## Local preview

Install **Hugo Extended 0.165.0**. GitHub Actions is pinned to the same version as the current local installation.

```sh
hugo server
```

Open the address printed in your terminal. The English homepage is at `/`, and the Chinese homepage is at `/zh/`. The language switch opens the translation of the current page.

## Build and validate

```sh
hugo build --gc --minify --panicOnWarning --printI18nWarnings --printPathWarnings
python scripts/check_site.py public
```

Generated files go into `public/` and should not be committed. The checker uses only the Python standard library and runs without network access. It checks internal links, anchors, local assets, duplicate IDs, and reciprocal English/Chinese translations. Visual layout and interactions still need browser review.

## Project structure

| Location | Purpose |
| --- | --- |
| `content/` | Homepage, downloads, bots, simulator, about, and community pages |
| `content/docs/` | User and developer guides, with matching `.en.md` and `.zh.md` files |
| `layouts/` | Hugo page templates and shared components |
| `assets/css/main.css` | Themes, responsive layouts, article typography, and print styles |
| `assets/js/site.js` | Theme switching, mobile navigation, the docs menu, and code copying |
| `i18n/` | English and Chinese interface text |
| `data/` | Project, release, contributor, and bot snapshots |
| `static/` | Icons and local fonts, including the font license |

## Writing documentation

Organize guides around what readers want to do. Add both language versions under the same base filename, with front matter such as:

```yaml
---
title: "Your guide title"
description: "Explain what this guide helps the reader accomplish."
doc_group: play
weight: 35
---
```

Use one of these `doc_group` values:

- `start`: getting started.
- `play`: playing and exploring the tools.
- `develop`: contributing to the project.

The `weight` sets the order within each group and the previous/next navigation. Keep weights increasing across the three groups.

Use Hugo's `relref` for internal links so the build can catch missing targets. Give frequently linked headings an explicit ID, such as `## Prepare a build environment {#build}`, to keep their anchors stable when titles change.

Write clear, friendly instructions. Start with the steps readers need, then explain parameters, behavior, and limitations. Describe unfinished features as unfinished.

## Refreshing project data

Normal builds use committed snapshots and do not call the GitHub API. To refresh them:

```sh
python scripts/sync_localgen.py
```

The script updates GitHub release and contributor metadata while preserving manually checked facts about the project version, toolchain, maps, and bots. It changes files and timestamps only when the underlying data changes.

For authenticated requests, set `GITHUB_TOKEN` or `GH_TOKEN` in your terminal's environment. The script does not load `.env` automatically. Keep tokens out of the repository.

The downloads page selects the release GitHub marks as latest and creates platform and architecture links from its actual assets. Preview labels check both GitHub's prerelease flag and version markers such as alpha, beta, rc, preview, and dev.

## Deployment with GitHub Actions

In the repository settings, select **Settings → Pages → Source → GitHub Actions**.

- `hugo.yaml` builds and validates pull requests targeting `main`. Pushes to `main` and manual runs on `main` also deploy the validated site to GitHub Pages.
- `sync-localgen-data.yaml` refreshes metadata every Monday at 03:00 UTC, or on demand. When data changes, it commits to `main` and explicitly triggers deployment. Unchanged data produces no commit.
- The sync workflow uses the repository's `GITHUB_TOKEN` with `contents: write` and `actions: write`. If branch protection prevents direct bot pushes, adapt the update process to the repository's policy.

The site uses `https://szxc-wg.github.io/`. If the domain or deployment subpath changes, update `baseURL` in `config/_default/hugo.toml` and pass the same URL to the checker through `--base-url`.

## Licensing

This website repository does not currently declare a repository-wide license. The LocalGen application source uses GPL-3.0-or-later, and the bundled Quicksand fonts use SIL OFL 1.1. These licenses do not automatically cover all website content. See the website's license page and individual resource notices.
