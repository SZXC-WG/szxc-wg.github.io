from __future__ import annotations

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
STATIC_DIR = ROOT / "static"
OUTPUT_DIR = STATIC_DIR / "img" / "generated"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

CARD_FILL = "#0f1c31"
CARD_BORDER = "rgba(255,255,255,0.12)"
TEXT_MAIN = "#eff6ff"
TEXT_MUTED = "#a9bdd7"
ACCENT = "#6ee7ff"
ACCENT_STRONG = "#4fd1f5"
VIOLET = "#8b5cf6"
SUCCESS = "#34d399"
WARNING = "#fbbf24"
DANGER = "#fb7185"
SURFACE = "#0c1628"


def load_json(name: str) -> dict:
    return json.loads((DATA_DIR / name).read_text(encoding="utf-8"))


def svg_text(value: object) -> str:
    return escape(str(value))


def wrap_words(text: str, max_chars: int, max_lines: int | None = None) -> list[str]:
    words = text.split()
    if not words:
        return []

    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        candidate = f"{current} {word}"
        if len(candidate) <= max_chars:
            current = candidate
        else:
            lines.append(current)
            current = word
    lines.append(current)

    if max_lines is not None and len(lines) > max_lines:
        trimmed = lines[:max_lines]
        remainder = " ".join(lines[max_lines - 1 :])
        tail = remainder[: max(0, max_chars - 1)].rstrip(" ,.;:")
        trimmed[-1] = f"{tail}…"
        return trimmed

    return lines


def text_block(
    x: float,
    y: float,
    text: str,
    *,
    max_chars: int,
    font_size: int,
    fill: str,
    line_height: int = 18,
    weight: str | None = None,
    anchor: str = "start",
    max_lines: int | None = None,
) -> str:
    weight_attr = f' font-weight="{weight}"' if weight else ""
    anchor_attr = f' text-anchor="{anchor}"' if anchor else ""
    lines = wrap_words(text, max_chars=max_chars, max_lines=max_lines)
    return "".join(
        f'<text x="{x}" y="{y + index * line_height}" font-size="{font_size}" fill="{fill}"{weight_attr}{anchor_attr}>{svg_text(line)}</text>'
        for index, line in enumerate(lines)
    )


def parse_timestamp(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def rounded_rect(x: float, y: float, w: float, h: float, r: float, *, fill: str, stroke: str = CARD_BORDER, stroke_width: int = 1) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" />'
    )


def write_svg(path: Path, width: int, height: int, content: str, defs: str = "") -> None:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" role="img" aria-labelledby="title desc">
  <title id="title">LocalGen generated visual</title>
  <desc id="desc">Automatically generated visual asset for the LocalGen website.</desc>
  <defs>
    <linearGradient id="bgGlow" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="#12213a" />
      <stop offset="100%" stop-color="#0a1322" />
    </linearGradient>
    <linearGradient id="accentLine" x1="0" x2="1" y1="0" y2="0">
      <stop offset="0%" stop-color="{ACCENT_STRONG}" />
      <stop offset="100%" stop-color="{VIOLET}" />
    </linearGradient>
    <linearGradient id="accentArea" x1="0" x2="0" y1="0" y2="1">
      <stop offset="0%" stop-color="rgba(110,231,255,0.32)" />
      <stop offset="100%" stop-color="rgba(110,231,255,0.02)" />
    </linearGradient>
    <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#020617" flood-opacity="0.42" />
    </filter>
    {defs}
  </defs>
  {content}
</svg>
'''
    path.write_text(svg, encoding="utf-8")


def generate_release_journey(project: dict, releases: dict) -> None:
    items = sorted(releases["items"], key=lambda item: parse_timestamp(item["published_at"]))
    width, height = 780, 456
    margin_left, margin_right, margin_top, margin_bottom = 68, 36, 172, 58
    plot_width = width - margin_left - margin_right
    plot_height = height - margin_top - margin_bottom

    dates = [parse_timestamp(item["published_at"]) for item in items]
    min_date, max_date = dates[0], dates[-1]
    span = max((max_date - min_date).days, 1)

    def x_for(date: datetime) -> float:
        return margin_left + ((date - min_date).days / span) * plot_width

    def y_for(value: float) -> float:
        return margin_top + plot_height - (value / len(items)) * plot_height

    points = []
    cumulative = 0
    for item, date in zip(items, dates):
        cumulative += 1
        points.append((x_for(date), y_for(cumulative), item))

    path_line = " ".join(
        [f"M {points[0][0]:.1f} {points[0][1]:.1f}"]
        + [f"L {x:.1f} {y:.1f}" for x, y, _ in points[1:]]
    )
    area_path = (
        f"M {points[0][0]:.1f} {margin_top + plot_height:.1f} "
        + " ".join([f"L {x:.1f} {y:.1f}" for x, y, _ in points])
        + f" L {points[-1][0]:.1f} {margin_top + plot_height:.1f} Z"
    )

    yearly_counts = Counter(date.year for date in dates)
    stable_count = sum(1 for item in items if not item["prerelease"])
    preview_count = len(items) - stable_count
    latest = next((item for item in reversed(items) if not item["prerelease"]), items[-1])

    grid_lines = []
    for tick in range(0, len(items) + 1, 5):
        y = y_for(tick)
        grid_lines.append(f'<line x1="{margin_left}" y1="{y:.1f}" x2="{width - margin_right}" y2="{y:.1f}" stroke="rgba(255,255,255,0.08)" stroke-dasharray="4 6" />')
        if tick:
            grid_lines.append(
                f'<text x="{margin_left - 14}" y="{y + 4:.1f}" text-anchor="end" font-size="12" fill="{TEXT_MUTED}">{tick}</text>'
            )

    year_ticks = []
    for year in sorted(yearly_counts):
        year_start = datetime(year, 1, 1, tzinfo=min_date.tzinfo)
        year_x = max(margin_left, min(width - margin_right, x_for(year_start)))
        year_ticks.append(
            f'<line x1="{year_x:.1f}" y1="{margin_top}" x2="{year_x:.1f}" y2="{margin_top + plot_height}" stroke="rgba(255,255,255,0.08)" />'
            f'<text x="{year_x:.1f}" y="{height - 18}" text-anchor="middle" font-size="12" fill="{TEXT_MUTED}">{year}</text>'
        )

    markers = []
    for x, y, item in points:
        fill = WARNING if item["prerelease"] else SUCCESS
        radius = 6 if item is latest else 4.5
        markers.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius}" fill="{fill}" stroke="#08111f" stroke-width="2" />')

    header_stats = [
        ("releases", str(project["release_count"]), ACCENT),
        ("stable", str(stable_count), SUCCESS),
        ("preview", str(preview_count), WARNING),
        ("latest", latest["tag_name"], VIOLET),
    ]
    stat_cards = []
    for index, (label, value, color) in enumerate(header_stats):
        x = 36 + index * 178
        stat_cards.append(
            rounded_rect(x, 28, 162, 44, 16, fill="#101d32", stroke="rgba(255,255,255,0.08)")
            + f'<text x="{x + 18}" y="48" font-size="11" fill="{TEXT_MUTED}" letter-spacing="1.4">{label.upper()}</text>'
            + f'<text x="{x + 18}" y="63" font-size="16" fill="{color}" font-weight="700">{svg_text(value)}</text>'
        )

    content = f'''
  <rect width="{width}" height="{height}" rx="32" fill="url(#bgGlow)" />
  <circle cx="670" cy="72" r="96" fill="rgba(110,231,255,0.10)" />
  <circle cx="94" cy="360" r="140" fill="rgba(139,92,246,0.08)" />
  <g filter="url(#softShadow)">{rounded_rect(22, 22, width - 44, height - 44, 28, fill=CARD_FILL)}</g>
    <text x="36" y="108" font-size="24" font-weight="700" fill="{TEXT_MAIN}">Release journey</text>
    {text_block(36, 132, "How LocalGen evolved from the first GUI builds to the current Qt-era branch.", max_chars=68, font_size=13, fill=TEXT_MUTED, line_height=18, max_lines=2)}
  {''.join(stat_cards)}
  <g>{''.join(grid_lines)}</g>
  <g>{''.join(year_ticks)}</g>
  <path d="{area_path}" fill="rgba(110,231,255,0.18)" />
  <path d="{path_line}" stroke="url(#accentLine)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
  <g>{''.join(markers)}</g>
    <text x="{width - 40}" y="{margin_top - 14}" text-anchor="end" font-size="12" fill="{TEXT_MUTED}">cumulative releases</text>
    <text x="{width - 40}" y="{height - 22}" text-anchor="end" font-size="12" fill="{TEXT_MUTED}">{min_date.year}–{max_date.year}</text>
'''
    write_svg(OUTPUT_DIR / "release-journey.svg", width, height, content)


def generate_bot_spectrum(project: dict, bots: dict) -> None:
    items = sorted(bots["items"], key=lambda item: (item["complexity_score"], item["enabled"], item["name"]))
    width, height = 780, 560
    row_height = 28
    top = 188
    columns = {1: 324, 2: 476, 3: 628}
    enabled_count = sum(1 for item in items if item["enabled"])

    column_labels = []
    for index, label in enumerate(["low", "medium", "high"], start=1):
        x = columns[index]
        column_labels.append(
            f'<text x="{x}" y="166" text-anchor="middle" font-size="13" fill="{TEXT_MUTED}" letter-spacing="1.1">{label.upper()}</text>'
            f'<line x1="{x}" y1="176" x2="{x}" y2="{height - 54}" stroke="rgba(255,255,255,0.08)" stroke-dasharray="4 8" />'
        )

    rows = []
    for index, item in enumerate(items):
        y = top + index * row_height
        color = {1: ACCENT, 2: WARNING, 3: DANGER}[item["complexity_score"]]
        pill_x = columns[item["complexity_score"]] - 52
        status_fill = SUCCESS if item["enabled"] else "rgba(255,255,255,0.14)"
        status_text = "enabled" if item["enabled"] else "disabled"
        rows.append(
            f'<text x="44" y="{y + 4}" font-size="13" fill="{TEXT_MAIN}" font-weight="600">{svg_text(item["name"])}</text>'
            f'<rect x="{pill_x}" y="{y - 14}" width="104" height="22" rx="11" fill="{color}" fill-opacity="0.18" stroke="{color}" stroke-opacity="0.45" />'
            f'<text x="{columns[item["complexity_score"]]}" y="{y}" text-anchor="middle" font-size="11" fill="{color}" font-weight="700">{svg_text(item["complexity"])}</text>'
            f'<text x="686" y="{y + 4}" text-anchor="end" font-size="11" fill="{TEXT_MUTED}">{svg_text(item["time_complexity"])}</text>'
            f'<rect x="698" y="{y - 13}" width="48" height="20" rx="10" fill="{status_fill}" fill-opacity="0.18" stroke="{status_fill}" stroke-opacity="0.45" />'
            f'<text x="722" y="{y + 1}" text-anchor="middle" font-size="9" fill="{status_fill}" font-weight="700">{status_text.upper()}</text>'
        )

    stat_cards = [
        ("built-in", str(len(items)), ACCENT),
        ("enabled", str(enabled_count), SUCCESS),
        ("external-ready", "v6", VIOLET),
    ]
    header_stats = []
    for index, (label, value, color) in enumerate(stat_cards):
        x = 36 + index * 178
        header_stats.append(
            rounded_rect(x, 28, 162, 44, 16, fill="#101d32", stroke="rgba(255,255,255,0.08)")
            + f'<text x="{x + 18}" y="48" font-size="11" fill="{TEXT_MUTED}" letter-spacing="1.4">{label.upper()}</text>'
            + f'<text x="{x + 18}" y="63" font-size="16" fill="{color}" font-weight="700">{svg_text(value)}</text>'
        )

    content = f'''
  <rect width="{width}" height="{height}" rx="32" fill="url(#bgGlow)" />
  <circle cx="652" cy="86" r="104" fill="rgba(251,191,36,0.09)" />
  <circle cx="118" cy="432" r="148" fill="rgba(139,92,246,0.08)" />
  <g filter="url(#softShadow)">{rounded_rect(22, 22, width - 44, height - 44, 28, fill=CARD_FILL)}</g>
  <text x="36" y="116" font-size="24" font-weight="700" fill="{TEXT_MAIN}">Built-in bot spectrum</text>
    {text_block(36, 138, "A quick view of which bots ship today, how complex they are, and how expensive their worst-case turns can get.", max_chars=72, font_size=13, fill=TEXT_MUTED, line_height=18, max_lines=2)}
  {''.join(header_stats)}
  {''.join(column_labels)}
  {''.join(rows)}
    <text x="686" y="166" text-anchor="end" font-size="13" fill="{TEXT_MUTED}" letter-spacing="1.1">TIME</text>
    <text x="722" y="166" text-anchor="middle" font-size="13" fill="{TEXT_MUTED}" letter-spacing="1.1">STATUS</text>
    <text x="36" y="{height - 24}" font-size="12" fill="{TEXT_MUTED}">Derived from the upstream built-in bot README and contribution guide.</text>
'''
    write_svg(OUTPUT_DIR / "bot-spectrum.svg", width, height, content)


def generate_project_pillars(project: dict) -> None:
    width, height = 820, 472
    card_y = 184
    card_w = 178
    card_h = 194
    gap = 18
    pillars = [
        ("Offline play", "Play generals.io entirely offline with ready-to-use built-in bots.", ACCENT, project["version_line"]),
        ("Same-LAN battles", "Set up local matches with nearby friends without a hosted backend.", SUCCESS, f"{project['release_count']} releases"),
        ("Bot laboratory", "Compare heuristics, ship built-in bots, or prototype external ones in any language.", WARNING, f"{project['bot_count']} bots"),
        ("Qt6 transition", "Track the active rewrite focused on portability, maintainability, and tooling.", VIOLET, "/".join(project["built_with"])),
    ]

    cards = []
    for index, (title, summary, color, meta) in enumerate(pillars):
        x = 32 + index * (card_w + gap)
        summary_block = text_block(
            x + 24,
            card_y + 104,
            summary,
            max_chars=26,
            font_size=12,
            fill=TEXT_MUTED,
            line_height=18,
            max_lines=3,
        )
        cards.append(
            rounded_rect(x, card_y, card_w, card_h, 24, fill="#101d32", stroke="rgba(255,255,255,0.08)")
            + f'<circle cx="{x + 34}" cy="{card_y + 34}" r="18" fill="{color}" fill-opacity="0.18" stroke="{color}" stroke-opacity="0.45" />'
            + f'<circle cx="{x + 34}" cy="{card_y + 34}" r="7" fill="{color}" />'
            + f'<text x="{x + 24}" y="{card_y + 74}" font-size="18" font-weight="700" fill="{TEXT_MAIN}">{svg_text(title)}</text>'
            + summary_block
            + f'<rect x="{x + 24}" y="{card_y + 148}" width="130" height="28" rx="14" fill="{color}" fill-opacity="0.16" />'
            + f'<text x="{x + 89}" y="{card_y + 166}" text-anchor="middle" font-size="11" fill="{color}" font-weight="700">{svg_text(meta)}</text>'
        )

    content = f'''
  <rect width="{width}" height="{height}" rx="32" fill="url(#bgGlow)" />
  <circle cx="90" cy="90" r="88" fill="rgba(110,231,255,0.10)" />
  <circle cx="730" cy="330" r="110" fill="rgba(139,92,246,0.09)" />
  <g filter="url(#softShadow)">{rounded_rect(22, 22, width - 44, height - 44, 28, fill=CARD_FILL)}</g>
  <text x="32" y="68" font-size="16" fill="{ACCENT}" font-weight="700" letter-spacing="2">PROJECT PILLARS</text>
  <text x="32" y="96" font-size="28" font-weight="700" fill="{TEXT_MAIN}">Why LocalGen feels different</text>
    {text_block(32, 124, "The README and docs keep returning to the same promise: local-first strategy play, open bot research, and a cleaner Qt-based future.", max_chars=90, font_size=13, fill=TEXT_MUTED, line_height=18, max_lines=2)}
  {''.join(cards)}
    <text x="32" y="436" font-size="12" fill="{TEXT_MUTED}">GPL-3.0 · {svg_text(project['organization'])} · source-backed from README and project guides</text>
'''
    write_svg(OUTPUT_DIR / "project-pillars.svg", width, height, content)


def generate_hero_board(project: dict) -> None:
    width, height = 820, 460
    tile_size = 56
    tile_gap = 10
    origin_x, origin_y = 176, 182
    tiles = []
    accents = [ACCENT_STRONG, WARNING, SUCCESS, VIOLET]
    for row in range(4):
        for col in range(5):
            x = origin_x + col * (tile_size + tile_gap)
            y = origin_y + row * (tile_size + tile_gap)
            radius = 22
            fill = "rgba(255,255,255,0.05)"
            if (row, col) in {(0, 0), (1, 2), (2, 3), (3, 1)}:
                fill = f"{accents[(row + col) % len(accents)]}22"
            tiles.append(rounded_rect(x, y, tile_size, tile_size, radius, fill=fill, stroke="rgba(255,255,255,0.08)"))

    arrows = [
        (248, 210, 392, 210),
        (392, 210, 536, 286),
        (320, 362, 536, 362),
    ]
    arrow_paths = []
    for x1, y1, x2, y2 in arrows:
        arrow_paths.append(
            f'<path d="M {x1} {y1} C {(x1 + x2) / 2:.1f} {y1 - 30:.1f}, {(x1 + x2) / 2:.1f} {y2 + 30:.1f}, {x2} {y2}" stroke="url(#accentLine)" stroke-width="4" stroke-linecap="round" />'
            f'<circle cx="{x2}" cy="{y2}" r="6" fill="{ACCENT}" />'
        )

    content = f'''
  <rect width="{width}" height="{height}" rx="36" fill="url(#bgGlow)" />
  <circle cx="128" cy="104" r="110" fill="rgba(110,231,255,0.14)" />
  <circle cx="706" cy="366" r="144" fill="rgba(139,92,246,0.12)" />
  <g filter="url(#softShadow)">{rounded_rect(24, 24, width - 48, height - 48, 30, fill=CARD_FILL)}</g>
  <text x="40" y="72" font-size="16" fill="{ACCENT}" font-weight="700" letter-spacing="2">OFFLINE-FIRST</text>
  <text x="40" y="106" font-size="34" fill="{TEXT_MAIN}" font-weight="700">Play, study, and extend</text>
  <text x="40" y="140" font-size="34" fill="{TEXT_MAIN}" font-weight="700">Local Generals.io.</text>
  <text x="40" y="176" font-size="14" fill="{TEXT_MUTED}">Built around ready-to-use bots, same-LAN matches, replay tools, and the active Qt6 rewrite.</text>
  <g>{''.join(tiles)}</g>
  <g>{''.join(arrow_paths)}</g>
  <circle cx="410" cy="278" r="44" fill="rgba(255,255,255,0.08)" stroke="{ACCENT}" stroke-width="2" />
  <path d="M 410 240 L 422 262 L 445 266 L 428 284 L 432 308 L 410 296 L 388 308 L 392 284 L 375 266 L 398 262 Z" fill="{WARNING}" />
  <text x="602" y="166" font-size="12" fill="{TEXT_MUTED}">CURRENT BRANCH</text>
  <text x="602" y="188" font-size="24" fill="{TEXT_MAIN}" font-weight="700">{svg_text(project['version_line'])}</text>
  <text x="602" y="234" font-size="12" fill="{TEXT_MUTED}">TOOLCHAIN</text>
  <text x="602" y="256" font-size="20" fill="{TEXT_MAIN}" font-weight="700">{svg_text(' · '.join(project['built_with']))}</text>
  <text x="602" y="302" font-size="12" fill="{TEXT_MUTED}">PROJECT SCALE</text>
  <text x="602" y="324" font-size="20" fill="{TEXT_MAIN}" font-weight="700">{project['release_count']} releases · {project['bot_count']} bots</text>
  <text x="602" y="370" font-size="12" fill="{TEXT_MUTED}">MAINTAINED BY</text>
  <text x="602" y="392" font-size="20" fill="{TEXT_MAIN}" font-weight="700">{svg_text(project['organization'])}</text>
'''
    write_svg(OUTPUT_DIR / "hero-board.svg", width, height, content)


def generate_favicon() -> None:
    content = f'''
  <rect width="64" height="64" rx="18" fill="url(#accentLine)" />
  <rect x="8" y="8" width="48" height="48" rx="14" fill="#08111f" fill-opacity="0.82" />
  <rect x="14" y="14" width="16" height="16" rx="6" fill="rgba(110,231,255,0.18)" stroke="{ACCENT}" stroke-opacity="0.45" />
  <rect x="34" y="14" width="16" height="16" rx="6" fill="rgba(139,92,246,0.18)" stroke="{VIOLET}" stroke-opacity="0.45" />
  <rect x="14" y="34" width="16" height="16" rx="6" fill="rgba(52,211,153,0.18)" stroke="{SUCCESS}" stroke-opacity="0.45" />
  <rect x="34" y="34" width="16" height="16" rx="6" fill="rgba(251,191,36,0.18)" stroke="{WARNING}" stroke-opacity="0.45" />
  <path d="M32 16 L37 26 L48 27 L40 36 L42 47 L32 41 L22 47 L24 36 L16 27 L27 26 Z" fill="{WARNING}" />
'''
    write_svg(STATIC_DIR / "favicon.svg", 64, 64, content)


def generate_webmanifest(project: dict) -> None:
    manifest = {
        "name": project["project_name"],
        "short_name": project["short_name"],
        "icons": [
            {"src": "/favicon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any"},
            {"src": "/favicon.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
        ],
        "theme_color": "#07111f",
        "background_color": "#07111f",
        "display": "standalone",
        "start_url": "/",
    }
    (STATIC_DIR / "site.webmanifest").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def main() -> None:
    project = load_json("project.json")
    releases = load_json("releases.json")
    bots = load_json("bots.json")
    project.setdefault("release_count", len(releases.get("items", [])))
    project.setdefault("bot_count", len(bots.get("items", [])))
    generate_release_journey(project, releases)
    generate_bot_spectrum(project, bots)
    generate_project_pillars(project)
    generate_hero_board(project)
    generate_favicon()
    generate_webmanifest(project)


if __name__ == "__main__":
    main()
