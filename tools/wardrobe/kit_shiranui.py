"""Shiranui building blocks: the senbon (a long steel throwing needle), the thigh and wrist holsters
that carry them, a needle bandolier painted across a torso, the backward bandana protector, the
needle held in the teeth, flicked-out hair ends and the clan's will-o'-the-wisp flame crest.

Every piece paints key colors only: needles in M, holsters and straps in L, bandana cloth in D, so a
palette decides how a family's kit looks."""
from anime import lock
from glyphs import stamp
from kit_shinobi import protector_plate
from paint import fabric, k, solid

# The shiranui, the sea-fire: a teardrop flame with a curl, at double resolution on a half-scale
# decal (8 x 8 texels).
FLAME = ["...#....",
         "...##...",
         "..##..#.",
         ".##..##.",
         ".#..###.",
         ".#...##.",
         "..#..#..",
         "...##..."]


def senbon(g, pid: str, bone: str, pivot, rotation=(0, 0, 0), length: int = 9, scale: float = 1 / 3, y0: float = 0.0):
    """One senbon at a third of a pixel thick, running along local +y from the pivot: a dark grip
    texel at the root, bright steel along the shaft, a highlit point."""
    box = g.piece(pid, bone, (-.5, y0, -.5), (1, length, 1), pivot=pivot, rotation=rotation, scale=(scale, scale, scale))
    for f in box.faces:
        f.fill("M3")
    for f in box.sides:
        f.set(0, 0, "K2"), f.set(0, length - 1, "M4")
    box.bottom.fill("M4"), box.top.fill("K2")
    return box


def thigh_holster(g, side: str = "right", seed: int = 16900, needles: int = 3, role: str = "L", y: float = 0.0):
    """A holster strapped to the outer thigh, a fan of senbon points standing out of its mouth;
    `y` lowers it, to sit below a skirt."""
    bone = "RIGHT_LEG" if side == "right" else "LEFT_LEG"
    sign = -1 if side == "right" else 1
    strap = g.piece(f"{side}_holster_strap", bone, (-2.45, 1.0 + y, -2.45), (5, 1, 5))
    solid(strap, role, "leather", seed, 2)
    holster = g.piece(f"{side}_holster", bone, (-.5, 0, -1), (1, 4, 2), pivot=(2.5 * sign, .6 + y, -.2))
    solid(holster, role, "leather", seed + 1, 2)
    for f in holster.sides:
        f.hline(0, f.w - 1, 0, k(role, 3))
    outer = holster.right if side == "right" else holster.left
    outer.set(0, 2, "M3"), outer.set(1, 2, "M3")
    for i in range(needles):
        senbon(g, f"{side}_holster_needle_{i}", bone, (2.5 * sign, .9 + y, -.8 + i * .55), (0, 0, 180 + sign * (6 - i * 4)),
               length=6)


def wrist_holster(g, side: str, seed: int = 16910, y: float = 7.0, role: str = "L", needles: int = 3):
    """A leather cuff on the forearm with senbon slotted along its outer face, points to the elbow."""
    bone = "RIGHT_ARM" if side == "right" else "LEFT_ARM"
    x0 = -3.0 if side == "right" else -1.0
    cuff = g.piece(f"{side}_needle_cuff", bone, (x0 - .4, y, -2.4), (5, 3, 5))
    solid(cuff, role, "leather", seed + (side == "left"), 2)
    for f in cuff.sides:
        f.hline(0, f.w - 1, 0, k(role, 3))
    outer_x = x0 - .5 if side == "right" else x0 + 4.5
    for i in range(needles):
        senbon(g, f"{side}_cuff_needle_{i}", bone, (outer_x, y + 2.8, -.9 + i * .9), (0, 0, 180), length=15)


def bandolier(face, role: str = "L", base: int = 2, mirror: bool = False, rows: int = 11, x0: int = 0):
    """A two-texel strap from one shoulder to the other hip, a steel needle head every other row."""
    w = face.w
    for y in range(rows):
        x = x0 + round(y * (w - 2 - x0) / (rows - 1))
        a, b = (w - 1 - x, w - 2 - x) if mirror else (x, x + 1)
        face.set(a, y, k(role, base + 1)), face.set(b, y, k(role, base - 1))
        if y % 2 == 1:
            face.set(a, y, "M4")


def crest(g, pid: str, pivot, bone: str = "TORSO", role: str = "P", base: int = 2, mark: str = "A3", face: str = "back"):
    """The flame crest on a half-scale plate one texel deep (4 x 4 model pixels)."""
    z0 = 0 if face == "back" else -1
    plate = g.piece(pid, bone, (-4, -4, z0), (8, 8, 1), pivot=pivot, scale=(.5, .5, .5))
    for f in plate.faces:
        fabric(f, role, "plain", 16901, base)
    stamp(getattr(plate, face), FLAME if face == "back" else [r[::-1] for r in FLAME], 0, 0, {"#": mark})
    return plate


def backward_bandana(g, role: str = "D", seed: int = 16920):
    """The forehead protector worn as a bandana turned backwards: the cloth tied over the crown with
    the steel plate riding on the back of the head and the knot sitting up on the brow."""
    cap = g.piece("bandana", "HEAD", (-4, -8, -4), (8, 2, 8), inflate=.62)
    solid(cap, role, "weave", seed, 2, edge=False)
    fabric(cap.top, role, "weave", seed, 3)
    cap.front.hline(0, 7, 1, k(role, 1))
    band = g.piece("bandana_band", "HEAD", (-4, -6, 2), (8, 1, 2), inflate=.62)
    solid(band, role, "weave", seed + 1, 1)
    plate = g.piece("plate", "HEAD", (-9, -4, 0), (18, 8, 2), pivot=(0, -6.6, 4.62), scale=(1 / 3, 1 / 3, 1 / 3))
    for f in plate.faces:
        fabric(f, "M", "plain", seed + 2, 2)
    protector_plate(plate.back)
    knot = g.piece("bandana_knot", "HEAD", (-1, -1, -1), (2, 2, 1), pivot=(.6, -7.4, -4.7))
    solid(knot, role, "weave", seed + 3, 3)
    for i, (x, rz) in enumerate(((-.3, 78), (1.5, -78))):
        end = g.piece(f"bandana_end_{i}", "HEAD", (-.5, 0, -.5), (1, 3, 1), pivot=(x, -7.2, -4.8), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, role, "weave", seed + 4 + i, 2)


def mouth_senbon(g, pid: str = "mouth_senbon"):
    """A senbon held idly in the corner of the mouth, tilted down and out to the left."""
    senbon(g, pid, "HEAD", (.3, -1.35, -4.25), (0, 30, -76), length=12)


def flicks(g, prefix: str, y: float, seed: int, x: float = 4.3, z: float = -2.4, segments=((2, 2), (1, 2)), splay: float = 30,
           back: bool = False):
    """A pair of hair ends flicking outward, one each side, from height `y` (continuing a fall)."""
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"{prefix}_{side}", (x * sign, y, z), (-14 if not back else 14, 0, -splay * sign), segments, 1,
             seed + (sign > 0) * 17, ring=None)
