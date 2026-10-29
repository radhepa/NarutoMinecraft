"""Senju building blocks: hair side panels and buns, the split-circle clan crest, and lacquered
Warring States armor plates (lames laced in rows) for the clan's tops."""
from __future__ import annotations

from anime import cel_box
from paint import fabric, k, solid


def side_panels(g, prefix: str, length: int, seed: int, top: float = -7.0, x: float = 4.6, z0: float = -3,
                depth: int = 7, flare: float = 0):
    """A sheet of straight hair over each ear, from `top` down `length` texels."""
    for side, sign in (("right", -1), ("left", 1)):
        panel = g.piece(f"{prefix}_{side}", "HEAD", (-.5, 0, z0), (1, length, depth), pivot=(x * sign, top, .6),
                        rotation=(0, 0, -flare * sign))
        cel_box(panel, seed + (sign > 0), ring=1)


def bun(g, pid: str, pivot, size=(4, 3, 3), seed: int = 0, rotation=(0, 0, 0), wrap: str | None = None):
    """A round knot of hair: a core box with a smaller cap on each broad side so it reads rounded."""
    w, h, d = size
    core = g.piece(pid, "HEAD", (-w / 2, -h / 2, -d / 2), size, pivot=pivot, rotation=rotation)
    cel_box(core, seed, ring=0)
    rw, rd = max(1, w - 2), max(1, d - 1)
    capb = g.piece(f"{pid}_round", "HEAD", (-rw / 2, -(h + 2) / 2, -rd / 2), (rw, h + 2, rd), pivot=pivot,
                   rotation=rotation)
    cel_box(capb, seed + 1, ring=1)
    if wrap:
        band = g.piece(f"{pid}_wrap", "HEAD", (-(w + .2) / 2, -.5, -(d + .2) / 2), (w, 1, d), pivot=pivot,
                       rotation=rotation, inflate=.1)
        for f in band.faces:
            f.fill(wrap)
    return core


# The Senju crest: a circle split by a vertical bar, the halves standing apart. 8 x 8 texels.
CREST = ["..####..",
         ".##..##.",
         "##....##",
         "##....##",
         "##....##",
         "##....##",
         ".##..##.",
         "..####.."]


def crest(face, x0: int, y0: int, key: str, bar: str | None = None):
    for y, row in enumerate(CREST):
        for x, ch in enumerate(row):
            if ch == "#":
                face.set(x0 + x, y0 + y, key)
    if bar:
        face.vline(x0 + 3, y0 + 1, y0 + 6, bar), face.vline(x0 + 4, y0 + 1, y0 + 6, bar)


def lames(face, role: str, y0: int, y1: int, step: int = 2, lace: str | None = "A2", base: int = 2, x0: int = 0,
          x1: int | None = None):
    """Lacquered plates in horizontal rows: a lit upper edge per row, a dark lower edge and lacing
    dots (odoshi) in the accent between them."""
    x1 = face.w - 1 if x1 is None else x1
    for y in range(y0, y1 + 1):
        r = (y - y0) % step
        for x in range(x0, x1 + 1):
            if r == 0:
                key = k(role, base + 1)
            elif r == step - 1:
                key = k(role, base - 1)
            else:
                key = k(role, base)
            if lace and r == step - 1 and x % 3 == 1:
                key = lace
            face.set(x, y, key)


def plate(g, pid: str, bone: str, origin, size, role: str = "P", seed: int = 0, pivot=(0, 0, 0), rotation=(0, 0, 0),
          step: int = 2, lace: str | None = "A2", inflate: float = 0):
    """A box of laced lames: every side carries the plate rows, the top is lit, the underside dark."""
    box = g.piece(pid, bone, origin, size, pivot=pivot, rotation=rotation, inflate=inflate)
    solid(box, role, "smooth", seed, 2)
    for f in box.sides:
        lames(f, role, 0, f.h - 1, step, lace)
    fabric(box.top, role, "smooth", seed, 3)
    box.bottom.fill(k(role, 0))
    return box


def shoulder_guards(g, prefix: str = "shoulder_guard", length: int = 6, seed: int = 0, role: str = "P",
                    lace: str | None = "A2", flare: float = 14, depth: int = 5, top: float = -2.4):
    """Sode: a laced plate hanging off the outside of each shoulder, flaring out at the hem."""
    for side, bone, sign in (("right", "RIGHT_ARM", -1), ("left", "LEFT_ARM", 1)):
        plate(g, f"{side}_{prefix}", bone, (-.5, 0, -depth / 2), (1, length, depth), role, seed + (sign > 0),
              pivot=(3.45 * sign, top, 0), rotation=(0, 0, -flare * sign), step=3, lace=lace)
