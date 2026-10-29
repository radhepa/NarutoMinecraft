"""Kinoshita clan building blocks: the carpenter family's tools (a pull saw, chisels, the carpenter's
square, a wooden mallet), the leather nail pouches of a tool belt, sashiko running stitch on indigo
work-cloth, split-toe jika-tabi and the clan crest, a carpenter's square inside a ring."""
from glyphs import stamp
from paint import fabric, k, rnd, solid

SIDES = ("right", "left")

# The Kinoshita crest at double resolution: a ring round a carpenter's square, the long arm down
# the left and the short arm along the foot, with a square-cut peg in the open corner.
CREST = ["....####....",
         "..##....##..",
         ".#........#.",
         ".#.##.....#.",
         "#..##..#...#",
         "#..##.###..#",
         "#..##..#...#",
         "#..######..#",
         ".#.######.#.",
         ".#........#.",
         "..##....##..",
         "....####...."]


def crest(face, x0: int, y0: int, key: str, ground: str | None = None):
    if ground:
        for y in range(12):
            for x in range(12):
                face.set(x0 + x, y0 + y, ground)
    stamp(face, CREST, x0, y0, {"#": key})


def back_crest(g, role: str, key: str, seed: int, y: float = 1.6, z: float = 2.3, pid: str = "back_crest"):
    """The crest on a cloth patch across the shoulder blades, at double resolution."""
    patch = g.piece(pid, "TORSO", (-6, 0, 0), (12, 12, 1), pivot=(0, y, z), scale=(.5, .5, .5))
    fabric(patch.back, role, "weave", seed, 2)
    crest(patch.back, 0, 0, key)
    for face in (patch.top, patch.bottom, patch.right, patch.left, patch.front):
        face.fill(f"{role}2")
    return patch


def sashiko(face, key: str, x0: int = 0, y0: int = 0, w: int | None = None, h: int | None = None, step: int = 2):
    """Running stitch quilted through work-cloth: two-texel dashes in `key` on every `step`th row,
    offset row to row, the way indigo jackets are reinforced at the shoulders and hem."""
    w = face.w - x0 if w is None else w
    h = face.h - y0 if h is None else h
    for y in range(y0, y0 + h):
        if (y - y0) % step:
            continue
        for x in range(x0, x0 + w):
            if (x + (y - y0) // step) % 3 != 2:
                face.set(x, y, key)


def wood_grain(face, role: str = "L", seed: int = 0, base: int = 2):
    """Planed timber: long wavy grain lines down the face and the odd knot."""
    for y in range(face.h):
        for x in range(face.w):
            s = base
            if (x + int(rnd(y // 3, x, seed) * 1.6)) % 3 == 0:
                s -= 1
            elif rnd(x, y, seed + 1) > .97:
                s += 1
            face.set(x, y, k(role, s))


def _piece(g, pid, bone, origin, size, pivot, rotation, scale=None, motion="none"):
    return g.piece(pid, bone, origin, size, pivot=pivot, rotation=rotation, scale=scale, motion=motion)


def saw(g, pid: str, pivot, rotation=(0, 0, 0), bone: str = "TORSO", length: int = 10, motion: str = "none"):
    """A ryoba pull saw drawn at double resolution: a cane-wrapped handle above the pivot and a thin
    steel blade below it, toothed on both edges."""
    s = (.5, .5, .5)
    handle = _piece(g, f"{pid}_handle", bone, (-1, -8, -1), (2, 8, 2), pivot, rotation, s, motion)
    solid(handle, "L", "smooth", 22901, 3, edge=False)
    for face in handle.sides:
        for y in range(0, 8, 2):
            face.set(0, y, "L1"), face.set(1, y + 1, "L1")
    blade = _piece(g, f"{pid}_blade", bone, (-2, 0, -.5), (4, length, 1), pivot, rotation, s, motion)
    solid(blade, "M", "plain", 22902, 3, edge=False)
    for face in (blade.front, blade.back):
        face.vline(0, 0, length - 1, "M1"), face.vline(3, 0, length - 1, "M1")
        for y in range(0, length, 2):
            face.set(0, y, "M4"), face.set(3, y + 1 if y + 1 < length else y, "M4")
        face.hline(1, 2, 0, "M2")
    return handle, blade


def chisel(g, pid: str, pivot, rotation=(0, 0, 0), bone: str = "TORSO", motion: str = "none"):
    """A nomi chisel at double resolution: an oak handle with a steel hoop and a short bright blade."""
    s = (.5, .5, .5)
    handle = _piece(g, f"{pid}_handle", bone, (-1, -5, -1), (2, 5, 2), pivot, rotation, s, motion)
    solid(handle, "L", "smooth", 22903, 3, edge=False)
    for face in handle.sides:
        face.hline(0, 1, 0, "M3")
    blade = _piece(g, f"{pid}_blade", bone, (-.5, 0, -.5), (1, 4, 1), pivot, rotation, s, motion)
    solid(blade, "M", "plain", 22904, 3, edge=False)
    for face in blade.sides:
        face.set(0, 3, "M4")
    return handle, blade


def square(g, pid: str, pivot, rotation=(0, 0, 0), bone: str = "TORSO", long: int = 14, short: int = 8):
    """The sashigane, the carpenter's steel square, at double resolution: a long and a short arm meeting
    at the corner below the pivot, ticked with graduations."""
    s = (.5, .5, .5)
    arm = _piece(g, f"{pid}_long", bone, (-1, 0, -.5), (2, long, 1), pivot, rotation, s)
    foot = _piece(g, f"{pid}_short", bone, (1, long - 2, -.5), (short, 2, 1), pivot, rotation, s)
    for box in (arm, foot):
        solid(box, "M", "plain", 22905, 3, edge=False)
    for face in (arm.front, arm.back):
        for y in range(1, long, 2):
            face.set(0, y, "M1")
    for face in (foot.front, foot.back):
        for x in range(1, short, 2):
            face.set(x, 0, "M1")
    return arm, foot


def mallet(g, pid: str, pivot, rotation=(0, 0, 0), bone: str = "TORSO", motion: str = "none"):
    """A kizuchi, the carpenter's wooden mallet: a long handle below the pivot and a barrel head of
    pale oak above it, banded at both faces."""
    s = (.5, .5, .5)
    head = _piece(g, f"{pid}_head", bone, (-3, -3, -1.5), (6, 3, 3), pivot, rotation, s, motion)
    solid(head, "S", "smooth", 22906, 2, edge=False)
    for face in head.sides:
        face.vline(0, 0, 2, "L1"), face.vline(face.w - 1, 0, 2, "L1")
    wood_grain(head.front, "S", 22906), wood_grain(head.back, "S", 22907)
    for face in (head.front, head.back):
        face.vline(0, 0, 2, "L1"), face.vline(5, 0, 2, "L1")
    handle = _piece(g, f"{pid}_handle", bone, (-.5, 0, -.5), (1, 9, 1), pivot, rotation, s, motion)
    solid(handle, "L", "smooth", 22908, 3, edge=False)
    return head, handle


def nail_pouch(g, pid: str, pivot, bone: str = "TORSO", size=(2, 3, 2), rotation=(0, 0, 0), role: str = "L",
               motion: str = "none"):
    """A koshi-bukuro, the leather nail pouch of a carpenter's belt: an open top with nail heads and a
    pencil peeking out, a stitched front and a darker welt at the rim."""
    w, h, d = size
    box = g.piece(pid, bone, (-w / 2, 0, -d / 2), size, pivot=pivot, rotation=rotation, motion=motion)
    solid(box, role, "leather", 22909, 2)
    for face in box.sides:
        face.hline(0, face.w - 1, 0, k(role, 1))
    box.top.fill("K1")
    box.top.set(0, 0, "M3")
    if w > 1:
        box.top.set(w - 1, d - 1, "M4")
    box.front.vline(w // 2, 1, h - 1, k(role, 3))
    return box


def tool_belt(g, prefix: str = "tool_belt", y: float = 9.4, role: str = "L", seed: int = 22910, pouches: bool = True,
              hammer: bool = True):
    """A wide leather tool belt round the hips with nail pouches at both front hips, a chisel tucked in
    the right one and a hammer loop at the back. Bottoms prefix it with 'waist' so long tops hide it."""
    belt = g.piece(prefix, "TORSO", (-4.6, y, -2.6), (9, 2, 5), inflate=.06)
    solid(belt, role, "leather", seed, 2, edge=False)
    for face in belt.sides:
        face.hline(0, face.w - 1, 0, k(role, 3))
        face.hline(0, face.w - 1, 1, k(role, 1))
    belt.front.set(4, 0, "M3"), belt.front.set(4, 1, "M2"), belt.front.set(3, 0, "M2")
    if pouches:
        for i, x in enumerate((-3.4, 3.4)):
            nail_pouch(g, f"{prefix}_pouch_{i}", (x, y + 1.2, -2.6), size=(2, 3, 2), role=role)
        chisel(g, f"{prefix}_chisel", (-3.0, y + 1.0, -2.7), (0, 0, 8))
    if hammer:
        loop = g.piece(f"{prefix}_loop", "TORSO", (-.5, 0, -.5), (1, 2, 1), pivot=(2.0, y + 1.8, 2.7))
        solid(loop, "M", "plain", seed + 1, 2, edge=False)
        mallet(g, f"{prefix}_mallet", (2.0, y + 2.6, 2.9), (0, 0, 0))
    return belt


def tabi(g, top: int = 7, role: str = "K", base: int = 2, clasps: bool = True):
    """Jika-tabi: split-toe work boots of soft cloth to the shin, hooked shut up the inside with brass
    kohaze clasps, the big toe parted from the others by a seam and a thick rubber sole."""
    for side in SIDES:
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        fabric(leg.strip, role, "weave", 22915 + (side == "left"), base, 0, top, leg.strip.w, 12 - top)
        leg.strip.hline(0, leg.strip.w - 1, top, k(role, base + 1))
        leg.bottom.fill("K0")
        for face in pants.sides:
            fabric(face, role, "weave", 22917, base, 0, top, face.w, 12 - top)
            face.hline(0, face.w - 1, top, k(role, base + 1))
            face.hline(0, face.w - 1, 11, "K0")
        pants.bottom.fill("K0")
        # The split toe: the big toe on the inner side of each foot.
        split = 2 if side == "right" else 1
        leg.front.vline(split, 10, 11, "K0"), pants.front.vline(split, 10, 10, "K0")
        pants.front.set(split, 11, "K0")
        if clasps:
            inner = leg.left if side == "right" else leg.right
            for y in range(top + 1, 10, 1):
                inner.set(1, y, "M3" if y % 2 else "M2")


def kyahan(g, top: int = 5, bottom: int = 8, role: str = "S", base: int = 3):
    """Kyahan gaiters: cloth shin guards wrapped over the trouser and tied at the top."""
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        fabric(leg.strip, role, "weave", 22919 + (side == "left"), base, 0, top, leg.strip.w, bottom - top + 1)
        leg.strip.hline(0, leg.strip.w - 1, top, k(role, base - 1))
        leg.strip.hline(0, leg.strip.w - 1, bottom, k(role, base - 1))
        for x in range(0, leg.strip.w, 4):
            leg.strip.set(x + 1, top + 1, k(role, base - 2))


def pencil(g, pid: str, pivot, rotation=(0, 0, 0), bone: str = "HEAD", length: int = 6):
    """A flat carpenter's pencil at three-quarter scale: cedar-red body, the bare wood and lead at the
    sharpened end below the pivot."""
    s = (.75, .75, .75)
    box = _piece(g, pid, bone, (-.5, -length / 2, -.5), (1, length, 1), pivot, rotation, s)
    solid(box, "A", "smooth", 22911, 3, edge=False)
    for face in box.sides:
        face.set(0, length - 1, "S3")
    box.bottom.fill("K1"), box.top.fill("A2")
    return box
