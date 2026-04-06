from __future__ import annotations

import json
import math
import shutil
import subprocess
import tempfile
from collections import Counter
from datetime import datetime
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont  # pyright: ignore[reportMissingImports]

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
STATIC_DIR = ROOT / "static"
OUTPUT_DIR = STATIC_DIR / "img" / "generated"
VIDEO_DIR = STATIC_DIR / "video"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_DIR.mkdir(parents=True, exist_ok=True)

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
CYAN_RGB = (110, 231, 255)
PURPLE_RGB = (139, 92, 246)
TEAL_RGB = (52, 211, 153)
AMBER_RGB = (251, 191, 36)
ROSE_RGB = (251, 113, 133)


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


def ensure_ffmpeg() -> str:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise SystemExit("ffmpeg is required to generate the sample video assets.")
    return ffmpeg


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = ["DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf", "DejaVuSans.ttf"]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def mix_rgb(first: tuple[int, int, int], second: tuple[int, int, int], ratio: float) -> tuple[int, int, int]:
    ratio = max(0.0, min(1.0, ratio))
    return (
        int(round(first[0] + (second[0] - first[0]) * ratio)),
        int(round(first[1] + (second[1] - first[1]) * ratio)),
        int(round(first[2] + (second[2] - first[2]) * ratio)),
    )


def rgba(color: tuple[int, int, int], alpha: int) -> tuple[int, int, int, int]:
    return (*color, alpha)


def save_frame(image: Image.Image, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)


def encode_video_from_frames(frame_dir: Path, output_mp4: Path, output_webm: Path, fps: int) -> None:
    ffmpeg = ensure_ffmpeg()
    pattern = str(frame_dir / "frame_%03d.png")
    common = [ffmpeg, "-y", "-hide_banner", "-loglevel", "error", "-framerate", str(fps), "-i", pattern]
    subprocess.run(common + ["-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(output_mp4)], check=True)
    subprocess.run(common + ["-c:v", "libvpx", "-pix_fmt", "yuv420p", "-crf", "34", "-b:v", "0", str(output_webm)], check=True)


def draw_labeled_chip(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    label: str,
    fill: tuple[int, int, int, int],
    outline: tuple[int, int, int, int],
    font: ImageFont.ImageFont,
) -> None:
    draw.rounded_rectangle(box, radius=box[3] - box[1], fill=fill, outline=outline, width=1)
    x1, y1, x2, y2 = box
    text_box = draw.textbbox((0, 0), label, font=font)
    text_width = text_box[2] - text_box[0]
    text_height = text_box[3] - text_box[1]
    draw.text(
        (x1 + (x2 - x1 - text_width) / 2, y1 + (y2 - y1 - text_height) / 2 - 1),
        label,
        font=font,
        fill=(239, 246, 255, 255),
    )


def generate_simulation_frame(index: int, total_frames: int, width: int = 960, height: int = 540) -> Image.Image:
    progress = index / max(total_frames - 1, 1)
    image = Image.new("RGBA", (width, height), (7, 17, 31, 255))
    draw = ImageDraw.Draw(image, "RGBA")
    title_font = load_font(30, bold=True)
    subtitle_font = load_font(15)
    body_font = load_font(13)
    chip_font = load_font(12, bold=True)
    tiny_font = load_font(11)

    draw.ellipse((-100, -60, 260, 260), fill=rgba(CYAN_RGB, 30))
    draw.ellipse((700, 320, 1020, 650), fill=rgba(PURPLE_RGB, 28))
    draw.ellipse((360, 40, 700, 340), fill=rgba(TEAL_RGB, 20))

    panel = (54, 86, 906, 454)
    board = (98, 142, 862, 388)
    draw.rounded_rectangle(panel, radius=34, fill=(15, 28, 49, 245), outline=(255, 255, 255, 24), width=1)
    draw.rounded_rectangle(board, radius=26, fill=(10, 18, 34, 255), outline=(255, 255, 255, 18), width=1)

    cols, rows = 12, 6
    cell_w = (board[2] - board[0]) / cols
    cell_h = (board[3] - board[1]) / rows
    center_a = (
        board[0] + 96 + (board[2] - board[0] - 192) * progress,
        board[1] + 74 + 34 * math.sin(progress * math.tau),
    )
    center_b = (
        board[2] - 96 - (board[2] - board[0] - 192) * progress,
        board[3] - 72 + 34 * math.cos(progress * math.tau),
    )

    for row in range(rows):
        for col in range(cols):
            left = int(board[0] + col * cell_w)
            top = int(board[1] + row * cell_h)
            right = int(board[0] + (col + 1) * cell_w)
            bottom = int(board[1] + (row + 1) * cell_h)
            cx = (left + right) / 2
            cy = (top + bottom) / 2
            dist_a = math.hypot(cx - center_a[0], cy - center_a[1])
            dist_b = math.hypot(cx - center_b[0], cy - center_b[1])
            owner = CYAN_RGB if dist_a <= dist_b else PURPLE_RGB
            pulse = max(0.16, 1 - min(dist_a, dist_b) / 310)
            fill = rgba(mix_rgb((20, 29, 50), owner, pulse), int(72 + 138 * pulse))
            outline = rgba((255, 255, 255), 14 + int(52 * pulse))
            draw.rounded_rectangle((left + 2, top + 2, right - 2, bottom - 2), radius=9, fill=fill, outline=outline, width=1)
            if abs(dist_a - dist_b) < 35:
                draw.rounded_rectangle(
                    (left + 5, top + 5, right - 5, bottom - 5),
                    radius=8,
                    outline=rgba(AMBER_RGB, 92),
                    width=1,
                )

    for offset, color in ((-0.08, CYAN_RGB), (0.08, PURPLE_RGB)):
        phase = (progress + offset) % 1.0
        px = board[0] + 120 + (board[2] - board[0] - 240) * phase
        py = board[1] + 74 + 40 * math.sin((phase + offset) * math.tau * 1.6)
        draw.ellipse((px - 18, py - 18, px + 18, py + 18), fill=rgba(color, 128), outline=rgba((255, 255, 255), 220), width=3)
        draw.line((board[0] + 120, board[3] - 54, px, py), fill=rgba(color, 165), width=4)

    draw.text((84, 32), "SIMULATION SAMPLE", font=title_font, fill=(239, 246, 255, 255))
    draw.text(
        (84, 65),
        "Bot-vs-bot pressure loop with moving frontiers and replay-style pacing.",
        font=subtitle_font,
        fill=(169, 189, 215, 255),
    )

    status_box = (88, 414, 876, 492)
    draw.rounded_rectangle(status_box, radius=22, fill=(16, 29, 50, 250), outline=(255, 255, 255, 20), width=1)
    draw_labeled_chip(draw, (114, 434, 238, 458), "OFFLINE", rgba(CYAN_RGB, 34), rgba(CYAN_RGB, 110), chip_font)
    draw_labeled_chip(draw, (250, 434, 342, 458), "LAN", rgba(PURPLE_RGB, 34), rgba(PURPLE_RGB, 110), chip_font)
    draw_labeled_chip(draw, (354, 434, 468, 458), "REPLAY", rgba(TEAL_RGB, 34), rgba(TEAL_RGB, 110), chip_font)
    draw.text((516, 432), f"TURN {index + 1:02d}/{total_frames:02d}", font=body_font, fill=(239, 246, 255, 255))
    draw.text(
        (516, 453),
        "Cyan and violet fronts converge while the match keeps looping.",
        font=tiny_font,
        fill=(169, 189, 215, 255),
    )
    draw.text((728, 432), "STATUS", font=tiny_font, fill=(169, 189, 215, 255))
    draw.text((728, 451), "Stable preview", font=body_font, fill=(110, 231, 255, 255))

    return image


def generate_release_frame(index: int, total_frames: int, releases: dict, width: int = 960, height: int = 540) -> Image.Image:
    items = sorted(releases.get("items", []), key=lambda item: parse_timestamp(item["published_at"]))
    if not items:
        items = [
            {"tag_name": "v5.0", "prerelease": False, "published_at": "2024-01-01T00:00:00+00:00"},
            {"tag_name": "v5.5", "prerelease": False, "published_at": "2024-05-01T00:00:00+00:00"},
            {"tag_name": "v6.0-preview", "prerelease": True, "published_at": "2024-09-01T00:00:00+00:00"},
            {"tag_name": "v6.0", "prerelease": False, "published_at": "2025-01-01T00:00:00+00:00"},
        ]

    sample_count = min(8, len(items))
    if sample_count == 1:
        sample = items
    else:
        sample = [items[round(i * (len(items) - 1) / (sample_count - 1))] for i in range(sample_count)]

    progress = index / max(total_frames - 1, 1)
    image = Image.new("RGBA", (width, height), (7, 17, 31, 255))
    draw = ImageDraw.Draw(image, "RGBA")
    title_font = load_font(30, bold=True)
    subtitle_font = load_font(15)
    body_font = load_font(13)
    chip_font = load_font(12, bold=True)
    tiny_font = load_font(11)

    draw.ellipse((-120, -50, 200, 250), fill=rgba(PURPLE_RGB, 28))
    draw.ellipse((680, 300, 1020, 640), fill=rgba(CYAN_RGB, 26))
    draw.ellipse((320, 20, 620, 320), fill=rgba(TEAL_RGB, 18))

    panel = (54, 88, 906, 454)
    plot = (108, 154, 852, 364)
    draw.rounded_rectangle(panel, radius=34, fill=(15, 28, 49, 245), outline=(255, 255, 255, 24), width=1)
    draw.rounded_rectangle(plot, radius=26, fill=(10, 18, 34, 255), outline=(255, 255, 255, 18), width=1)

    points = []
    for idx, item in enumerate(sample):
        x = plot[0] + 60 + idx * ((plot[2] - plot[0] - 120) / max(len(sample) - 1, 1))
        value = 0.2 + (idx / max(len(sample) - 1, 1)) * 0.65 + (0.09 if item.get("prerelease") else 0.0)
        y = plot[3] - 36 - value * (plot[3] - plot[1] - 72)
        points.append((x, y, item, value))

    baseline = plot[3] - 36
    draw.line((plot[0] + 36, baseline, plot[2] - 36, baseline), fill=rgba((255, 255, 255), 32), width=2)

    if len(points) > 1:
        draw.line([(x, y) for x, y, _, _ in points], fill=rgba(CYAN_RGB, 170), width=4, joint="curve")

    active_index = min(len(points) - 1, int(progress * len(points)))
    for idx, (x, y, item, value) in enumerate(points):
        is_active = idx == active_index
        fill = AMBER_RGB if item.get("prerelease") else (CYAN_RGB if idx <= active_index else PURPLE_RGB)
        alpha = 240 if is_active else 160
        radius = 16 if is_active else 10
        draw.ellipse(
            (x - radius, y - radius, x + radius, y + radius),
            fill=rgba(fill, alpha),
            outline=rgba((255, 255, 255), 235),
            width=3 if is_active else 2,
        )
        draw.line((x, y, x, baseline), fill=rgba(fill, 52), width=2)
        tag = item.get("tag_name", "")
        tag_box = draw.textbbox((0, 0), tag, font=tiny_font)
        tag_w = tag_box[2] - tag_box[0]
        draw.text((x - tag_w / 2, y + 20), tag, font=tiny_font, fill=(239, 246, 255, 255))

    draw.text((84, 32), "RELEASE TIMELINE", font=title_font, fill=(239, 246, 255, 255))
    draw.text((84, 65), "Loop through stable builds, previews, and the project’s momentum.", font=subtitle_font, fill=(169, 189, 215, 255))

    summary_box = (88, 396, 876, 492)
    draw.rounded_rectangle(summary_box, radius=22, fill=(16, 29, 50, 250), outline=(255, 255, 255, 20), width=1)
    draw_labeled_chip(draw, (114, 416, 242, 440), "STABLE", rgba(TEAL_RGB, 34), rgba(TEAL_RGB, 110), chip_font)
    draw_labeled_chip(draw, (252, 416, 362, 440), "PREVIEW", rgba(AMBER_RGB, 34), rgba(AMBER_RGB, 110), chip_font)
    draw_labeled_chip(draw, (372, 416, 462, 440), "LIVE", rgba(PURPLE_RGB, 34), rgba(PURPLE_RGB, 110), chip_font)
    latest = sample[min(active_index, len(sample) - 1)]
    draw.text((514, 414), f"HIGHLIGHT {latest.get('tag_name', '')}", font=body_font, fill=(239, 246, 255, 255))
    draw.text(
        (514, 435),
        "Release cadence animated as a looping preview for the releases page.",
        font=tiny_font,
        fill=(169, 189, 215, 255),
    )
    draw.text((728, 414), "SYNCED", font=tiny_font, fill=(169, 189, 215, 255))
    draw.text((728, 433), f"{len(items)} releases", font=body_font, fill=(110, 231, 255, 255))

    return image


def build_video_from_frame_renderer(renderer, output_name: str, frame_total: int, fps: int, *renderer_args) -> None:
    with tempfile.TemporaryDirectory(dir=ROOT) as tmp_dir:
        frame_dir = Path(tmp_dir)
        first_frame = None
        for index in range(frame_total):
            frame = renderer(index, frame_total, *renderer_args)
            if first_frame is None:
                first_frame = frame.copy()
            frame.save(frame_dir / f"frame_{index:03d}.png")

        if first_frame is not None:
            save_frame(first_frame, OUTPUT_DIR / f"{output_name}-poster.png")

        encode_video_from_frames(
            frame_dir,
            VIDEO_DIR / f"{output_name}.mp4",
            VIDEO_DIR / f"{output_name}.webm",
            fps,
        )


def generate_sample_videos(project: dict, releases: dict) -> None:
    build_video_from_frame_renderer(generate_simulation_frame, "simulation-loop", 60, 20)
    build_video_from_frame_renderer(generate_release_frame, "release-loop", 60, 20, releases)


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
    generate_sample_videos(project, releases)
    generate_favicon()
    generate_webmanifest(project)


if __name__ == "__main__":
    main()
