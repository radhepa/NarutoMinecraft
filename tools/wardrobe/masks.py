"""Porcelain ANBU masks: a white face plate drawn at double resolution (16 x 15 texels over the
8 x 7.5 face), a strap around the head, and raised features built from half-scale boxes: ears,
a snout, a beak. Every ANBU headwear builds its animal from these.

Plate legend: 4 3 2 are the porcelain shades (S), A the red markings, K the black eye slits and
nostrils, M steel, P the plate color of the armor.
"""
from glyphs import stamp
from paint import fabric, k, solid

LEGEND = {"4": "S4", "3": "S3", "2": "S2", "1": "S1", "A": "A2", "a": "A1", "K": "K0", "M": "M3", "P": "P2"}
HALF = (.5, .5, .5)


def strap(g, y: float = -5.4, role: str = "K"):
    box = g.piece("strap", "HEAD", (-4, y, -4), (8, 1, 8), inflate=.55)
    solid(box, role, "smooth", 171, 2, edge=False)


def plate(g, rows, seed: int = 172, pid: str = "mask"):
    assert len(rows) == 15 and all(len(r) == 16 for r in rows), "a mask plate is 16 x 15"
    face = g.piece(pid, "HEAD", (-8, 0, -1), (16, 15, 1), pivot=(0, -7.6, -4.3), scale=HALF)
    for f in face.faces:
        fabric(f, "S", "plain", seed, 2)
    stamp(face.front, rows, 0, 0, LEGEND)
    return face


def bump(g, pid: str, rows, size, pivot, rotation=(0, 0, 0), base: int = 3, seed: int = 173):
    """A raised half-scale feature (snout, brow ridge, horn base) centred on its pivot."""
    w, h, d = size
    box = g.piece(pid, "HEAD", (-w / 2, 0, -d / 2), size, pivot=pivot, rotation=rotation, scale=HALF)
    solid(box, "S", "plain", seed, base)
    if rows:
        stamp(box.front, rows, 0, 0, LEGEND)
    return box


def ears(g, segments, x: float = 2.6, tilt: float = 14, y: float = -7.6, z: float = -4.4, inner: str = "A2",
         prefix: str = "ear"):
    """Pointed ears standing on the top edge of the plate: stacked half-scale boxes from a wide base
    to a fine tip, the lower ones with a red inner ear."""
    for side, sign in (("right", -1), ("left", 1)):
        top = 0.0
        for i, (w, h) in enumerate(segments):
            top -= h
            box = g.piece(f"{prefix}_{side}_{i}", "HEAD", (-w / 2, top, -1), (w, h, 2), pivot=(x * sign, y, z),
                          rotation=(0, 0, tilt * sign), scale=HALF)
            solid(box, "S", "plain", 174 + i, 3, edge=False)
            if inner and w >= 3:
                box.front.vline(w // 2, 0, h - 1, inner)
            if inner and w >= 4:
                box.front.vline(w // 2 - 1, 0, h - 1, inner)


def beak(g, pivot=(0, -4.4, -4.8), tip: str = "S1", ridge: str | None = "A2"):
    """A hooked bird beak: a broad root on the plate, a narrower bridge and a tip curling down, with
    a colored ridge along the top and down the front of the hook."""
    for i, (origin, size) in enumerate((((-3, 0, -3), (6, 4, 3)), ((-2, 1, -6), (4, 3, 3)), ((-1, 3, -7), (2, 3, 2)))):
        box = g.piece(f"beak_{i}", "HEAD", origin, size, pivot=pivot, scale=HALF)
        solid(box, "S", "plain", 176 + i, 3)
        fabric(box.top, "S", "plain", 176 + i, 4)
        if ridge:
            w = size[0]
            box.top.vline(w // 2 - 1, 0, box.top.h - 1, ridge), box.top.vline(w // 2, 0, box.top.h - 1, ridge)
            box.front.vline(w // 2 - 1, 0, box.front.h - 1, ridge), box.front.vline(w // 2, 0, box.front.h - 1, ridge)
        if i == 2:
            box.front.hline(0, 1, box.front.h - 1, tip), box.bottom.fill("K1")
