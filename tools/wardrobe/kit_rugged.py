"""Rugged building blocks for the wilderness shinobi of the general wardrobe: shaggy fur, forest
camouflage, patches and darns, twisted rope, ragged hems, shin guards, straw sandals and tabi, capes,
and rope-like dreadlocks for the hair."""
from __future__ import annotations

from anime import cel_box
from kit import SIDES, leg_bone
from paint import fabric, k, rnd, solid, strip_fabric


# -- cloth -----------------------------------------------------------------------------------
def shag_face(face, role: str = "S", seed: int = 0, base: int = 2):
    """Shaggy fur: staggered clumps with lit tips, shaded roots and a darker lower edge."""
    for y in range(face.h):
        for x in range(face.w):
            clump = (x + int(rnd(x // 2, 5, seed) * 3)) % 3
            s = base + (1 if clump == 1 else 0) - (1 if clump == 0 and rnd(x, y, seed) < .55 else 0)
            if y == 0 and rnd(x, 13, seed) < .5:
                s += 1
            if y == face.h - 1 and face.h > 1:
                s -= 1
            face.set(x, y, k(role, s))


def shag_box(box, role: str = "S", seed: int = 0, base: int = 2):
    """A cuboid of fur on every face: lit top, shaded underside."""
    for f in box.sides:
        shag_face(f, role, seed + f.x0, base)
    shag_face(box.top, role, seed + 1, base + 1)
    box.bottom.fill(k(role, base - 1))
    return box


def camo(face, seed: int, x0: int = 0, y0: int = 0, w: int | None = None, h: int | None = None,
         keys=("L2", "K3", "P3")):
    """Forest camouflage: soft blotches of each key scattered over the cloth already painted."""
    w = face.w - x0 if w is None else w
    h = face.h - y0 if h is None else h
    for y in range(y0, y0 + h):
        for x in range(x0, x0 + w):
            gx, gy = x + face.x0, y + face.y0
            # Blotches are cells of 3x2 texels, each cell tinted by one key or left as the ground.
            v = rnd(gx // 3, gy // 2, seed)
            edge = rnd(gx, gy, seed + 1)
            for i, key in enumerate(keys):
                if .18 * i <= v < .18 * i + .14 and edge > .2:
                    face.set(x, y, key)


def patch(face, x: int, y: int, w: int, h: int, role: str, seed: int = 0, base: int = 2):
    """A darned-on patch of another cloth with stitched corners."""
    fabric(face, role, "weave", seed, base, x, y, w, h)
    for cx, cy in ((x, y), (x + w - 1, y), (x, y + h - 1), (x + w - 1, y + h - 1)):
        face.set(cx, cy, k(role, base - 1))


def ragged(face, y: int, seed: int = 0, chance: float = .45):
    """Fray a hem: knock texels out of row y (and a few of the row above) so the edge reads torn."""
    for x in range(face.w):
        if rnd(x, y, seed) < chance:
            face.set(x, y, None)
            if rnd(x, y - 1, seed + 3) < .25:
                face.set(x, y - 1, None)


def rope_face(face, role: str = "S", base: int = 2):
    """Twisted rope: light and dark diagonal strands."""
    for y in range(face.h):
        for x in range(face.w):
            face.set(x, y, k(role, base + (1 if (x + y) % 3 == 0 else -1 if (x + y) % 3 == 2 else 0)))


def rope(g, pid: str, y: float = 9.5, role: str = "S", base: int = 2, knot: bool = True, inflate: float = .1):
    """A twisted rope belt round the waist, knotted at the front left with two short ends."""
    box = g.piece(pid, "TORSO", (-4.5, y, -2.5), (9, 1, 5), inflate=inflate)
    for f in box.faces:
        rope_face(f, role, base)
    if knot:
        kb = g.piece(f"{pid}_knot", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(1.0, y - .3, -3.0))
        for f in kb.faces:
            rope_face(f, role, base + 1)
        for i, (x, rz) in enumerate(((1.4, 10), (2.4, -12))):
            end = g.piece(f"{pid}_end_{i}", "TORSO", (-.5, 0, -.5), (1, 3 - i, 1), pivot=(x, y + 1.6, -3.0),
                          rotation=(0, 0, rz), motion="flap_front")
            for f in end.faces:
                rope_face(f, role, base)
    return box


def cape(g, pid: str, width: int, length: int, top: float, role: str = "P", texture: str = "twill", seed: int = 0,
         z: float = 2.5, folds: int = 3, hem: str | None = None, tear: bool = False):
    """A cloth panel hanging down the back from the shoulders, with fold lines and an optional hem."""
    back = g.piece(pid, "TORSO", (-width / 2, 0, 0), (width, length, 1), pivot=(0, top, z), motion="flap_back")
    solid(back, role, texture, seed, 2)
    face = back.back
    for x in range(1, face.w - 1, folds):
        face.vline(x, 2, face.h - 1, k(role, 1))
    face.hline(0, face.w - 1, 0, k(role, 3))
    if hem:
        face.hline(0, face.w - 1, length - 1, hem)
    if tear:
        # A worn hem: a broken dark edge over the last two rows.
        for f in (back.back, back.front):
            for x in range(f.w):
                f.set(x, length - 1, k(role, 0 if rnd(x, 1, seed) < .5 else 1))
                if rnd(x, 2, seed) < .3:
                    f.set(x, length - 2, k(role, 0))
    return back


# -- legs and feet ---------------------------------------------------------------------------
def leg_wraps(g, top: int, bottom: int, role: str = "S", base: int = 3):
    """Cloth strips wound round the lower legs on the skin layer, turns slanting across the shin."""
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        for y in range(top, bottom + 1):
            for x in range(leg.strip.w):
                leg.strip.set(x, y, k(role, base - 1) if (x + y * 2) % 5 == 0 else k(role, base))


def shin_guard(g, prefix: str, role: str = "L", seed: int = 0, top: float = 5.0, length: int = 4, strap: str = "K2",
               knee: bool = False, texture: str = "leather"):
    """A plate strapped over the front of each shin, with two straps round the calf and an optional knee cap."""
    out = []
    for side in SIDES:
        bone = leg_bone(side)
        plate = g.piece(f"{prefix}_{side}", bone, (-2, top, -2.75), (4, length, 1), inflate=.05)
        solid(plate, role, texture, seed + (side == "left"), 2)
        plate.front.hline(0, 3, 0, k(role, 3))
        plate.front.vline(1, 1, length - 2, k(role, 3)), plate.front.vline(2, 1, length - 2, k(role, 1))
        for i, y in enumerate((top + .6, top + length - 1.4)):
            band = g.piece(f"{prefix}_{side}_strap_{i}", bone, (-2, y, -2), (4, 1, 4), inflate=.3)
            for f in band.faces:
                f.fill(strap)
        if knee:
            cap = g.piece(f"{prefix}_{side}_knee", bone, (-1.5, top - 2.2, -2.85), (3, 2, 1), inflate=.05)
            solid(cap, role, texture, seed + 3, 3)
        out.append(plate)
    return out


def straw_sandals(g, strap: str = "L2", sole: str = "S1"):
    """Waraji: woven straw soles tied on with dark cords crossing over the bare foot."""
    for side in SIDES:
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        leg.front.set(1, 10, strap), leg.front.set(2, 10, strap)
        leg.right.set(3, 10, strap), leg.left.set(0, 10, strap)
        leg.strip.hline(0, leg.strip.w - 1, 11, sole)
        leg.front.set(1, 11, None), leg.front.set(2, 11, None)
        leg.bottom.fill(sole)
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, sole)
        pants.front.set(1, 11, None), pants.front.set(2, 11, None)
        pants.bottom.fill("K0")


def tabi(g, role: str = "S", base: int = 3, rows=(9, 11), sole: str = "K1", thong: str = "L1"):
    """Split-toe socks on the skin layer, a thong strap and a dark sole."""
    for side in SIDES:
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, role, "plain", 35990, base, rows[0], rows[1])
        leg.front.vline(2, rows[1] - 1, rows[1], k(role, base - 2))
        leg.front.set(1, rows[1] - 1, thong), leg.front.set(2, rows[1] - 1, thong)
        leg.bottom.fill(sole)
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, sole)
        pants.bottom.fill("K0")


def soft_boots(g, top: int = 7, role: str = "L", base: int = 2, laces: str | None = None):
    """Soft leather boots to the calf, with optional crossed lacing up the front."""
    for side in SIDES:
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, role, "leather", 35991, base, top, 11)
        leg.strip.hline(0, leg.strip.w - 1, top, k(role, base + 1))
        leg.strip.hline(0, leg.strip.w - 1, 11, "K1")
        leg.bottom.fill("K1")
        if laces:
            # Ladder lacing: a cord across the front every other row, the eyelet edges shaded.
            leg.front.vline(0, top + 1, 9, k(role, base - 1)), leg.front.vline(3, top + 1, 9, k(role, base - 1))
            for y in range(top + 1, 10, 2):
                leg.front.set(1, y, laces), leg.front.set(2, y, laces)
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, "K1")
        pants.bottom.fill("K0")


def baggy_legs(g, prefix: str, role: str = "P", seed: int = 0, top: float = 0.0, length: int = 9, flare: float = 3,
               width: int = 5, folds: bool = True, texture: str = "twill"):
    """Loose trouser legs: one wide box per leg splaying a little outward, with vertical drape folds."""
    out = []
    for side, sign in (("right", -1), ("left", 1)):
        box = g.piece(f"{prefix}_{side}", leg_bone(side), (-width / 2, 0, -width / 2), (width, length, width),
                      pivot=(0, top, 0), rotation=(0, 0, -flare * sign), inflate=.1)
        solid(box, role, texture, seed + (sign > 0), 2)
        if folds:
            for face in box.sides:
                for x in range(1, face.w, 2):
                    face.vline(x, 2, face.h - 2, k(role, 1))
                face.hline(0, face.w - 1, 0, k(role, 3))
        box.bottom.fill(k(role, 0))
        out.append(box)
    return out


# -- hair ------------------------------------------------------------------------------------
def rope_hair(box, seed: int, base: int = 2):
    """A dreadlock segment: twisted rope strands in hair keys, a lit top and dark underside."""
    for f in box.sides:
        for y in range(f.h):
            for x in range(f.w):
                s = base + (1 if (x + y + seed) % 3 == 0 else -1 if (x + y + seed) % 3 == 2 else 0)
                f.set(x, y, k("H", s))
    box.top.fill(k("H", base + 1))
    box.bottom.fill(k("H", base - 1))


def dread(g, pid: str, pivot, rotation=(0, 0, 0), length: int = 8, width: int = 2, seed: int = 0, base: int = 2,
          motion: str = "sway", tie: str | None = None, tie_at: int | None = None):
    """A rope-like dreadlock hanging along local +y in 2-texel links, thinning to a blunt tip, with an
    optional cloth or bead tie partway down."""
    y = 0.0
    links = max(1, length // 2)
    for i in range(links):
        w = width if i < links - 1 else max(1, width - 1)
        box = g.piece(f"{pid}_{i}", "HEAD", (-w / 2, y, -w / 2), (w, 2, w), pivot=pivot, rotation=rotation, motion=motion)
        rope_hair(box, seed + i, base - (1 if i == links - 1 else 0))
        if tie and tie_at == i:
            band = g.piece(f"{pid}_tie", "HEAD", (-w / 2, y + .5, -w / 2), (w, 1, w), pivot=pivot, rotation=rotation,
                           motion=motion, inflate=.2)
            for f in band.faces:
                f.fill(tie)
        y += 2
    return y


def knot_bun(g, pid: str, pivot, rotation=(0, 0, 0), size=(3, 3, 3), seed: int = 0, base: int = 2):
    """A round bun of hair: a cel-shaded box with a crossing wrap line on the sides."""
    w, h, d = size
    box = g.piece(pid, "HEAD", (-w / 2, -h, -d / 2), size, pivot=pivot, rotation=rotation)
    cel_box(box, seed, base, top_delta=1)
    for f in box.sides:
        for x in range(f.w):
            f.set(x, (x + 1) % f.h, k("H", base - 1))
    return box
