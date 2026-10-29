"""Household helpers: the everyday cloth of the village's homes, festivals and shrines.

Woven and dyed patterns (kasuri flecks, stripes, checks, ichimatsu, dots, sprigs), the kimono
overlap read as a lowercase y, short, long and wide sleeves, a sash with a back or side knot, and
the footwear of home life: tabi with zori, wooden geta, straw waraji, split-toe jika-tabi and soft
cloth shoes. Patterns take their keys from palette roles, so every civilian palette reads.
"""
from __future__ import annotations

from kit import arm_bone, arm_x, flaps, side_panels
from paint import fabric, k, rnd, solid, strip_fabric

SIDES = ("right", "left")


# -- patterns -----------------------------------------------------------------------------------
def kasuri(face, key: str, step: int = 3, seed: int = 0, rows=None):
    """Ikat flecks: short dashes in a staggered grid, the way splash-dyed thread blurs."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        if (y + seed) % step:
            continue
        shift = ((y + seed) // step) * 2
        for x in range(face.w):
            if (x + face.x0 + shift) % 5 in (0, 1):
                face.set(x, y, key)


def stripes(face, key: str, every: int = 3, offset: int = 0, rows=None):
    """Vertical stripes: one column of `key` every `every` texels, continuous around a strip."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        for x in range(face.w):
            if (x + face.x0 + offset) % every == 0:
                face.set(x, y, key)


def bands(face, key: str, every: int = 3, offset: int = 0, rows=None):
    """Horizontal stripes, for knits and play shirts."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        if (y + offset) % every == 0:
            face.hline(0, face.w - 1, y, key)


def checks(face, line: str, every: int = 4, offset: int = 0, cross: str | None = None, rows=None):
    """A woven check: lines both ways every `every` texels, a darker texel where they cross."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        for x in range(face.w):
            vx, hy = (x + face.x0 + offset) % every == 0, (y + offset) % every == 0
            if vx and hy and cross:
                face.set(x, y, cross)
            elif vx or hy:
                face.set(x, y, line)


def ichimatsu(face, key: str, size: int = 2, rows=None):
    """The checkerboard of alternating squares."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        for x in range(face.w):
            if ((x + face.x0) // size + y // size) % 2 == 0:
                face.set(x, y, key)


def dots(face, key: str, step: int = 4, seed: int = 0, rows=None):
    """Mizutama: round dots in a half-drop grid."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        for x in range(face.w):
            row = (y + seed) // step
            if (y + seed) % step == 1 and (x + face.x0 + (row % 2) * (step // 2)) % step == 1:
                face.set(x, y, key)


def sprigs(face, petal: str, heart: str, step: int = 5, seed: int = 0, rows=None, chance: float = 1.0):
    """Five-texel blossoms (a plus of petals round a heart) scattered in a half-drop grid."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        for x in range(face.w):
            row = (y + seed) // step
            gx = x + face.x0 + (row % 2) * (step // 2) + seed
            if (y + seed) % step == 2 and gx % step == 2 and rnd(gx // step, row, seed) < chance:
                for dx, dy in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                    if y + dy in rows:
                        face.set(x + dx, y + dy, petal)
                face.set(x, y, heart)


def trim(box, y: int, key: str, faces=("right", "front", "left", "back")):
    for name in faces:
        f = getattr(box, name)
        f.hline(0, f.w - 1, y, key)


# -- tops ---------------------------------------------------------------------------------------
# The overlap of a kimono worn correctly: the wearer's left panel over the right, so the front reads
# as a lowercase y. Front x runs from the wearer's right to left, so the long edge falls from the
# upper right of the face to the lower left.
EDGE = [(5, 0), (5, 1), (4, 2), (4, 3), (3, 4), (3, 5), (2, 6), (2, 7), (1, 8), (1, 9), (0, 10), (0, 11)]
UNDER = [(2, 0), (3, 1), (3, 2)]


def overlap(face, edge: str, shade: str | None = None, rows: int = 8, collar: str | None = None, under: str | None = None):
    """The y-shaped kimono front: the over-panel's edge down to row `rows`, a shadow beside it, the
    under-panel's short collar line and the inner collar (`under`) filling the V at the throat."""
    for x, y in EDGE[:rows]:
        face.set(x, y, edge)
        if shade and x - 1 >= 0:
            face.set(x - 1, y, shade)
    for x, y in UNDER:
        face.set(x, y, collar or edge)
    if under:
        face.set(3, 0, under), face.set(4, 0, under), face.set(4, 1, under)


def collar_band(face, key: str, rows: int = 8, width: int = 1):
    """A haori or happi lapel: a band either side of the opening from the shoulders down."""
    for y in range(rows):
        for w in range(width):
            face.set(w + 1, y, key), face.set(6 - w, y, key)


def arm_cloth(g, role: str, texture: str, seed: int, rows=(0, 4), base: int = 2, hem: str | None = None,
              overlay: bool = True, cuff: str | None = None):
    """Sleeves painted on both arms (and the sleeve overlay when `overlay`) from rows[0] to rows[1],
    with an optional hem line on the last row and a cuff key on the row below it."""
    boxes = []
    for side in SIDES:
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, role, texture, seed + (side == "left"), base, rows[0], rows[1])
        if rows[0] == 0:
            fabric(arm.top, role, texture, seed, base + 1)
        layers = [arm]
        if overlay:
            sleeve = g.part(f"{side}_sleeve")
            strip_fabric(sleeve, role, texture, seed + 2 + (side == "left"), base, rows[0], rows[1])
            if rows[0] == 0:
                fabric(sleeve.top, role, texture, seed + 2, base + 1)
            layers.append(sleeve)
        for box in layers:
            if hem:
                box.strip.hline(0, box.strip.w - 1, rows[1], hem)
            if cuff and rows[1] + 1 < box.h:
                box.strip.hline(0, box.strip.w - 1, rows[1] + 1, cuff)
        boxes.append(layers[-1])
    return boxes


def wide_sleeves(g, prefix: str, role: str, texture: str, seed: int, top: float = 2.4, length: int = 6,
                 depth: int = 5, base: int = 2, hem: str | None = None, pattern=None, arm_rows: int = 8,
                 inflate: float = .14, arm_role: str | None = None):
    """Loose kimono sleeves: arm cloth down to `arm_rows`, then a hanging box from the elbow.
    `pattern(face)` paints each outer side of the box."""
    out = []
    for side in SIDES:
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, arm_role or role, texture, seed + (side == "left"), base, 0, arm_rows)
        fabric(arm.top, arm_role or role, texture, seed, base + 1)
        strip_fabric(sleeve, role, texture, seed + 2, base, 0, 3)
        fabric(sleeve.top, role, texture, seed + 2, base + 1)
        if pattern:
            pattern(sleeve.strip, rows=range(0, 4))
        box = g.piece(f"{prefix}_{side}", arm_bone(side), (arm_x(side) - .5, top, -depth / 2), (5, length, depth),
                      inflate=inflate)
        solid(box, role, texture, seed + 3 + (side == "left"), base)
        if pattern:
            for face in box.sides:
                pattern(face)
        if hem:
            trim(box, length - 1, hem)
        box.bottom.fill(k(role, 0))
        out.append(box)
    return out


def sash(g, pid: str, role: str, y: float = 8.0, height: int = 2, knot: str | None = "back", seed: int = 0,
         stripe: str | None = None, inflate: float = .12, base: int = 2):
    """An obi or plain sash round the waist; `knot` is back (a flat tied bow with two ends),
    side (two ends hanging at the wearer's left hip), bow (a big butterfly bow at the back) or None."""
    box = g.piece(pid, "TORSO", (-4.6, y, -2.6), (9, height, 5), inflate=inflate)
    solid(box, role, "weave", seed, base, edge=False)
    for face in box.sides:
        face.hline(0, face.w - 1, 0, k(role, base + 1))
        if height > 2:
            face.hline(0, face.w - 1, height - 1, k(role, base - 1))
        if stripe:
            face.hline(0, face.w - 1, height // 2, stripe)
    if knot == "back":
        bow = g.piece(f"{pid}_knot", "TORSO", (-1.5, -1, 0), (3, 2, 1), pivot=(0, y + 1.2, 2.7))
        solid(bow, role, "weave", seed + 1, base + 1, edge=False)
        for i, x in enumerate((-.9, .2)):
            end = g.piece(f"{pid}_end_{i}", "TORSO", (0, 0, 0), (1, 3 - i, 1), pivot=(x, y + 1.6, 2.8), rotation=(6, 0, 0),
                          motion="sway")
            solid(end, role, "weave", seed + 2 + i, base)
    elif knot == "side":
        for i, (x, rz) in enumerate(((2.6, 6), (3.3, -8))):
            end = g.piece(f"{pid}_end_{i}", "TORSO", (-.5, 0, -.5), (1, 4 - i, 1), pivot=(x, y + height - .2, -2.8),
                          rotation=(0, 0, rz), motion="sway")
            solid(end, role, "weave", seed + 2 + i, base)
    elif knot == "bow":
        core = g.piece(f"{pid}_bow", "TORSO", (-1, -1, 0), (2, 2, 2), pivot=(0, y + height / 2, 2.6))
        solid(core, role, "weave", seed + 1, base, edge=False)
        for i, (sign, rz) in enumerate(((-1, 14), (1, -14))):
            wing = g.piece(f"{pid}_wing_{i}", "TORSO", (-2 if sign < 0 else 0, -1.5, 0), (2, 3, 1),
                           pivot=(sign * 1.0, y + height / 2, 3.1), rotation=(0, 0, rz))
            solid(wing, role, "weave", seed + 2 + i, base + 1, edge=False)
            for face in wing.sides:
                face.vline(0 if sign < 0 else 1, 0, 2, k(role, base - 1))
        for i, (x, rz) in enumerate(((-.6, 8), (.6, -8))):
            tail = g.piece(f"{pid}_tail_{i}", "TORSO", (-.5, 0, 0), (1, 4, 1), pivot=(x, y + height / 2 + .6, 3.2),
                           rotation=(4, 0, rz), motion="sway")
            solid(tail, role, "weave", seed + 4 + i, base)
    return box


def robe_skirt(g, prefix: str, length: int, role: str, texture: str, seed: int, hem: str | None = None, top: float = 10.6,
               pattern=None, overlap_key: str | None = None):
    """The skirt of a top that falls past the hips (a robe, a coat, a long haori): front and back
    panels a little proud of any bottom's own skirt, and side panels."""
    faces = flaps(g, prefix, length, role, texture, seed, width=9, hem=hem, top=top, front_z=-3.0, back_z=2.0)
    side_panels(g, f"{prefix}_side", length - 1, role, texture, hem=hem, top=top)
    for face in faces:
        if pattern:
            pattern(face, rows=range(1, length - (1 if hem else 0)))
        if overlap_key and face.name == "front":
            face.vline(3, 1, length - 1, overlap_key)
    return faces


# -- bottoms ------------------------------------------------------------------------------------
def waist(g, role: str, texture: str, seed: int, base: int = 2, rows=(9, 11), band: str | None = None):
    body = g.part("body")
    strip_fabric(body, role, texture, seed, base, rows[0], rows[1])
    fabric(body.bottom, role, texture, seed, base - 1)
    if band:
        body.strip.hline(0, body.strip.w - 1, rows[0], band)
    return body


def trouser_legs(g, role: str, texture: str, seed: int, rows=(0, 9), base: int = 2, crease: str | None = None):
    boxes = []
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, role, texture, seed + (side == "left"), base, rows[0], rows[1])
        if rows[0] == 0:
            fabric(leg.top, role, texture, seed, base)
        if crease:
            leg.front.vline(1 if side == "right" else 2, rows[0] + 1, rows[1], crease)
        boxes.append(leg)
    return boxes


def skirt(g, prefix: str, length: int, role: str, texture: str, seed: int, hem: str | None = None, top: float = 11.2,
          pattern=None, base: int = 2):
    """A skirt that follows the stride: front and back panels plus side panels; `pattern(face, rows)`
    paints the panels."""
    faces = flaps(g, prefix, length, role, texture, seed, width=9, hem=hem, top=top, base=base)
    side_panels(g, f"{prefix}_side", length, role, texture, hem=hem, top=top)
    if pattern:
        for face in faces:
            pattern(face, rows=range(1, length - (1 if hem else 0)))
    return faces


def socks(g, key: str, rows=(7, 9)):
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        for y in range(rows[0], rows[1] + 1):
            leg.strip.hline(0, leg.strip.w - 1, y, key)
        leg.strip.hline(0, leg.strip.w - 1, rows[0], k(key[0], int(key[1]) + 1))


def _soles(g, sole: str = "K1"):
    for side in SIDES:
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        leg.bottom.fill(sole)
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, sole)
        pants.bottom.fill("K0")


def zori(g, sock: str = "S3", strap: str = "A2", sole: str = "L3"):
    """White split-toe tabi in flat zori: the thong strap at the toe, a pale sole."""
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, sock[0], "plain", 37945, int(sock[1]), 10, 11)
        leg.front.vline(2, 10, 11, k(sock[0], int(sock[1]) - 1))
        leg.front.set(1, 10, strap), leg.front.set(2, 10, strap)
        leg.strip.hline(0, leg.strip.w - 1, 11, sole)
    _soles(g, sole)


def geta(g, strap: str = "A2", wood: str = "L3", bare: bool = True):
    """Wooden geta: bare toes, a cloth thong, a raised pale-wood block under the foot."""
    for side in SIDES:
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        leg.strip.hline(0, leg.strip.w - 1, 11, wood)
        leg.front.set(1, 10, strap), leg.front.set(2, 10, strap)
        leg.right.set(3, 10, strap), leg.left.set(0, 10, strap)
        leg.bottom.fill(k(wood[0], int(wood[1]) - 2))
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, k(wood[0], int(wood[1]) - 1))
        pants.front.hline(0, 3, 11, wood)
        pants.bottom.fill("K0")


def waraji(g, straw: str = "L4", tie: str = "L2"):
    """Straw sandals: a woven sole and cords crossing the instep and the ankle."""
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        leg.strip.hline(0, leg.strip.w - 1, 11, straw)
        leg.front.set(0, 10, tie), leg.front.set(3, 10, tie), leg.front.set(1, 11, tie)
        leg.right.set(1, 10, tie), leg.left.set(2, 10, tie)
        leg.back.hline(0, 3, 9, tie)
    _soles(g, "L1")


def jika_tabi(g, role: str = "K", top: int = 7, base: int = 2):
    """Split-toe work boots to mid-shin, fastened up the inside with small metal hooks."""
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, role, "smooth", 37946, base, top, 11)
        leg.strip.hline(0, leg.strip.w - 1, top, k(role, base + 1))
        leg.front.vline(2 if side == "right" else 1, 10, 11, k(role, base - 2))
        inner = leg.left if side == "right" else leg.right
        for y in range(top + 1, 11, 1):
            inner.set(1, y, "M3" if y % 2 else k(role, base - 1))
        leg.strip.hline(0, leg.strip.w - 1, 11, "K1")
    _soles(g)


def cloth_shoes(g, role: str = "K", base: int = 2, strap: str | None = None):
    """Soft cloth shoes (the house slipper or kung-fu shoe): a low upper, a pale sole edge."""
    for side in SIDES:
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, role, "plain", 37947, base, 10, 11)
        if strap:
            leg.front.hline(0, 3, 10, strap)
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, k(role, base - 1))
        pants.front.hline(0, 3, 11, k(role, base + 1))
        leg.strip.hline(0, leg.strip.w - 1, 11, "S2")
        leg.bottom.fill("K1"), pants.bottom.fill("K0")


# -- head -----------------------------------------------------------------------------------------
HALF = (.5, .5, .5)


def blossom(g, pid: str, pivot, rotation=(0, 0, 0), petal: str = "A3", heart: str = "S4", size: int = 5):
    """A folded-cloth blossom at half scale facing local -z: a square of petals with its corners
    clipped by shade, and a raised bright heart."""
    body = g.piece(pid, "HEAD", (-size / 2, -size / 2, -.5), (size, size, 1), pivot=pivot, rotation=rotation, scale=HALF)
    for f in body.faces:
        f.fill(petal)
    lo = k(petal[0], int(petal[1]) - 1)
    for f in (body.front, body.back):
        for x, y in ((0, 0), (size - 1, 0), (0, size - 1), (size - 1, size - 1)):
            f.set(x, y, lo)
        f.vline(size // 2, 0, size - 1, lo), f.hline(0, size - 1, size // 2, lo)
    centre = g.piece(f"{pid}_heart", "HEAD", (-.5, -.5, -1.3), (1, 1, 1), pivot=pivot, rotation=rotation, scale=HALF)
    for f in centre.faces:
        f.fill(heart)
    return body


def topknot(g, pid: str, pivot, size=(3, 2, 3), seed: int = 0, rotation=(0, 0, 0), tie: str | None = None):
    """A round knot of hair: a squat core with a narrower cap on top, the strands creased round it;
    an optional tie key binds its base."""
    from anime import cel_box
    w, h, d = size
    core = g.piece(pid, "HEAD", (-w / 2, -h / 2, -d / 2), size, pivot=pivot, rotation=rotation)
    cel_box(core, seed, ring=0, clump=2)
    cw, cd = max(1, w - 2), max(1, d - 2)
    top = g.piece(f"{pid}_cap", "HEAD", (-cw / 2, -h / 2 - 1, -cd / 2), (cw, 1, cd), pivot=pivot, rotation=rotation,
                  inflate=.3)
    cel_box(top, seed + 1, top_delta=1)
    if tie:
        band = g.piece(f"{pid}_tie", "HEAD", (-w / 2, h / 2 - .2, -d / 2), (w, 1, d), pivot=pivot, rotation=rotation,
                       inflate=.05)
        for f in band.faces:
            f.fill(tie)
    return core
