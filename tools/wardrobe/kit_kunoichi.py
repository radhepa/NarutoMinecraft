"""Kunoichi building blocks for the general wardrobe's kunoichi collection: a crossed wrap front, an
obi with a knot at the back, hanging kimono sleeves, arm warmers, frog buttons, a thigh holster and,
for hair, a rippling wave lock and a round bun. Every helper paints key colors only, so the pieces
take whichever palette the resident wears and mix with every other collection."""
from __future__ import annotations

from anime import cel_box
from kit import SIDES, arm_bone, arm_x, belt, leg_bone
from paint import fabric, k, solid, strip_fabric


# -- tops ------------------------------------------------------------------------------------
def wrap_front(face, role: str, rows: int = 7, base: int = 2, left_over_right: bool = True):
    """A crossed wrap closure on a body front: the outer panel's lit edge runs from the shoulder to
    the opposite hip, its shadow on the panel beneath."""
    for y in range(rows):
        x = 1 + y * 5 // max(1, rows - 1)
        x = x if left_over_right else 7 - x
        face.set(x, y, k(role, base + 1))
        face.set(x + (1 if left_over_right else -1), y, k(role, base - 1))


def obi(g, pid: str, y: float = 8.0, role: str = "A", height: int = 2, knot: str | None = "back", cord: str | None = None,
        seed: int = 0):
    """A wide sash round the waist with a flat knot at the back (or the side) and an optional cord."""
    box = belt(g, pid, y=y, role=role, height=height, buckle=None, inflate=.12)
    for face in box.sides:
        face.hline(0, face.w - 1, height - 1, k(role, 1))
    if cord:
        box.front.hline(0, 8, height // 2, cord)
        for face in (box.right, box.left, box.back):
            face.hline(0, face.w - 1, height // 2, cord)
    if knot == "back":
        bow = g.piece(f"{pid}_knot", "TORSO", (-2, 0, 0), (4, height + 1, 1), pivot=(0, y - .5, 2.65))
        solid(bow, role, "weave", seed, 2)
        bow.back.vline(1, 0, height, k(role, 1)), bow.back.vline(2, 0, height, k(role, 3))
    elif knot == "side":
        bow = g.piece(f"{pid}_knot", "TORSO", (-1, 0, -.5), (2, height, 1), pivot=(3.2, y, -2.9))
        solid(bow, role, "weave", seed, 3)
        for i, (x, rz) in enumerate(((2.8, 8), (3.6, -6))):
            tail = g.piece(f"{pid}_tail_{i}", "TORSO", (-.5, 0, -.5), (1, 4 - i, 1), pivot=(x, y + height, -2.9),
                           rotation=(0, 0, rz), motion="sway")
            solid(tail, role, "weave", seed + 1 + i, 2)
    return box


def kimono_sleeves(g, prefix: str, role: str, seed: int, length: int = 6, top: float = 1.0, trim: str | None = None,
                   texture: str = "weave"):
    """Wide hanging sleeves from the shoulder to below the elbow, open and deeper than the arm."""
    boxes = []
    for side in SIDES:
        box = g.piece(f"{prefix}_{side}", arm_bone(side), (arm_x(side) - .5, top - 2, -2.5), (5, length, 5), inflate=.05,
                      motion="none")
        solid(box, role, texture, seed + (side == "left"), 2)
        for face in box.sides:
            face.hline(0, face.w - 1, 0, k(role, 3))
            face.hline(0, face.w - 1, length - 1, trim or k(role, 1))
        box.bottom.fill(k(role, 0))
        boxes.append(box)
    return boxes


def arm_warmers(g, role: str, seed: int, rows=(6, 10), band: str | None = None, layer: str = "sleeve"):
    """Snug warmers from the elbow to the knuckles on the sleeve overlay, an optional band at the top."""
    for side in SIDES:
        box = g.part(f"{side}_{layer}")
        strip_fabric(box, role, "knit", seed + (side == "left"), 2, rows[0], rows[1])
        box.strip.hline(0, box.strip.w - 1, rows[1], k(role, 1))
        if band:
            box.strip.hline(0, box.strip.w - 1, rows[0], band)


def frog_buttons(face, points, key: str = "A3", loop: str = "A1"):
    """Chinese knot buttons: a bright knot with a darker loop beside it."""
    for x, y in points:
        face.set(x, y, key), face.set(x + 1, y, loop)


def mandarin_collar(g, pid: str, role: str, seed: int, y: float = -1.5, trim: str | None = None):
    """A narrow stand-up collar open at the front, the qipao's collar."""
    box = g.piece(pid, "TORSO", (-4.4, y, -2.55), (9, 2, 5), inflate=.04)
    solid(box, role, "smooth", seed, 2)
    box.front.set(4, 0, k(role, 0)), box.front.set(4, 1, k(role, 0))
    for face in box.sides:
        face.hline(0, face.w - 1, 0, trim or k(role, 3))
    return box


# -- bottoms ---------------------------------------------------------------------------------
def thigh_holster(g, pid: str = "holster", side: str = "right", y: float = 1.4, seed: int = 0):
    """A strapped kunai holster on the outer thigh."""
    sign = -1 if side == "right" else 1
    bone = leg_bone(side)
    strap = g.piece(f"{pid}_strap", bone, (-2.45, y, -2.45), (5, 1, 5))
    solid(strap, "L", "leather", seed, 2)
    box = g.piece(pid, bone, (0, 0, 0), (1, 3, 2), pivot=(2.0 * sign - (1 if sign < 0 else 0), y - .2, -1.0))
    solid(box, "K", "leather", seed + 1, 3)
    box.front.set(0, 0, "M3")
    return box


def shin_wrap(g, top: int, bottom: int, role: str = "S"):
    """Cloth wound round the shins on the base leg, turns leaning down to the front."""
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        for y in range(top, bottom + 1):
            for x in range(leg.strip.w):
                leg.strip.set(x, y, k(role, 2 if (x - y * 2) % 5 == 0 else 3))
        leg.strip.hline(0, leg.strip.w - 1, top, k(role, 4))


def tabi_boots(g, top: int = 7, role: str = "K", seed: int = 0):
    """Split-toe tabi boots, soft and snug to mid-shin, fastened with metal clasps up the back."""
    for side in SIDES:
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, role, "smooth", seed + (side == "left"), 2, top, 11)
        leg.front.vline(1, 10, 11, k(role, 0))
        leg.back.vline(1, top + 1, 10, "M3")
        for face in pants.sides:
            fabric(face, role, "smooth", seed + 2, 2, 0, top + 2, face.w, 10 - top)
            face.hline(0, face.w - 1, top + 2, k(role, 3))
            face.hline(0, face.w - 1, 11, "K0")
        pants.front.vline(1, 10, 11, k(role, 0))
        leg.bottom.fill("K1"), pants.bottom.fill("K0")


# -- hair ------------------------------------------------------------------------------------
def wave_lock(g, pid: str, pivot, rotation, segments, depth: int = 2, seed: int = 0, base: int = 2, amp: float = .5,
              phase: int = 0, motion: str = "sway"):
    """A long lock that ripples: each segment steps side to side as it falls, ending in a point."""
    y = 0.0
    for i, (w, h) in enumerate(segments):
        shift = amp if (i + phase) % 2 else -amp
        box = g.piece(f"{pid}_{i}", "HEAD", (-w / 2 + shift, y, -depth / 2), (w, h, depth), pivot=pivot, rotation=rotation,
                      motion=motion)
        cel_box(box, seed + i * 7, base, 1 if i == 0 else None, top_delta=1 if i == 0 else 0)
        y += h
    return y


def round_bun(g, pid: str, pivot, rotation=(0, 0, 0), size: int = 4, seed: int = 0, tie_key: str | None = None):
    """A round bun: a block with a smaller cap stacked on its face so it reads as a coil."""
    s = size
    bun = g.piece(pid, "HEAD", (-s / 2, -s / 2, 0), (s, s, s - 1), pivot=pivot, rotation=rotation)
    cel_box(bun, seed, ring=1)
    cap = g.piece(f"{pid}_coil", "HEAD", (-(s - 2) / 2, -(s - 2) / 2, s - 1), (s - 2, s - 2, 1), pivot=pivot, rotation=rotation)
    cel_box(cap, seed + 1, top_delta=1)
    if tie_key:
        band = g.piece(f"{pid}_tie", "HEAD", (-(s + 1) / 2, -(s + 1) / 2, -.6), (s + 1, s + 1, 1), pivot=pivot, rotation=rotation)
        for f in band.faces:
            f.fill(tie_key)
        for f in band.sides:
            f.hline(0, f.w - 1, 0, tie_key[0] + str(min(4, int(tie_key[1]) + 1)))
    return bun
