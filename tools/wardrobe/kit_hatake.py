"""Hatake building blocks: the clan crest, the scarecrow face of the ninja hounds' vests, paw prints,
the White Fang's white-hilted tanto, the forehead protector worn aslant and the cloth face mask."""
from glyphs import LEAF, stamp
from paint import fabric, k, solid

# The Hatake crest (an invention, drawn at double resolution): a white fang inside a ring.
CREST = ["...oooo...",
         ".oo....oo.",
         ".o.ffff.o.",
         "o..ffff..o",
         "o...ff...o",
         "o...ff...o",
         "o....f...o",
         ".o...f..o.",
         ".oo....oo.",
         "...oooo..."]

# へのへのもへじ: the scarecrow face Kakashi's ninja hounds wear on the backs of their vests.
SCARECROW = ["...#......#...",
             "..#.#....#.#..",
             ".#...#..#...#.",
             "............#.",
             "..##......##.#",
             ".#..#....#..#.",
             ".#.##....#.##.",
             "..##..#...##..",
             "......#.......",
             ".....###.....#",
             "......#......#",
             "....#...#...#.",
             "...#.....#.#..",
             "..........#..."]

PAW = [".o.o.",
       "o...o",
       "..o..",
       ".ooo.",
       ".ooo."]


def decal(g, pid: str, rows, legend: dict, ground: str, pivot, bone: str = "TORSO", face: str = "back", pad: int = 1):
    """A double-resolution flat decal carrying `rows` on one face, the rest filled with `ground`."""
    w, h = len(rows[0]) + 2 * pad, len(rows) + 2 * pad
    z0 = 0 if face == "back" else -1
    box = g.piece(pid, bone, (-w / 2, 0, z0), (w, h, 1), pivot=pivot, scale=(.5, .5, .5))
    for f in box.faces:
        f.fill(ground)
    target = getattr(box, face)
    src = [r[::-1] for r in rows] if face == "back" else rows
    stamp(target, src, pad, pad, legend)
    return box


def white_fang_tanto(g, prefix: str = "tanto", pivot=(-1.6, 1.4, 2.9), rotation=(0, 0, 32), bone: str = "TORSO",
                     length: int = 8):
    """Sakumo's chakra sabre: a white hilt wound with black cord, a small steel guard and a long black
    sheath, worn across the back with the hilt over the shoulder."""
    hilt = g.piece(f"{prefix}_hilt", bone, (-.5, -4, -.5), (1, 4, 1), pivot=pivot, rotation=rotation)
    solid(hilt, "S", "smooth", 11951, 3, edge=False)
    for face in hilt.sides:
        face.set(0, 1, "K1"), face.set(0, 3, "K1")
    hilt.top.fill("M3")
    guard = g.piece(f"{prefix}_guard", bone, (-1, 0, -1), (2, 1, 2), pivot=pivot, rotation=rotation)
    solid(guard, "M", "plain", 11952, 3)
    sheath = g.piece(f"{prefix}_sheath", bone, (-.5, 1, -.5), (1, length, 1), pivot=pivot, rotation=rotation)
    solid(sheath, "K", "smooth", 11953, 2)
    for face in sheath.sides:
        face.set(0, 1, "S3"), face.set(0, length - 1, "M2")


def slanted_protector(g, band: str = "D", seed: int = 11961, tilt: float = 10, flap: bool = True):
    """The forehead protector worn aslant, dipping over the wearer's left brow the way Kakashi wears it
    over his Sharingan; a fold of the band hangs at the left temple, outside the eye."""
    rot = (0, 0, tilt)
    box = g.piece("band", "HEAD", (-4, -.5, -4), (8, 1, 8), pivot=(0, -7.1, 0), rotation=rot, inflate=.6)
    solid(box, band, "weave", seed, 2, edge=False)
    plate = g.piece("plate", "HEAD", (-9, -4, -2), (18, 8, 2), pivot=(0, -7.1, -4.62), rotation=rot,
                    scale=(1 / 3, 1 / 3, 1 / 3))
    for face in plate.faces:
        fabric(face, "M", "plain", seed + 1, 2)
    fabric(plate.front, "M", "plain", seed + 1, 3)
    plate.front.hline(0, 17, 0, "M4"), plate.front.hline(0, 17, 7, "M1")
    plate.front.vline(0, 0, 7, "M2"), plate.front.vline(17, 0, 7, "M1")
    for x in (2, 15):
        plate.front.set(x, 2, "M1"), plate.front.set(x, 5, "M1")
    stamp(plate.front, LEAF, 5, 0, {"#": "M0"})
    if flap:
        fold = g.piece("band_fold", "HEAD", (0, 0, 0), (2, 2, 1), pivot=(3.4, -5.6, -4.75), rotation=(0, 0, 8))
        solid(fold, band, "weave", seed + 2, 2)
        fold.front.hline(0, 1, 0, k(band, 3))
    knot = g.piece("knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -7.1, 4.6))
    solid(knot, band, "weave", seed + 3, 2)
    for i, (x, rz) in enumerate(((-.6, 14), (.6, -10))):
        tail = g.piece(f"tail_{i}", "HEAD", (-.5, 0, 0), (1, 5, 1), pivot=(x, -6.4, 4.9), rotation=(22, 0, rz), motion="sway")
        solid(tail, band, "weave", seed + 4 + i, 2)
        tail.back.set(0, 4, k(band, 1))


def face_mask(g, role: str = "D", seed: int = 11971, neck: bool = True):
    """A close-fitting cloth mask pulled up over the nose to just under the eyes, its seam down the
    bridge of the nose, running on down into the collar."""
    mask = g.piece("face_mask", "HEAD", (-4, -1.75, -4), (8, 2, 8), inflate=.25)
    solid(mask, role, "knit", seed, 2, edge=False)
    mask.front.vline(3, 0, 1, k(role, 3)), mask.front.vline(4, 0, 1, k(role, 1))
    for face in mask.sides:
        face.hline(0, face.w - 1, 0, k(role, 3))
    if neck:
        collar = g.piece("face_mask_neck", "HEAD", (-3.5, 0, -3.5), (7, 1, 7), inflate=.1)
        solid(collar, role, "knit", seed + 1, 1, edge=False)


def shoulder_decal(g, prefix: str, rows, legend: dict, ground: str, y: float = .4):
    """A double-resolution patch on the outside of each upper arm (the left arm's mirrored)."""
    w, h = len(rows[0]) + 1, len(rows) + 1
    for side, bone, x in (("right", "RIGHT_ARM", -3.55), ("left", "LEFT_ARM", 3.05)):
        patch = g.piece(f"{side}_{prefix}", bone, (0, 0, -w / 2), (1, h, w), pivot=(x, y, 0), scale=(.5, .5, .5))
        for f in patch.faces:
            f.fill(ground)
        outer = patch.right if side == "right" else patch.left
        stamp(outer, rows if side == "left" else [r[::-1] for r in rows], 0, 0, legend)
