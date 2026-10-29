"""Yuhi building blocks: the genjutsu clan's wild waves, rose-and-thorn cloth and bandage wraps.

Kurenai's hair is long, black and untamed, so the clan's hair is drawn with waves: shade lines that
snake down each face instead of running straight, and locks whose segments step side to side so the
silhouette ripples. Her dress is a broad bandage wrap printed with rose thorns; `thorn_wrap` paints
that cloth, `thorn_vine` a single climbing stem, and `rose` a small half-scale bloom for pins,
brooches and crests. Everything paints key colors, so the thorns follow the outfit's accent."""
from __future__ import annotations

import math

from paint import k, rnd


# -- hair ------------------------------------------------------------------------------------
def wave_face(face, seed: int, base: int = 2, ring: int | None = None, clump: int = 3, tip_dark: bool = True,
              amp: float = 1.0, period: float = 3.2):
    """Cel-shaded hair whose strand lines snake: each shade line wanders a texel left and right as it
    falls, with a broken sheen band and darker tips."""
    off = int(rnd(seed, 1) * clump)
    phase = rnd(seed, 2) * 6.28
    for y in range(face.h):
        dx = round(amp * math.sin(y / period * 3.14159 + phase))
        for x in range(face.w):
            s = base
            if (x + off + dx) % clump == 0 and y > 0:
                s -= 1
            elif (x + off + dx) % clump == 1 and rnd(x, y, seed + 3) > .82:
                s += 1
            if ring is not None and y in (ring, ring + 1) and (x + off + dx) % clump != 0:
                s = base + (2 if y == ring and rnd(x, y, seed) > .25 else 1)
            if tip_dark and y == face.h - 1 and face.h > 2:
                s = min(s, base - 1)
            face.set(x, y, k("H", s))


def wave_box(box, seed: int, base: int = 2, ring: int | None = None, top_delta: int = 1, clump: int = 3, amp: float = 1.0):
    for f in box.sides:
        wave_face(f, seed + f.x0, base, ring, clump, amp=amp)
    for y in range(box.top.h):
        for x in range(box.top.w):
            box.top.set(x, y, k("H", base + top_delta - (1 if (x + y) % clump == 0 else 0)))
    box.bottom.fill(k("H", base - 2))


def wave_lock(g, pid: str, pivot, rotation=(0, 0, 0), segments=((3, 3), (3, 3), (2, 2), (1, 1)), depth: int = 1,
              seed: int = 0, base: int = 2, ring: int | None = 1, motion: str = "none", amp: float = .5, z_offset: float = 0,
              y0: float = 0.0, flip: bool = False):
    """A wavy lock: like anime.lock, but each segment steps sideways by `amp`, alternating, so the
    lock ripples as it tapers. Every segment shares one pivot, so the whole lock sways as one."""
    y = y0
    boxes = []
    for i, (w, h) in enumerate(segments):
        shift = amp * (1 if (i % 2 == 0) != flip else -1) if i else 0
        box = g.piece(f"{pid}_{i}", "HEAD", (-w / 2 + shift, y, -depth / 2 + z_offset), (w, h, depth), pivot=pivot,
                      rotation=rotation, motion=motion)
        wave_box(box, seed + i * 7, base, ring if i == 0 else None, top_delta=1 if i == 0 else 0)
        y += h
        boxes.append(box)
    return boxes


def wave_fan(g, prefix: str, specs, seed: int = 0, base: int = 2, z: float = 4.25, y: float = -7.6, motion: str = "sway",
             depth: int = 1, amp: float = .5):
    """Wavy locks hanging down the back: specs are (x, segments, rz, rx)."""
    for i, (x, segments, rz, rx) in enumerate(specs):
        wave_lock(g, f"{prefix}_{i}", (x, y, z), (rx, 0, rz), segments, depth, seed + i * 11, base, ring=1, motion=motion,
                  amp=amp, flip=bool(i % 2))


def wave_curtain(g, prefix: str, pivot, tilt, bands, seed: int = 0, base: int = 2, depth: int = 1, motion: str = "sway",
                 amp: float = .5):
    """A back sheet of wavy hair built as stacked bands that alternate sideways, so both edges ripple:
    `bands` lists (width, height) from the crown down; narrowing bands give a pointed hem."""
    y = 0.0
    for i, (w, h) in enumerate(bands):
        shift = amp * (1 if i % 2 else -1) if i else 0
        box = g.piece(f"{prefix}_{i}", "HEAD", (-w / 2 + shift, y, -depth / 2), (w, h, depth), pivot=pivot, rotation=tilt,
                      motion=motion)
        wave_box(box, seed + i * 5, base, 1 if i == 0 else None, top_delta=1 if i == 0 else 0)
        y += h
    return y


def wave_shell(g, seed: int, base: int = 2, side_rows: int = 6, back_rows: int = 8, ring_row: int = 1):
    """Hat-layer hair with a sheen band and snaking strand lines."""
    hat = g.part("hat")
    for y in range(8):
        for x in range(8):
            hat.top.set(x, y, k("H", base + 1 - (1 if (x + y * 3) % 5 == 0 else 0)))
    for face, rows in ((hat.back, back_rows), (hat.right, side_rows), (hat.left, side_rows)):
        sub = type(face)(face.layer, face.x0, face.y0, face.w, rows, face.name)
        wave_face(sub, seed + face.x0, base, ring_row, tip_dark=False)
        for x in range(face.w):
            if rnd(x, rows, seed) < .55 and rows < 8:
                face.set(x, rows, k("H", base - 1))
    hat.front.hline(0, 7, 0, k("H", base))
    return hat


# -- cloth -----------------------------------------------------------------------------------
def bandage_turns(face, x0: int, y0: int, x1: int, y1: int, role: str = "S", base: int = 3, lean: int = 1):
    """Broad bandage turns wound on a slant: a shaded seam every third texel, a lit edge above it."""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            t = (x * lean + y) % 3
            face.set(x, y, k(role, base - 1 if t == 0 else (base + 1 if t == 1 and rnd(x, y, 7) > .6 else base)))


def thorn_wrap(face, x0: int, y0: int, x1: int, y1: int, role: str = "P", thorn: str = "A", base: int = 2, seed: int = 0,
               step: int = 4):
    """Kurenai's dress cloth: broad bandage turns printed with thorny stems. Every `step` columns a stem
    snakes down the cloth in the thorn role, throwing a short thorn to alternate sides."""
    bandage_turns(face, x0, y0, x1, y1, role, base, lean=-1)
    off = int(rnd(seed, 5) * step)
    for y in range(y0, y1 + 1):
        for sx in range(x0 - step + off, x1 + 1, step):
            x = sx + (1 if (y // 2) % 2 else 0)
            if x0 <= x <= x1:
                face.set(x, y, k(thorn, 2))
            if y % 3 == 1:
                tx = x + (1 if (y // 3) % 2 else -1)
                if x0 <= tx <= x1:
                    face.set(tx, y, k(thorn, 1))


def thorn_vine(face, x: int, y0: int, y1: int, thorn: str = "A", base: int = 2):
    """One climbing stem with thorns, for a sleeve, a sash or a hem."""
    for y in range(y0, y1 + 1):
        xx = x + (1 if (y // 2) % 2 else 0)
        face.set(xx, y, k(thorn, base))
        if y % 3 == 0:
            face.set(xx + (1 if (y // 3) % 2 else -1), y, k(thorn, base - 1))


def thorn_band(face, y: int, thorn: str = "A", ground: str | None = None, base: int = 2):
    """A row of thorns along a hem: a stem line with a thorn raised every third texel."""
    if ground:
        face.hline(0, face.w - 1, y, ground)
    for x in range(face.w):
        face.set(x, y, k(thorn, base))
        if x % 3 == 1 and y > 0:
            face.set(x, y - 1, k(thorn, base - 1))


def mist_swirls(face, x0: int, y0: int, x1: int, y1: int, role: str = "S", base: int = 2):
    """Genjutsu mist: loose spirals traced in a light shade over a cloth, two texels apart."""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            u, v = (x - x0) % 6, (y - y0 + (x - x0) // 6 * 3) % 6
            if (u, v) in ((1, 1), (2, 1), (3, 1), (4, 2), (4, 3), (3, 4), (2, 4), (2, 3)):
                face.set(x, y, k(role, base))


def rose(g, pid: str, pivot, bone: str = "HEAD", rotation=(0, 0, 0), petal: str = "A", base: int = 2, leaf: str | None = None):
    """A half-scale rose facing local -z: a 3 x 3 bloom of wound petals with a dark heart, and an
    optional leaf below it. Small enough for a hairpin or a brooch."""
    s = (.5, .5, .5)
    bloom = g.piece(f"{pid}_bloom", bone, (-1.5, -1.5, -1), (3, 3, 2), pivot=pivot, rotation=rotation, scale=s)
    for f in bloom.faces:
        f.fill(k(petal, base))
    for f in bloom.sides:
        f.set(0, 0, k(petal, base + 1)), f.set(f.w - 1, 0, k(petal, base + 1))
        f.set(0, f.h - 1, k(petal, base - 1)), f.set(f.w - 1, f.h - 1, k(petal, base - 1))
    bloom.front.set(1, 1, k(petal, base - 2))
    bloom.front.set(2, 1, k(petal, base + 1)), bloom.front.set(1, 0, k(petal, base + 2))
    bloom.top.fill(k(petal, base + 1))
    if leaf:
        lf = g.piece(f"{pid}_leaf", bone, (-.5, 1.5, -.5), (2, 1, 1), pivot=pivot, rotation=rotation, scale=s)
        for f in lf.faces:
            f.fill(k(leaf, 2))
    return bloom
