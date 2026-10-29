"""16 x 16 block textures painted in code, the way the wardrobe paints its pieces: a few flat tones,
seeded noise for grain, then lines and stamps. Every texture is RGBA uint8."""
from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

FONT = Path("/usr/share/fonts/truetype/fonts-japanese-gothic.ttf")


def hexrgb(c) -> tuple[int, int, int]:
    if not isinstance(c, str):
        return tuple(c)
    c = c.lstrip("#")
    return int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)


def shade(c: str, k: float) -> tuple[int, int, int]:
    """k < 1 darkens, k > 1 lightens toward white."""
    r, g, b = hexrgb(c)
    if k <= 1:
        return int(r * k), int(g * k), int(b * k)
    t = k - 1
    return int(r + (255 - r) * t), int(g + (255 - g) * t), int(b + (255 - b) * t)


class Tex:
    def __init__(self, color: str = "#000000", w: int = 16, h: int = 16, alpha: int = 255):
        self.a = np.zeros((h, w, 4), np.uint8)
        self.a[..., :3] = hexrgb(color)
        self.a[..., 3] = alpha
        self.w, self.h = w, h

    def px(self, x, y, c, alpha=255):
        if 0 <= x < self.w and 0 <= y < self.h:
            self.a[y, x, :3] = hexrgb(c)
            self.a[y, x, 3] = alpha
        return self

    def rect(self, x0, y0, x1, y1, c, alpha=255):
        """Inclusive pixel rectangle."""
        for y in range(max(0, y0), min(self.h, y1 + 1)):
            for x in range(max(0, x0), min(self.w, x1 + 1)):
                self.px(x, y, c, alpha)
        return self

    def hline(self, y, c, x0=0, x1=None):
        return self.rect(x0, y, self.w - 1 if x1 is None else x1, y, c)

    def vline(self, x, c, y0=0, y1=None):
        return self.rect(x, y0, x, self.h - 1 if y1 is None else y1, c)

    def clear(self, x0, y0, x1, y1):
        self.a[y0:y1 + 1, x0:x1 + 1, 3] = 0
        return self

    def grain(self, seed: int, amount: float = .06, axis: str | None = None):
        """Seeded brightness noise; axis 'x' or 'y' stretches it into wood or weave grain."""
        rng = np.random.default_rng(seed)
        n = rng.normal(0, amount, (self.h, self.w))
        if axis == "x":
            n = np.repeat(rng.normal(0, amount, (self.h, 1)), self.w, 1) * .7 + n * .3
        elif axis == "y":
            n = np.repeat(rng.normal(0, amount, (1, self.w)), self.h, 0) * .7 + n * .3
        rgb = self.a[..., :3].astype(np.float32) * (1 + n[..., None])
        self.a[..., :3] = np.clip(rgb, 0, 255).astype(np.uint8)
        return self

    def stamp(self, rows: list[str], x0: int, y0: int, legend: dict):
        for y, row in enumerate(rows):
            for x, ch in enumerate(row):
                if ch in legend:
                    self.px(x0 + x, y0 + y, legend[ch])
        return self

    def glyph(self, text: str, c: str, size: int = 12, cx: float | None = None, cy: float | None = None,
              threshold: int = 110):
        """A kanji or kana stamped at pixel scale (IPA Gothic, thresholded). Check small glyphs by eye:
        at 16 px only bold, simple characters read."""
        font = ImageFont.truetype(str(FONT), size * 4)
        img = Image.new("L", (self.w * 4, self.h * 4), 0)
        d = ImageDraw.Draw(img)
        box = d.textbbox((0, 0), text, font=font)
        gw, gh = box[2] - box[0], box[3] - box[1]
        cx = self.w / 2 if cx is None else cx
        cy = self.h / 2 if cy is None else cy
        d.text((cx * 4 - gw / 2 - box[0], cy * 4 - gh / 2 - box[1]), text, fill=255, font=font)
        small = np.array(img.resize((self.w, self.h), Image.BOX))
        for y, x in zip(*np.nonzero(small > threshold)):
            self.px(int(x), int(y), c)
        return self

    def copy(self) -> "Tex":
        t = Tex(w=self.w, h=self.h)
        t.a = self.a.copy()
        return t

    def save(self, path: Path):
        path.parent.mkdir(parents=True, exist_ok=True)
        Image.fromarray(self.a, "RGBA").save(path)
