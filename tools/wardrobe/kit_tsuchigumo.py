"""Tsuchigumo building blocks: the earth-spider crest, web-line trims, the twisted shimenawa rope of
the mountain shrine with its folded paper streamers, and chakra threads wound round the limbs.

The clan lives hidden in the mountains guarding the forbidden technique En no Gyoja sealed into his
heir as a spider on her back, so its clothes are shrine cloth in plum, ochre and umber, edged with
thin web lines rather than the beetles and high collars of the Aburame.
"""
from __future__ import annotations

from paint import fabric, k, line, solid

# The earth spider seen from above, for decals at double resolution: '#' body, '+' legs.
SPIDER = ["..+....+..",
          "+..+..+..+",
          ".+..##..+.",
          "..++##++..",
          "+..####..+",
          ".++####++.",
          "...####...",
          "..+.##.+..",
          ".+......+.",
          "+........+"]


def glyph(face, rows, x0: int, y0: int, legend: dict):
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch in legend:
                face.set(x0 + x, y0 + y, legend[ch])


def web(face, cx: int, cy: int, key: str, rings=(2, 4, 6), spokes: int = 8, x0: int = 0, y0: int = 0,
        x1: int | None = None, y1: int | None = None):
    """A spider web drawn on a face: straight spokes from (cx, cy) and diamond rings around it,
    clipped to the rectangle (x0, y0)-(x1, y1)."""
    x1 = face.w - 1 if x1 is None else x1
    y1 = face.h - 1 if y1 is None else y1
    reach = max(face.w, face.h)
    dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)][:spokes]
    for dx, dy in dirs:
        for i in range(1, reach):
            x, y = cx + dx * i, cy + dy * i
            if x0 <= x <= x1 and y0 <= y <= y1:
                face.set(x, y, key)
    for r in rings:
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                if abs(x - cx) + abs(y - cy) == r:
                    face.set(x, y, key)
    if x0 <= cx <= x1 and y0 <= cy <= y1:
        face.set(cx, cy, key)


def web_hem(face, y: int, key: str, sag: str | None = None, step: int = 4, up: bool = True):
    """A web-line trim: one straight thread along row `y` and shallow scallops of thread strung
    between anchor points every `step` texels, hanging on the row above (or below, `up=False`)."""
    face.hline(0, face.w - 1, y, key)
    yy = y - 1 if up else y + 1
    if 0 <= yy < face.h:
        for x in range(face.w):
            if x % step in (1, step - 1):
                face.set(x, yy, sag or key)
    yy2 = y - 2 if up else y + 2
    if 0 <= yy2 < face.h and step >= 4:
        for x in range(face.w):
            if x % step == 0:
                face.set(x, yy2, sag or key)


def threads(face, x0: int, y0: int, x1: int, y1: int, key: str, step: int = 3, crossed: bool = False):
    """Chakra threads wound over a face rectangle: one spiral of diagonals `step` texels apart, or
    with `crossed` a second set the other way."""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if (x - y) % step == 0 or (crossed and (x + y) % step == 0):
                face.set(x, y, key)


def shimenawa(g, pid: str = "rope", y: float = 8.6, role: str = "S", streamers: bool = True, seed: int = 23980):
    """The shrine's twisted straw rope tied round the waist, with folded paper streamers (shide)
    zigzagging down at the front."""
    rope = g.piece(pid, "TORSO", (-4.6, y, -2.6), (9, 2, 5), inflate=.12)
    solid(rope, role, "plain", seed, 2, edge=False)
    for f in rope.sides:
        for yy in range(f.h):
            for x in range(f.w):
                f.set(x, yy, k(role, 3 if (x + f.x0 + yy) % 3 == 0 else (1 if (x + f.x0 + yy) % 3 == 2 else 2)))
    knot = g.piece(f"{pid}_knot", "TORSO", (-1, -1, -1), (2, 2, 2), pivot=(1.6, y + 1, -2.9))
    solid(knot, role, "plain", seed + 1, 3, edge=False)
    if streamers:
        for i, x in enumerate((-2.4, 2.6)):
            shide = g.piece(f"{pid}_shide_{i}", "TORSO", (-1, 0, 0), (2, 6, 1), pivot=(x, y + 2, -2.95), scale=(.4, .4, .4))
            for f in shide.faces:
                f.fill("S4")
            for yy in range(6):   # the zigzag folds of the paper
                shide.front.set(yy % 2, yy, "S2")
    return rope


def spider_crest(g, pid: str, role: str, ink: str, pivot, bone: str = "TORSO", face: str = "back", seed: int = 23990,
                 scale: float = .5):
    """The earth spider on a small square plate: on the back by default, `face="front"` for a breast badge."""
    plate = g.piece(pid, bone, (-5, 0, 0), (10, 10, 1), pivot=pivot, scale=(scale, scale, scale))
    for f in plate.faces:
        fabric(f, role, "plain", seed, 2)
    glyph(getattr(plate, face), SPIDER, 0, 0, {"#": ink, "+": ink})
    return plate


def thread_spool(g, pid: str, pivot, role: str = "A", seed: int = 23995):
    """A wooden spool of wire thread hung at the hip."""
    spool = g.piece(pid, "TORSO", (-1, 0, -1), (2, 3, 2), pivot=pivot)
    solid(spool, role, "plain", seed, 3, edge=False)
    for f in spool.sides:
        f.hline(0, f.w - 1, 0, "L2"), f.hline(0, f.w - 1, 2, "L2")
    return spool


def drawn_line(face, points, key):
    for (ax, ay), (bx, by) in zip(points, points[1:]):
        line(face, ax, ay, bx, by, key)
