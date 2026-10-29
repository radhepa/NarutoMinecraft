"""Suzuran building blocks: the lily-of-the-valley household of herbalists, poison masters and field
medics. White bells hanging from green stems on their cloth and hems, the clan crest of a bell sprig,
glass vials of antidote and toxin, herb pouches with leaves spilling out, the apothecary sash worn
across the chest and the long medic gloves that keep the skin off what they brew.

Roles keep the village meaning: S is the porcelain-white cloth (and the bells), D a deep leaf green
(the stems and the clan's under-layers), A the toxic violet, M glass and steel, L the leather of
pouches and straps."""
from __future__ import annotations

from glyphs import stamp
from kit import arm_bone, arm_x
from paint import fabric, k, solid

# The Suzuran crest (an invention, drawn at double resolution): one arching stem with three white
# bells hanging from it and a broad leaf rising behind, inside a ring.
CREST = ["...oooooo...",
         ".oo......oo.",
         ".o..sss...o.",
         "o..s...s...o",
         "o.s.l...s..o",
         "o.s.l....b.o",
         "o..b.l..bbbo",
         "o.bbbl.b.b.o",
         "o.b.bl..b..o",
         ".o.b.l....o.",
         ".oo..l...oo.",
         "...oooooo..."]


# -- painted cloth -----------------------------------------------------------------------------
def bell_sprig(face, x: int, y: int, stem: str = "D2", bell: str = "S4", shade: str = "S2", bells: int = 3, flip: bool = False):
    """A small lily-of-the-valley sprig painted on a face: a stem arching over to one side with
    `bells` white bells hanging under it, each a bright texel over its shade. (x, y) is the root of
    the arch, the bells run off to the right (left if `flip`)."""
    step = -1 if flip else 1
    face.set(x, y + 1, stem), face.set(x, y, stem)
    for i in range(1, bells + 1):
        sx = x + i * step
        if not face.inside(sx, y):
            break
        face.set(sx, y, stem)
        if face.inside(sx, y + 1):
            face.set(sx, y + 1, bell)
        if face.inside(sx, y + 2):
            face.set(sx, y + 2, shade)


def bell_print(face, role: str, seed: int, base: int = 2, texture: str = "weave", stem: str = "D2", bell: str = "S4",
               shade: str | None = None, rows=None, every: int = 6):
    """Cloth with a sparse print of bell sprigs, offset row to row."""
    fabric(face, role, texture, seed, base)
    shade = shade or k(role, base - 1)
    for n, y in enumerate(rows if rows is not None else range(1, face.h - 2, 5)):
        for x in range((n % 2) * (every // 2), face.w - 2, every):
            bell_sprig(face, x, y, stem, bell, shade, bells=2)


def bell_hem(face, y: int, stem: str = "D2", bell: str = "S4", shade: str = "S2", step: int = 3, start: int = 1):
    """A hem trimmed with a running stem and a hanging bell every `step` columns."""
    face.hline(0, face.w - 1, y, stem)
    for x in range(start, face.w, step):
        if face.inside(x, y + 1):
            face.set(x, y + 1, bell)
        if face.inside(x, y + 2):
            face.set(x, y + 2, shade)


def back_crest(g, pid: str = "back_crest", ground: str = "P2", ring: str = "S3", pivot=(0, 1.4, 2.06),
               bone: str = "TORSO"):
    """The clan crest at double resolution on the back of a top."""
    box = g.piece(pid, bone, (-7, 0, 0), (14, 14, 1), pivot=(pivot[0], pivot[1], pivot[2]), scale=(.5, .5, .5))
    for f in box.faces:
        f.fill(ground)
    rows = [r[::-1] for r in CREST]
    stamp(box.back, rows, 1, 1, {"o": ring, "s": "D2", "l": "D1", "b": "S4"})
    return box


# -- gear --------------------------------------------------------------------------------------
def vial(g, pid: str, pivot, bone: str = "TORSO", liquid: str = "A2", rotation=(0, 0, 0), height: int = 4):
    """A stoppered glass vial at half scale: a cork, a clear shoulder and a coloured draught."""
    s = (.5, .5, .5)
    glass = g.piece(f"{pid}_glass", bone, (-1, 0, -1), (2, height, 2), pivot=pivot, rotation=rotation, scale=s)
    for f in glass.faces:
        f.fill("M4")
    for f in glass.sides:
        for y in range(1, height):
            f.set(0, y, k(liquid[0], int(liquid[1]) + (1 if y == 1 else 0)))
            f.set(1, y, k(liquid[0], int(liquid[1]) - (1 if y == height - 1 else 0)))
        f.set(1, 1, "M4")
    glass.bottom.fill(k(liquid[0], int(liquid[1]) - 1))
    cork = g.piece(f"{pid}_cork", bone, (-.5, -1, -.5), (1, 1, 1), pivot=pivot, rotation=rotation, scale=s)
    for f in cork.faces:
        f.fill("L3")
    return glass


def herb_pouch(g, pid: str, pivot, bone: str = "TORSO", role: str = "L", rotation=(0, 0, 0), size=(3, 3, 2),
               sprig: bool = True):
    """A drawstring pouch with a leafy sprig of herbs poking out of its mouth."""
    w, h, d = size
    box = g.piece(pid, bone, (-w / 2, 0, -d / 2), size, pivot=pivot, rotation=rotation)
    solid(box, role, "leather" if role == "L" else "weave", 24901, 2)
    for f in box.sides:
        f.hline(0, f.w - 1, 0, k(role, 3)), f.set(f.w // 2, 1, "K2")
    if sprig:
        leaf = g.piece(f"{pid}_herbs", bone, (-1, -2, -.5), (2, 2, 1), pivot=pivot, rotation=(0, 0, 14), scale=(.7, .7, .7))
        for f in leaf.faces:
            f.fill("D3")
        for f in leaf.sides:
            f.set(0, 0, "D4"), f.set(f.w - 1, f.h - 1, "D1")
        bell = g.piece(f"{pid}_bell", bone, (.4, -2.4, -.7), (1, 1, 1), pivot=pivot, rotation=(0, 0, 14), scale=(.6, .6, .6))
        for f in bell.faces:
            f.fill("S4")
    return box


def apothecary_sash(front, back, role: str = "L", base: int = 2, rows: int = 12):
    """A sash painted two texels wide from the right shoulder across the chest to the left hip, and
    from the left hip back up to the right shoulder behind."""
    for y in range(rows):
        x = min(6, y * 7 // (rows - 1))
        front.set(x, y, k(role, base + 1)), front.set(x + 1, y, k(role, base - 1))
        back.set(7 - x, y, k(role, base + 1)), back.set(6 - x, y, k(role, base - 1))


def sash_vials(g, prefix: str, liquids=("A2", "D3", "S3"), start=(-2.4, 1.8), step=(1.27, 2.0), z: float = -2.75):
    """Vials slotted into a chest sash, following its slope down from the right shoulder."""
    for i, liquid in enumerate(liquids):
        vial(g, f"{prefix}_{i}", (start[0] + i * step[0], start[1] + i * step[1], z), liquid=liquid)


def gloves(g, role: str = "K", base: int = 2, top: int = 7, cuff: str | None = None):
    """Long medic gloves from row `top` of the base arm to the fingertips, with a turned cuff."""
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        for y in range(top, 12):
            arm.strip.hline(0, arm.strip.w - 1, y, k(role, base - (1 if y == 11 else 0)))
        arm.bottom.fill(k(role, base - 1))
        arm.strip.hline(0, arm.strip.w - 1, top, cuff or k(role, base + 1))


def armband(g, prefix: str, y: float = 1.4, role: str = "S", mark: str = "D2"):
    """A white medic's armband on each upper arm with a green sprig mark on the outside."""
    for side in ("right", "left"):
        band = g.piece(f"{side}_{prefix}", arm_bone(side), (arm_x(side) - .45, y, -2.45), (5, 2, 5))
        solid(band, role, "weave", 24902 + (side == "left"), 3, edge=False)
        outer = band.right if side == "right" else band.left
        outer.set(2, 0, mark), outer.set(2, 1, mark), outer.set(1, 1, "S4" if role != "S" else "D3")


# -- hair ornaments ----------------------------------------------------------------------------
def bell_charm(g, pid: str, pivot, rotation=(0, 0, 0), bells: int = 3, bone: str = "HEAD", stem: str = "D2",
               bell: str = "S4"):
    """A sprig of lily of the valley at half scale, pinned in the hair or tied to a cord: a green stem
    arching along local +x with white bells hanging under it, each with a flared lip."""
    s = (.5, .5, .5)
    arch = g.piece(f"{pid}_stem", bone, (0, -1, -.5), (2 * bells + 1, 1, 1), pivot=pivot, rotation=rotation, scale=s)
    for f in arch.faces:
        f.fill(stem)
    for f in arch.sides:
        f.set(0, 0, k(stem[0], int(stem[1]) + 1))
    leaf = g.piece(f"{pid}_leaf", bone, (-1, -4, -.5), (2, 4, 1), pivot=pivot, rotation=rotation, scale=s)
    for f in leaf.faces:
        f.fill(k(stem[0], int(stem[1]) + 1))
    for f in leaf.sides:
        f.vline(0, 1, 3, k(stem[0], int(stem[1]) - 1))
    for i in range(bells):
        x = 1 + 2 * i
        cup = g.piece(f"{pid}_bell_{i}", bone, (x, 0, -.5), (1, 1, 1), pivot=pivot, rotation=rotation, scale=s,
                      inflate=.15)
        for f in cup.faces:
            f.fill(bell)
        lip = g.piece(f"{pid}_lip_{i}", bone, (x - .5, 1, -1), (2, 1, 2), pivot=pivot, rotation=rotation, scale=s)
        for f in lip.faces:
            f.fill(k(bell[0], int(bell[1]) - 1))
