#!/usr/bin/env python3
"""Refresh GitHub metadata while preserving reviewed project facts and stable files."""
from __future__ import annotations

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

OWNER = "SZXC-WG"
REPO = "LocalGen-new"
API_ROOT = f"https://api.github.com/repos/{OWNER}/{REPO}"
SITE_ROOT = Path(__file__).resolve().parents[1]
TOKEN = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")


def fetch_json(url: str, params: dict[str, Any] | None = None, *, allow_404: bool = False) -> Any:
    if params:
        url = f"{url}?{urlencode(params)}"
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "LocalGen-website-sync/2.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    try:
        with urlopen(Request(url, headers=headers), timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        if allow_404 and exc.code == 404:
            return None
        raise SystemExit(f"GitHub API request failed: {exc.code} {exc.reason} ({url})") from exc
    except (URLError, TimeoutError) as exc:
        raise SystemExit(f"GitHub API request failed: {exc} ({url})") from exc


def fetch_all(endpoint: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    page = 1
    while True:
        batch = fetch_json(f"{API_ROOT}/{endpoint}", {"per_page": 100, "page": page})
        if not isinstance(batch, list):
            raise SystemExit(f"Expected a list from GitHub endpoint: {endpoint}")
        items.extend(batch)
        if len(batch) < 100:
            return items
        page += 1


def human_size(size: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB"]
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            return f"{int(value)} {unit}" if unit == "B" else f"{value:.1f} {unit}"
        value /= 1024
    return f"{size} B"


def normalize_repo(repo: dict[str, Any], current: dict[str, Any]) -> dict[str, Any]:
    # Version, C++/Qt requirements, maps, and bot counts are reviewed against source
    # code. The repository API does not report these facts and must not replace them.
    project = {key: value for key, value in current.items() if key != "synced_at"}
    for key in (
        "name", "full_name", "description", "html_url", "homepage", "default_branch",
        "created_at", "updated_at", "pushed_at", "stargazers_count", "forks_count",
        "open_issues_count",
    ):
        project[key] = repo.get(key)
    project["watchers_count"] = repo.get("subscribers_count", 0)
    project["topics"] = repo.get("topics") or []
    return project


def normalize_release(release: dict[str, Any], latest_stable_tag: str | None) -> dict[str, Any]:
    assets = []
    for asset in release.get("assets") or []:
        assets.append({
            "name": asset.get("name"),
            "size": asset.get("size", 0),
            "size_human": human_size(asset.get("size", 0)),
            "download_count": asset.get("download_count", 0),
            "content_type": asset.get("content_type"),
            "browser_download_url": asset.get("browser_download_url"),
            "updated_at": asset.get("updated_at"),
        })
    body = release.get("body") or ""
    return {
        "name": release.get("name") or release.get("tag_name"),
        "tag_name": release.get("tag_name"),
        "html_url": release.get("html_url"),
        "body": body,
        "summary": body.strip(),
        "draft": release.get("draft", False),
        "prerelease": release.get("prerelease", False),
        "published_at": release.get("published_at"),
        "created_at": release.get("created_at"),
        "author": (release.get("author") or {}).get("login"),
        "is_latest": release.get("tag_name") == latest_stable_tag,
        "zipball_url": release.get("zipball_url"),
        "tarball_url": release.get("tarball_url"),
        "assets": assets,
    }


def normalize_contributor(contributor: dict[str, Any]) -> dict[str, Any]:
    return {
        "login": contributor.get("login"),
        "html_url": contributor.get("html_url"),
        "avatar_url": contributor.get("avatar_url"),
        "contributions": contributor.get("contributions", 0),
        "type": contributor.get("type"),
    }


def write_if_changed(path: Path, payload: dict[str, Any], timestamp: str) -> bool:
    if path.exists():
        previous = json.loads(path.read_text(encoding="utf-8"))
        if {key: value for key, value in previous.items() if key != "synced_at"} == payload:
            return False
    encoded = json.dumps({**payload, "synced_at": timestamp}, indent=2, ensure_ascii=False) + "\n"
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(encoded, encoding="utf-8", newline="\n")
    temporary.replace(path)
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=SITE_ROOT / "data")
    args = parser.parse_args()
    data_dir = args.data_dir.resolve()
    project_path = data_dir / "project.json"
    if not project_path.exists():
        parser.error(f"reviewed project snapshot is missing: {project_path}")
    current_project = json.loads(project_path.read_text(encoding="utf-8"))
    repo = fetch_json(API_ROOT)
    releases = fetch_all("releases")
    contributors = fetch_all("contributors")
    latest = fetch_json(f"{API_ROOT}/releases/latest", allow_404=True)
    latest_stable_tag = latest.get("tag_name") if latest else None
    project = normalize_repo(repo, current_project)
    normalized_releases = [normalize_release(item, latest_stable_tag) for item in releases if not item.get("draft")]
    normalized_contributors = [normalize_contributor(item) for item in contributors]
    project["release_count"] = len(normalized_releases)
    project["contributor_count"] = len(normalized_contributors)
    timestamp = datetime.now(timezone.utc).isoformat()
    changed = []
    for name, payload in (
        ("project.json", project),
        ("releases.json", {"items": normalized_releases}),
        ("contributors.json", {"items": normalized_contributors}),
    ):
        if write_if_changed(data_dir / name, payload, timestamp):
            changed.append(name)
    print(f"Checked {len(normalized_releases)} releases and {len(normalized_contributors)} contributors.")
    print("Updated: " + ", ".join(changed) if changed else "Metadata is unchanged.")


if __name__ == "__main__":
    main()
