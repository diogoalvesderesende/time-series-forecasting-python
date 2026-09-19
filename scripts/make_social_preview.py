#!/usr/bin/env python3
"""Generate assets/social-preview.png, the card shown when the repo is shared.

GitHub falls back to a generic card unless a custom image is set, so every share
on LinkedIn, X or Slack looks like every other repository. This draws a 1280x640
card with the course title, the rating and the model list.

GitHub has no API for the social preview, so the generated file has to be
uploaded by hand once: Settings -> General -> Social preview -> Upload an image.
The same file is also served by the Pages site as the og:image, which does not
need any manual step.

Run with:  python scripts/make_social_preview.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "assets" / "social-preview.png"

W, H = 1280, 640
BG = (17, 20, 26)
FG = (240, 242, 245)
MUTED = (150, 157, 170)
ACCENT = (110, 168, 255)
GOLD = (246, 177, 0)
CARD = (28, 32, 40)

TITLE = "Master Time Series\nForecasting with Python"
SUB = "Every notebook from the Udemy course"
MODELS = ["ARIMA / SARIMAX", "Prophet", "Holt-Winters", "LSTM",
          "Temporal Fusion Transformer", "N-BEATS", "Amazon Chronos",
          "AutoGluon", "Google TSMixer"]
STATS = [("4.3", "rating", GOLD), ("1,545", "reviews", FG),
         ("13,693", "students", FG), ("62", "notebooks", FG)]


def font(name: str, size: int):
    for candidate in (name, f"C:/Windows/Fonts/{name}"):
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def star(d, cx, cy, r, fill):
    """Five-pointed star, drawn rather than typed.

    The Unicode star renders as a missing-glyph box in the UI fonts available
    here, so the shape is built from points instead.
    """
    import math
    pts = []
    for i in range(10):
        radius = r if i % 2 == 0 else r * 0.42
        angle = math.radians(-90 + i * 36)
        pts.append((cx + radius * math.cos(angle), cy + radius * math.sin(angle)))
    d.polygon(pts, fill=fill)


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    f_title = font("seguisb.ttf", 66)
    f_sub = font("segoeui.ttf", 28)
    f_stat = font("seguisb.ttf", 34)
    f_label = font("segoeui.ttf", 20)
    f_chip = font("segoeui.ttf", 21)
    f_foot = font("segoeui.ttf", 22)

    # accent bar down the left edge
    d.rectangle([0, 0, 10, H], fill=ACCENT)

    x = 64
    y = 62
    for line in TITLE.split("\n"):
        d.text((x, y), line, font=f_title, fill=FG)
        y += 76
    y += 6
    d.text((x, y), SUB, font=f_sub, fill=MUTED)

    # stats row
    y += 66
    sx = x
    for value, label, colour in STATS:
        vw = d.textlength(value, font=f_stat)
        lw = d.textlength(label, font=f_label)
        d.text((sx, y), value, font=f_stat, fill=colour)
        width = max(vw, lw)
        if label == "rating":
            star(d, sx + vw + 20, y + 20, 15, GOLD)
            width = max(width, vw + 38)
        d.text((sx, y + 42), label, font=f_label, fill=MUTED)
        sx += width + 56

    # model chips, wrapped
    y += 104
    cx, cy = x, y
    for name in MODELS:
        tw = d.textlength(name, font=f_chip)
        if cx + tw + 32 > W - 64:
            cx = x
            cy += 48
        d.rounded_rectangle([cx, cy, cx + tw + 30, cy + 38], radius=19, fill=CARD)
        d.text((cx + 15, cy + 7), name, font=f_chip, fill=MUTED)
        cx += tw + 44

    d.text((x, H - 62), "github.com/diogoalvesderesende/time-series-forecasting-python",
           font=f_foot, fill=ACCENT)

    img.save(OUT, "PNG", optimize=True)
    print(f"{OUT.relative_to(REPO)}  {W}x{H}  {OUT.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()
