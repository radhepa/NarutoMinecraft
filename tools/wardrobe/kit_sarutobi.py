"""Sarutobi clan building blocks: the beard grown along the jaw (clear of the mouth), the clan crest
of a ring round a flame, the long scarf, the Twelve Guardian sash with its fire kanji and the
monkey-king armor plates of the Third Hokage's battle dress.

Hair pieces in the clan's styles are named from a few prefixes (crown, fringe, frame, back, tail,
bun, nape) so the battle helmet can hide them and leave the beard, which starts with 'beard'."""
from anime import cel_box, lock
from glyphs import FIRE, stamp
from paint import fabric, k, solid

HAIR_PREFIXES = ["crown", "fringe", "frame", "back", "tail", "bun", "nape"]


# -- beards ----------------------------------------------------------------------------------
BEARD_Z = -4.08   # lying on the face, just in front of the skin and the face planes


def beard(g, seed: int, style: str = "full", goatee: int = 0):
    """A short beard grown along the jaw. Every piece stays below the eyes (y > -2) and clear of the
    mouth (|x| < 1, y -1.7..-1.2): sideburns down the sides of the head, cheek pads on the lower
    outer cheeks, a chin band under the lip, a strap under the jaw and an optional goatee tuft.
    Styles: full (Asuma), chinstrap (sideburns, jaw and a thin chin line), goatee (chin only)."""
    if style in ("full", "chinstrap"):
        for side, sign in (("right", -1), ("left", 1)):
            box = g.piece(f"beard_side_{side}", "HEAD", (3.5 if sign > 0 else -4.5, -5.0, -4.05), (1, 5, 3))
            cel_box(box, seed + (sign > 0), base=2, top_delta=0)
    if style == "full":
        for side, sign in (("right", -1), ("left", 1)):
            pad = g.piece(f"beard_cheek_{side}", "HEAD", (2.1 if sign > 0 else -4.1, -1.9, BEARD_Z), (2, 2, 1))
            cel_box(pad, seed + 2 + (sign > 0), base=2, top_delta=0)
            pad.front.set(0 if sign > 0 else 1, 0, k("H", 1))
    if style in ("full", "chinstrap", "goatee"):
        w = {"full": 5, "chinstrap": 7, "goatee": 3}[style]
        chin = g.piece("beard_chin", "HEAD", (-w / 2, -.95, BEARD_Z), (w, 1, 1))
        cel_box(chin, seed + 4, base=2 if style != "chinstrap" else 1, top_delta=0)
    if style in ("full", "chinstrap"):
        strap = g.piece("beard_jaw", "HEAD", (-4.4, 0, -4.4), (9, 1, 4))
        cel_box(strap, seed + 3, base=2, top_delta=0)
        strap.front.hline(0, 8, 0, k("H", 2))
        strap.front.set(0, 0, k("H", 1)), strap.front.set(8, 0, k("H", 1))
    if goatee:
        lock(g, "beard_goatee", (0, .15, -3.9), (8, 0, 0), ((2, goatee), (1, 1)), 1, seed + 5, ring=None)


# -- crest -----------------------------------------------------------------------------------
# The Sarutobi crest: a ring round a three-tongued flame (the Will of Fire), at double resolution.
CREST = ["...####...",
         ".##....##.",
         ".#..#....#",
         "#...##...#",
         "#..#.##..#",
         "#..#.#.#.#",
         "#.##.##..#",
         ".#.####.#.",
         ".##....##.",
         "...####..."]


def crest(face, x0: int, y0: int, key: str, ground: str | None = None):
    if ground:
        for y in range(10):
            for x in range(10):
                if 2 <= x + y <= 16 and -7 <= x - y <= 7:
                    face.set(x0 + x, y0 + y, ground)
    stamp(face, CREST, x0, y0, {"#": key})


def crest_patch(g, pid: str, bone: str, pivot, role: str, key: str, seed: int, face: str = "back",
                ground: str | None = None, rotation=(0, 0, 0)):
    """The crest on a thin cloth patch at half scale (5 x 5 model pixels), facing `face`."""
    size = {"back": (10, 10, 1), "front": (10, 10, 1), "right": (1, 10, 10), "left": (1, 10, 10)}[face]
    origin = {"back": (-5, 0, 0), "front": (-5, 0, -1), "right": (-1, 0, -5), "left": (0, 0, -5)}[face]
    patch = g.piece(pid, bone, origin, size, pivot=pivot, scale=(.5, .5, .5), rotation=rotation)
    for f in patch.faces:
        fabric(f, role, "weave", seed, 2)
    crest(getattr(patch, face), 0, 0, key, ground)
    return patch


# -- scarf -----------------------------------------------------------------------------------
def scarf(g, role: str = "D", seed: int = 9300, tail: int = 14, front_tail: int = 0, stripe: str | None = None):
    """A scarf wound twice round the neck, a long tail trailing down the back from the left shoulder
    and, if `front_tail`, a short end over the right of the chest. Konohamaru's runs to the knees."""
    wrap = g.piece("scarf_wrap", "TORSO", (-4.5, -1.8, -2.7), (9, 3, 5), inflate=.1)
    solid(wrap, role, "knit", seed, 2, edge=False)
    for f in wrap.sides:
        f.hline(0, f.w - 1, 0, k(role, 3)), f.hline(0, f.w - 1, 1, k(role, 1))
    knot = g.piece("scarf_knot", "TORSO", (-1, 0, -1), (2, 2, 2), pivot=(2.4, 1.0, 2.6))
    solid(knot, role, "knit", seed + 1, 2)
    ends = [("scarf_tail", (2.2, 1.6, 2.7), (10, 0, -4), tail)]
    if front_tail:
        ends.append(("scarf_front", (-2.4, .6, -2.9), (-6, 0, 3), front_tail))
    for pid, pivot, rot, n in ends:
        if n <= 0:
            continue
        box = g.piece(pid, "TORSO", (-1.5, 0, -.5), (3, n, 1), pivot=pivot, rotation=rot, motion="sway")
        solid(box, role, "knit", seed + 2 + len(pid), 2)
        for f in box.sides:
            f.hline(0, f.w - 1, n - 1, k(role, 1))
            if stripe:
                f.hline(0, f.w - 1, n - 3, stripe)
        box.back.vline(1, 0, n - 2, k(role, 3)) if pid == "scarf_tail" else box.front.vline(1, 0, n - 2, k(role, 3))


# -- the Twelve Guardian sash ----------------------------------------------------------------
def guardian_sash(g, role: str = "S", ink: str = "K1", seed: int = 9400, y: float = 8.6, pid: str = "sash"):
    """Asuma's sash of the Twelve Guardian Ninja: a broad cloth belt knotted on the left hip, two
    hanging ends and a square on the front of the right hip carrying the kanji for fire."""
    belt = g.piece(pid, "TORSO", (-4.6, y, -2.6), (9, 2, 5), inflate=.12)
    solid(belt, role, "weave", seed, 2, edge=False)
    for f in belt.sides:
        f.hline(0, f.w - 1, 0, k(role, 3))
    knot = g.piece(f"{pid}_knot", "TORSO", (-1, -1, -1), (2, 2, 2), pivot=(3.6, y + 1, -2.6))
    solid(knot, role, "weave", seed + 1, 2)
    for i, (x, rz, n) in enumerate(((3.2, 8, 6), (4.0, -6, 5))):
        end = g.piece(f"{pid}_end_{i}", "TORSO", (-.5, 0, -.5), (1, n, 1), pivot=(x, y + 1.6, -2.8), rotation=(-4, 0, rz),
                      motion="sway")
        solid(end, role, "weave", seed + 2 + i, 2)
        end.front.set(0, n - 1, k(role, 1))
    plate = g.piece(f"{pid}_kanji", "TORSO", (-7, 0, -1), (14, 16, 1), pivot=(-2.0, y - .2, -2.85), scale=(.25, .25, .25))
    for f in plate.faces:
        fabric(f, role, "weave", seed + 4, 3)
    fr = plate.front
    fr.hline(0, 13, 0, k(role, 4)), fr.hline(0, 13, 15, k(role, 1))
    fr.vline(0, 0, 15, k(role, 2)), fr.vline(13, 0, 15, k(role, 1))
    stamp(fr, FIRE, 1, 1, {"#": ink})


# -- armor -----------------------------------------------------------------------------------
def pauldron(g, side: str, role: str = "M", seed: int = 9500, trim: str | None = None, tiers: int = 2):
    """Layered shoulder plates over the upper arm, each tier a little wider and lower."""
    bone = "RIGHT_ARM" if side == "right" else "LEFT_ARM"
    ox = -3.0 if side == "right" else -1.0
    for t in range(tiers):
        plate = g.piece(f"{side}_pauldron_{t}", bone, (ox - .6 - t * .2, -2.6 + t * 1.6, -2.6 - t * .2), (5, 2, 5),
                        inflate=.05 + t * .1)
        solid(plate, role, "smooth", seed + t, 2)
        for f in plate.sides:
            f.hline(0, f.w - 1, 0, k(role, 3))
            f.hline(0, f.w - 1, 1, trim or k(role, 1))


# A monkey face for the back of the battle armor (Enma), at double resolution: ears, brow ridge,
# two eyes and a muzzle.
MONKEY = [".##......##.",
          "#..######..#",
          "#.#......#.#",
          ".#.######.#.",
          ".#.#....#.#.",
          ".#..#..#..#.",
          ".#........#.",
          "..#.####.#..",
          "..#.#..#.#..",
          "...#....#...",
          "....####...."]


def monkey(face, x0: int, y0: int, key: str):
    stamp(face, MONKEY, x0, y0, {"#": key})


# Flame tongues for a hem, repeating every six texels: '#' accent, '+' its lighter core.
FLAME = ["..#...",
         ".##..#",
         ".#+#.#",
         "#+++##",
         "######"]


def flame_hem(face, y0: int, key: str, core: str, x0: int = 0):
    """Flame tongues rising from row y0 + 4 up to y0 across a face."""
    for x in range(face.w):
        for dy, row in enumerate(FLAME):
            ch = row[(x + x0) % 6]
            if ch == "#":
                face.set(x, y0 + dy, key)
            elif ch == "+":
                face.set(x, y0 + dy, core)
