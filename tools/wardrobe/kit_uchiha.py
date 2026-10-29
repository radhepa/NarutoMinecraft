"""Uchiha building blocks: the red-and-white uchiwa crest at any size, the clan's tall open collar,
white arm warmers and the lamellar plates of Warring States armor."""
from __future__ import annotations

import math

from kit import arm_bone, arm_x
from paint import fabric, k, solid, strip_fabric


def crest(face, x0: int, y0: int, size: int = 10, handle: int = 5):
    """The uchiwa: a round fan, red above and white below with a darker rim, on a white handle.
    `size` is the fan's diameter in texels; the handle hangs `handle` rows below it."""
    c = size / 2
    r = c - .4
    rim = .9 if size >= 8 else .7
    for y in range(size):
        for x in range(size):
            d = math.hypot(x + .5 - c, y + .5 - c)
            if d > r:
                continue
            upper = y < size // 2
            key = "A2" if upper else "S3"
            if d > r - rim:
                key = "A1" if upper else "S2"
            elif upper and x + y < size // 2:
                key = "A3"
            face.set(x0 + x, y0 + y, key)
    mid = x0 + size // 2
    for y in range(size, size + handle):
        face.set(mid - 1, y0 + y, "S3"), face.set(mid, y0 + y, "S2")


def back_crest(g, role: str = "P", pivot=(0, 1.0, 2.05), texture: str = "weave", seed: int = 3990, base: int = 2,
               width: int = 10, height: int = 16):
    """The crest across the shoulder blades at double resolution, on a thin plate of the garment's
    cloth. Raise pivot z to clear an overlay: 2.05 on the shirt, 2.35 on a jacket layer. A wider or
    taller plate covers a patch beneath it, the crest centred on it."""
    plate = g.piece("back_crest", "TORSO", (-width / 2, 0, 0), (width, height, 1), pivot=pivot, scale=(.5, .5, .5))
    for face in plate.faces:
        fabric(face, role, texture, seed, base)
    crest(plate.back, (width - 10) // 2, (height - 15) // 2)
    return plate


def arm_crest(g, side: str, role: str = "P", y: float = .6, out: float = 3.05, seed: int = 3991, base: int = 2):
    """A small crest patch on the outer upper arm, at double resolution."""
    x = -out - .5 if side == "right" else out
    patch = g.piece(f"{side}_arm_crest", arm_bone(side), (0, 0, -3), (1, 9, 6), pivot=(x, y, 0), scale=(.5, .5, .5))
    for face in patch.faces:
        fabric(face, role, "weave", seed, base)
    outer = patch.right if side == "right" else patch.left
    crest(outer, 0, 0, size=6, handle=3)
    return patch


def chest_crest(g, pid: str, x: float, y: float = 1.0, z: float = -2.1, role: str = "P", seed: int = 3992, base: int = 2):
    """A small crest on the chest (a haori's mon), at triple resolution, facing front."""
    patch = g.piece(pid, "TORSO", (-3, 0, -1), (6, 9, 1), pivot=(x, y, z), scale=(1 / 3, 1 / 3, 1 / 3))
    for face in patch.faces:
        fabric(face, role, "weave", seed, base)
    crest(patch.front, 0, 0, size=6, handle=3)
    return patch


def high_collar(g, role: str = "P", seed: int = 3993, height: int = 3, z: float = 1.6, flare: float = 6,
                trim: str | None = None):
    """The tall open collar: a back panel and two side wings standing up round the neck, open at the
    front. `trim` keys the top edge (the light shade of the role by default)."""
    edge = trim or k(role, 3)
    back = g.piece("collar_back", "TORSO", (-4.5, -height + .4, 0), (9, height, 1), pivot=(0, 0, z), rotation=(-8, 0, 0))
    solid(back, role, "weave", seed, 2)
    for face in back.sides:
        face.hline(0, face.w - 1, 0, edge)
    for side, x, rz in (("right", -4.5, -flare), ("left", 3.5, flare)):
        wing = g.piece(f"collar_{side}", "TORSO", (0, -height + .4, -2.6), (1, height, 4), pivot=(x, 0, 0), rotation=(0, 0, rz))
        solid(wing, role, "weave", seed + 1, 2)
        for face in wing.sides:
            face.hline(0, face.w - 1, 0, edge)
    return back


def arm_warmers(g, rows=(6, 10), role: str = "S", seed: int = 3995, cuff: bool = True):
    """Ribbed warmers from below the elbow to the wrist, with a rolled cuff at the top."""
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        for y in range(rows[0], rows[1] + 1):
            for x in range(arm.strip.w):
                arm.strip.set(x, y, k(role, 2) if y in rows else k(role, 3 if x % 2 else 4))
        if cuff:
            ring = g.piece(f"{side}_warmer_cuff", arm_bone(side), (arm_x(side) - .3, rows[0] - .4, -2.3), (4, 1, 4),
                           inflate=.12)
            solid(ring, role, "rib", seed + (side == "left"), 3)


def lamellar(face, role: str = "P", lace: str = "K2", seed: int = 3996, x0: int = 0, y0: int = 0, w=None, h=None, step: int = 3):
    """Warring States lamellar: rows of small plates, each row lit on top and shaded underneath,
    laced with a cord every few texels."""
    w = face.w - x0 if w is None else w
    h = face.h - y0 if h is None else h
    fabric(face, role, "leather", seed, 2, x0, y0, w, h)
    for y in range(y0, y0 + h):
        row = (y - y0) % step
        for x in range(x0, x0 + w):
            if row == 0:
                face.set(x, y, k(role, 3))
            elif row == step - 1:
                face.set(x, y, k(role, 1))
            if row == step - 1 and (x + (y - y0) // step) % 4 == 1:
                face.set(x, y, lace)
