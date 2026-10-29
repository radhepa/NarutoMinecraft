"""Hagane building blocks: riveted steel plates, plated bracers and shin guards, the gate guard's
mace slung on a leather harness, and a crown of stiff spikes for the clan's scrappy dark hair."""
from __future__ import annotations

from anime import spike
from kit import SIDES, arm_x, arm_bone, leg_bone
from paint import fabric, k, solid


def plate(face, x0: int, y0: int, w: int, h: int, role: str = "M", base: int = 2, rivets: bool = True):
    """A steel plate on a face rectangle: lit top edge, shaded lower edge and side, corner rivets."""
    fabric(face, role, "plain", 21000 + face.x0, base, x0, y0, w, h)
    face.hline(x0, x0 + w - 1, y0, k(role, base + 2))
    if h > 2:
        face.hline(x0, x0 + w - 1, y0 + h - 1, k(role, base - 1))
    if w > 2:
        face.vline(x0 + w - 1, y0 + 1, y0 + h - 1, k(role, base - 1))
    if rivets and w >= 3 and h >= 3:
        for x in (x0, x0 + w - 1):
            face.set(x, y0 + 1, k(role, base + 2))
            face.set(x, y0 + h - 2, k(role, base - 1))


def bracers(g, top: float = 6.0, height: int = 4, seed: int = 21010, strap: str = "L", inflate: float = 0):
    """Steel-plated bracers round each forearm: a plate on every side and a leather strap at the wrist."""
    out = []
    for side in SIDES:
        box = g.piece(f"{side}_bracer", arm_bone(side), (arm_x(side) - .5, top, -2.5), (5, height, 5), inflate=inflate)
        solid(box, "M", "plain", seed + (side == "left"), 2)
        for face in box.sides:
            plate(face, 0, 0, face.w, height - 1)
            face.hline(0, face.w - 1, height - 1, k(strap, 2))
            face.set(face.w // 2, height - 1, "M3")
        out.append(box)
    return out


def shin_guards(g, top: float = 5.0, height: int = 5, seed: int = 21030, strap: str = "K"):
    """Steel shin guards strapped over the lower leg: a riveted plate down the front and sides, two
    straps round the calf behind."""
    out = []
    for side in SIDES:
        box = g.piece(f"{side}_shin_guard", leg_bone(side), (-2.5, top, -2.5), (5, height, 5))
        solid(box, "M", "plain", seed + (side == "left"), 2)
        for face in (box.front, box.right, box.left):
            plate(face, 0, 0, face.w, height)
        box.front.vline(2, 1, height - 2, "M3")
        fabric(box.back, strap, "smooth", seed + 2, 2)
        for y in (1, height - 2):
            box.back.hline(0, box.back.w - 1, y, k(strap, 1))
            box.right.set(4, y, k(strap, 1)), box.left.set(0, y, k(strap, 1))
        out.append(box)
    return out


def mace(g, prefix: str = "mace", pivot=(1.2, 6.0, 3.1), rotation=(0, 0, 52), handle: int = 9, seed: int = 21050):
    """The clan's iron mace on the back: a leather-gripped haft and a flanged steel head above the
    shoulder, studded, with a rust-red cord at the pommel."""
    haft = g.piece(f"{prefix}_haft", "TORSO", (-.5, -handle + 3, -.5), (1, handle, 1), pivot=pivot, rotation=rotation)
    solid(haft, "L", "leather", seed, 2)
    for face in haft.sides:
        for y in range(handle - 4, handle):
            face.set(0, y, "K2" if y % 2 else "L3")
    head = g.piece(f"{prefix}_head", "TORSO", (-1.5, -handle - 1, -1.5), (3, 4, 3), pivot=pivot, rotation=rotation)
    solid(head, "M", "plain", seed + 1, 2)
    for face in head.sides:
        plate(face, 0, 0, 3, 4, rivets=False)
        face.set(1, 1, "M4"), face.set(1, 2, "K1")
    for i, (x, z) in enumerate(((-2, 0), (1, 0))):
        flange = g.piece(f"{prefix}_flange_{i}", "TORSO", (x, -handle - .5, -.5), (1, 3, 1), pivot=pivot, rotation=rotation)
        solid(flange, "M", "plain", seed + 2 + i, 3)
    cord = g.piece(f"{prefix}_cord", "TORSO", (-.5, 3, -.5), (1, 2, 1), pivot=pivot, rotation=rotation)
    solid(cord, "A", "weave", seed + 4, 2)


def harness(g, prefix: str = "harness", seed: int = 21060, role: str = "L"):
    """The leather baldric the mace hangs from: over the left shoulder, across the chest to the right
    hip, a steel ring at the breast."""
    front = g.piece(f"{prefix}_front", "TORSO", (-.5, -7, -.5), (1, 14, 1), pivot=(0, 5.2, -2.6), rotation=(0, 0, 36))
    solid(front, role, "leather", seed, 2)
    back = g.piece(f"{prefix}_back", "TORSO", (-.5, -7, -.5), (1, 14, 1), pivot=(0, 5.2, 2.6), rotation=(0, 0, 36))
    solid(back, role, "leather", seed + 1, 2)
    ring = g.piece(f"{prefix}_ring", "TORSO", (-1, -1, -.5), (2, 2, 1), pivot=(.9, 3.9, -3.0))
    solid(ring, "M", "plain", seed + 2, 3, edge=False)
    ring.front.set(1, 1, "K1")


def crown(g, prefix: str, specs, seed: int, depth: int = 2, y: float = -7.7, base: int = 2):
    """Stiff spikes standing off the crown: specs are (x, z, segments, tilt x, tilt z); negative tilt
    x leans back, positive tilt z leans to the character's left."""
    for i, (x, z, segs, rx, rz) in enumerate(specs):
        spike(g, f"{prefix}_{i}", (x, y, z), (rx, 0, rz), segs, depth, seed + i * 3, base)
