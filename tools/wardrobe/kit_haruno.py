"""Haruno building blocks: the merchant household's white circle crest at any size, the standing
mandarin collar and frog clasps of a qipao, and the contrast trim of a kimono collar. The crest is
the one thread through the clan's wardrobe, worn on the back like Sakura's and on shop aprons."""
from __future__ import annotations

import math

from kit import arm_bone
from paint import fabric, k, solid


def circle(face, x0: int, y0: int, size: int = 8, ring: float = 1.4, key: str = "S4", rim: str = "S2"):
    """The crest: a clean white ring `size` texels across, its lower inner edge shaded so it reads
    as embroidered on the cloth rather than printed."""
    c = size / 2
    r = c - .3
    for y in range(size):
        for x in range(size):
            d = math.hypot(x + .5 - c, y + .5 - c)
            if r - ring <= d <= r:
                face.set(x0 + x, y0 + y, rim if (d < r - ring + .6 and y >= c) else key)


def back_crest(g, role: str = "P", pivot=(0, 1.4, 2.05), texture: str = "weave", seed: int = 19990, base: int = 2,
               size: int = 10, pid: str = "back_crest"):
    """The crest across the shoulder blades at double resolution, on a thin plate of the garment's
    cloth. Raise pivot z to clear an overlay: 2.05 on the shirt, 2.35 on a jacket layer."""
    plate = g.piece(pid, "TORSO", (-size / 2, 0, 0), (size, size, 1), pivot=pivot, scale=(.5, .5, .5))
    for face in plate.faces:
        fabric(face, role, texture, seed, base)
    circle(plate.back, 0, 0, size, ring=1.6)
    return plate


def chest_crest(g, pid: str, x: float, y: float = 1.2, z: float = -2.1, role: str = "P", seed: int = 19991, base: int = 2,
                bone: str = "TORSO"):
    """A small crest on the chest or an apron, at triple resolution, facing front."""
    patch = g.piece(pid, bone, (-3, 0, -1), (6, 6, 1), pivot=(x, y, z), scale=(1 / 3, 1 / 3, 1 / 3))
    for face in patch.faces:
        fabric(face, role, "weave", seed, base)
    circle(patch.front, 0, 0, 6, ring=1.3)
    return patch


def arm_crest(g, side: str, role: str = "P", y: float = .8, out: float = 3.05, seed: int = 19992, base: int = 2):
    """A small crest patch on the outer upper arm, at double resolution."""
    x = -out - .5 if side == "right" else out
    patch = g.piece(f"{side}_arm_crest", arm_bone(side), (0, 0, -3), (1, 6, 6), pivot=(x, y, 0), scale=(.5, .5, .5))
    for face in patch.faces:
        fabric(face, role, "weave", seed, base)
    circle(patch.right if side == "right" else patch.left, 0, 0, 6, ring=1.3)
    return patch


def mandarin_collar(g, role: str = "P", seed: int = 19993, trim: str | None = None, y: float = -1.4, pid: str = "collar"):
    """The qipao's standing collar: a snug band round the neck, closed at the front with one clasp,
    its top edge piped in `trim`."""
    box = g.piece(pid, "TORSO", (-3, y, -2.4), (6, 2, 5), inflate=.08)
    solid(box, role, "smooth", seed, 2, edge=False)
    for face in box.sides:
        face.hline(0, face.w - 1, 0, trim or k(role, 3))
    box.front.vline(3, 0, 1, k(role, 0))
    return box


def frog_clasps(face, points, role: str = "S"):
    """Knotted frog fastenings across the qipao's slanted opening: a bright knot with a shaded loop."""
    for x, y in points:
        face.set(x, y, k(role, 4))
        face.set(x + 1, y, k(role, 2))


def kimono_trim(face, rows, role: str = "S", base: int = 3):
    """A crossed kimono collar painted down a body front: each (y, x) puts a two-texel trim band,
    stepping toward the centre to meet in a V."""
    for y, x in rows:
        face.set(x, y, k(role, base + 1)), face.set(x + 1, y, k(role, base - 1))
