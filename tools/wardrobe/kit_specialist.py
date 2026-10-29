"""Specialist corps building blocks: the medic's cross armband, seal-tag trim, ink-stained cuffs, a
long coat's skirts, scroll tubes, light harness straps and blade bandoliers.

Kept to the shared roles so every piece mixes: P is the corps' coat, S its shirt or paper, A the
corps mark, L straps, M steel, K ink, D the trousers.
"""
from __future__ import annotations

from glyphs import stamp
from kit import arm_bone, arm_x
from paint import cap, fabric, k, rnd, solid, strip_fabric

# The medical corps' cross, drawn at double resolution on a half-scale patch. 6 x 6 texels.
CROSS = ["..##..",
         "..##..",
         "######",
         "######",
         "..##..",
         "..##.."]


def shirt(g, role: str = "S", texture: str = "weave", seed: int = 0, base: int = 2, arm_rows=(0, 11), cuff: str | None = None):
    """A plain long-sleeved shirt on the base body and arms, with an optional cuff band."""
    body = g.part("body")
    strip_fabric(body, role, texture, seed, base)
    cap(body, role, texture=texture, seed=seed, base=base)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, role, texture, seed + 1 + (side == "left"), base, *arm_rows)
        fabric(arm.top, role, texture, seed + 1, base + 1)
        if cuff:
            arm.strip.hline(0, arm.strip.w - 1, arm_rows[1], cuff)
    return body


def cross_armband(g, side: str = "left", y: float = .2, band: str = "P", mark: str | None = "A2", seed: int = 0, base: int = 3):
    """A cloth band round the upper arm with the medical cross on its outer face; `mark=None` leaves
    a plain duty band."""
    ring = g.piece(f"{side}_armband", arm_bone(side), (arm_x(side) - .45, y, -2.45), (5, 3, 5))
    solid(ring, band, "weave", seed, base, edge=False)
    for f in ring.sides:
        f.hline(0, f.w - 1, 0, k(band, base + 1)), f.hline(0, f.w - 1, 2, k(band, base - 1))
    if mark is None:
        return ring
    sign = 1 if side == "left" else -1
    patch = g.piece(f"{side}_cross", arm_bone(side), (0, 0, -3), (1, 6, 6),
                    pivot=(3.6 if sign > 0 else -4.1, y + .1, 0), scale=(.5, .5, .5))
    for f in patch.faces:
        f.fill(k(band, base + 1))
    stamp(patch.left if sign > 0 else patch.right, CROSS, 0, 0, {"#": mark})
    return ring


def seal_trim(face, y0: int, h: int, every: int = 3, paper: str = "S3", ink: str = "K1", seed: int = 0, start: int = 0):
    """Paper seal tags sewn along an edge: a cream strip every `every` texels, inked down the middle."""
    for x in range(start, face.w, every):
        for y in range(y0, y0 + h):
            face.set(x, y, paper)
        for y in range(y0 + 1, y0 + h - 1 if h > 2 else y0 + h):
            if rnd(x, y, seed) < .6:
                face.set(x, y, ink)


def ink_stains(face, seed: int, rows, density: float = .22, keys=("K1", "K2")):
    """Ink soaked into a cuff: dark blots that thin out up the sleeve."""
    rows = list(rows)
    for i, y in enumerate(rows):
        for x in range(face.w):
            if rnd(x, y, seed) < density * (1 + i / max(1, len(rows) - 1)):
                face.set(x, y, keys[int(rnd(y, x, seed + 1) * len(keys))])


def coat_skirts(g, prefix: str, length: int, role: str = "P", texture: str = "weave", seed: int = 0, hem: str | None = None,
                open_front: bool = True, top: float = 11.4, edge: str | None = None):
    """The skirts of a long coat below the waist: two front halves (or one closed front), the back
    and the sides, swinging with the stride. `edge` pipes the inner front edges."""
    fronts = ((f"{prefix}_front_right", -4.6, 3), (f"{prefix}_front_left", 1.6, 3)) if open_front else \
        ((f"{prefix}_front", -4.6, 9),)
    panels = [(n, x, w, -2.95, "flap_front") for n, x, w in fronts] + [(f"{prefix}_back", -4.6, 9, 1.95, "flap_back")]
    for i, (name, x0, w, z, motion) in enumerate(panels):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, length, 1), pivot=(x0, top, z), motion=motion)
        solid(skirt, role, texture, seed + i, 2)
        skirt.strip.hline(0, skirt.strip.w - 1, 0, k(role, 3))
        if hem:
            skirt.strip.hline(0, skirt.strip.w - 1, length - 1, hem)
            skirt.bottom.fill(hem)
        if edge and open_front and motion == "flap_front":
            skirt.front.vline(w - 1 if x0 < 0 else 0, 0, length - 1, edge)
    for name, x in ((f"{prefix}_right", -5.05), (f"{prefix}_left", 4.05)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, length - 1, 4), pivot=(x, top, 0))
        solid(panel, role, texture, seed + 7, 2)
        if hem:
            panel.strip.hline(0, panel.strip.w - 1, length - 2, hem)


def strap(g, pid: str, pivot, rz: float, length: int = 14, z: float = 0, role: str = "L", seed: int = 0):
    """A thin strap across the chest or back, rotated about the torso's depth axis."""
    box = g.piece(pid, "TORSO", (-.5, -length / 2, -.5), (1, length, 1), pivot=(pivot[0], pivot[1], z), rotation=(0, 0, rz))
    solid(box, role, "leather", seed, 2, edge=False)
    return box


def scroll_tube(g, pid: str, pivot, rotation=(0, 0, 0), length: int = 6, role: str = "L", end: str = "M3", bone: str = "TORSO",
                seed: int = 0, width: int = 2):
    """A capped message tube: a leather body along local +y, metal caps at both ends and a tie band."""
    tube = g.piece(pid, bone, (-width / 2, 0, -width / 2), (width, length, width), pivot=pivot, rotation=rotation)
    solid(tube, role, "leather", seed, 2, edge=False)
    for f in tube.sides:
        f.hline(0, f.w - 1, 0, end), f.hline(0, f.w - 1, length - 1, end)
        f.hline(0, f.w - 1, length // 2, k(role, 1))
    tube.top.fill(end), tube.bottom.fill(end)
    return tube


def bandolier(g, prefix: str, side: str = "right", face_z: float = -2.6, blades: int = 4, role: str = "L", seed: int = 0,
              back: bool = False):
    """A strap from one shoulder to the opposite hip holding a row of kunai, rings up, on the front
    (or the back) of the torso."""
    sign = -1 if side == "right" else 1
    rz = 38 * sign * (-1 if back else 1)
    z = face_z if not back else 2.6
    strap(g, f"{prefix}_strap", (0, 5.6), rz, 15, z, role, seed)
    import math
    for i in range(blades):
        t = (i - (blades - 1) / 2) * 2.6
        x = -math.sin(math.radians(rz)) * t
        y = 5.6 + math.cos(math.radians(rz)) * t
        dz = -.6 if not back else .6
        hilt = g.piece(f"{prefix}_kunai_{i}", "TORSO", (-.5, -1, -.5), (1, 3, 1), pivot=(x, y, z + dz), rotation=(0, 0, rz))
        solid(hilt, "K", "smooth", seed + 1 + i, 2, edge=False)
        for f in hilt.sides:
            f.set(0, 1, "S3")
        hilt.top.fill("M3")
        ring = g.piece(f"{prefix}_ring_{i}", "TORSO", (-.5, -2, -.5), (1, 1, 1), pivot=(x, y, z + dz), rotation=(0, 0, rz))
        for f in ring.faces:
            f.fill("M3")
