"""Kurama clan helpers: the genjutsu painters' household. Soft waves and side parts for the hair, a
paint brush worn as a hairpin, the two-bead clip Yakumo wears, and the clan's painted cloth: ink-wash
clouds, wisteria sprays and the Kurama crest (a brush-stroke cloud in a ring)."""
from __future__ import annotations

from anime import cel_box, lock
from kit import arm_bone, arm_x
from paint import fabric, k, rnd, solid


# -- hair --------------------------------------------------------------------------------------
def wave_lock(g, pid: str, pivot, rotation=(0, 0, 0), segments=((3, 3), (3, 3), (2, 2), (1, 1)), depth: int = 1,
              seed: int = 0, base: int = 2, amp: float = .45, ring: int | None = 1, motion: str = "none", y0: float = 0.0,
              phase: int = 0, z_offset: float = 0.0):
    """A soft wave: a tapered lock whose segments step side to side, so the length ripples."""
    y = y0
    boxes = []
    for i, (w, h) in enumerate(segments):
        dx = amp * (1 if (i + phase) % 2 else -1) if i else 0
        box = g.piece(f"{pid}_{i}", "HEAD", (-w / 2 + dx, y, -depth / 2 + z_offset), (w, h, depth), pivot=pivot,
                      rotation=rotation, motion=motion)
        cel_box(box, seed + i * 7, base, ring if i == 0 else None, top_delta=1 if i == 0 else 0)
        y += h
        boxes.append(box)
    return boxes


def side_fringe(g, prefix: str, seed: int, side: int = 1, specs=None, z: float = -4.35):
    """A fringe swept away from a side part: every lock leans the same way. `side` 1 parts the hair
    over the wearer's right eye and sweeps it to the left (+x); -1 mirrors it. Central locks stay short
    so the brows show."""
    specs = specs or [(-3.3, ((2, 2), (1, 1)), 4), (-1.4, ((3, 2), (2, 1)), 28), (.6, ((3, 2), (2, 1)), 30),
                      (2.4, ((2, 2), (1, 1)), 22), (3.4, ((2, 3), (1, 1)), 6)]
    for i, (x, segs, rz) in enumerate(specs):
        lock(g, f"{prefix}_{i}", (x * side, -8.55, z), (-10, 0, -rz * side), segs, 1, seed + i * 13, ring=0)


def part_line(g, x: int, base: int = 2):
    """The side part painted along the crown of the hat layer."""
    hat = g.part("hat")
    hat.top.vline(x, 0, 7, k("H", base - 2))
    hat.top.vline(min(7, x + 1), 0, 7, k("H", base + 2))


def brush_pin(g, pid: str, pivot, rotation=(0, 0, 0), length: int = 9, tip: str = "K2", ferrule: str = "M3",
              handle: str = "L", scale: float = .5):
    """A paint brush slid through the hair as a pin: a lacquered handle, a steel ferrule and an
    ink-dipped tip, at double resolution. The tip end sits at the pivot; the handle runs along -y."""
    s = (scale, scale, scale)
    stick = g.piece(f"{pid}_handle", "HEAD", (-.5, -length, -.5), (1, length, 1), pivot=pivot, rotation=rotation, scale=s)
    solid(stick, handle, "smooth", 12960, 3, edge=False)
    for f in stick.sides:
        f.set(0, 0, k(handle, 1)), f.set(0, length // 2, k(handle, 4))
    band = g.piece(f"{pid}_ferrule", "HEAD", (-1, 0, -1), (2, 2, 2), pivot=pivot, rotation=rotation, scale=s)
    for f in band.faces:
        f.fill(ferrule)
    for f in band.sides:
        f.set(0, 1, k(ferrule[0], int(ferrule[1]) - 1))
    bristle = g.piece(f"{pid}_tip", "HEAD", (-1, 2, -1), (2, 3, 2), pivot=pivot, rotation=rotation, scale=s)
    for f in bristle.faces:
        f.fill("S3")
    for f in bristle.sides:
        f.hline(0, 1, 1, tip), f.hline(0, 1, 2, k(tip[0], int(tip[1]) - 1))
    bristle.bottom.fill(k(tip[0], int(tip[1]) - 1))


def bead_clip(g, pid: str, pivot, rotation=(0, 0, 0), key: str = "A3", step=(0, 1.1, 0)):
    """Two round beads on a pin, the clip Yakumo wears: two small cubes at double resolution."""
    for i in range(2):
        p = (pivot[0] + step[0] * i, pivot[1] + step[1] * i, pivot[2] + step[2] * i)
        bead = g.piece(f"{pid}_{i}", "HEAD", (-1, -1, -1), (2, 2, 2), pivot=p, rotation=rotation, scale=(.5, .5, .5))
        for f in bead.faces:
            f.fill(key)
        for f in bead.sides:
            f.set(0, 0, k(key[0], min(4, int(key[1]) + 1)))
            f.set(1, 1, k(key[0], int(key[1]) - 1))


def bun(g, pid: str, pivot, size: int = 3, seed: int = 0, rotation=(0, 0, 0)):
    """A round knot of hair: a squat core with a smaller domed cap, cel shaded and creased."""
    h = size - 1
    core = g.piece(pid, "HEAD", (-size / 2, -h / 2, -size / 2), (size, h, size), pivot=pivot, rotation=rotation)
    cel_box(core, seed, ring=0, top_delta=1)
    cap = g.piece(f"{pid}_cap", "HEAD", (-(size - 2) / 2, -h / 2 - .5, -(size - 2) / 2), (size - 2, 1, size - 2),
                  pivot=pivot, rotation=rotation, inflate=.25)
    cel_box(cap, seed + 3, top_delta=1)
    for f in core.sides:
        for x in range(f.w):
            if (x + seed) % 3 == 0:
                f.vline(x, 0, f.h - 1, k("H", 1))
    return core


# -- cloth -------------------------------------------------------------------------------------
# The Kurama crest: a three-lobed brush-stroke cloud inside a ring, drawn at double resolution.
CREST = ["...####...",
         ".##....##.",
         "#........#",
         "#..##....#",
         "#.#..#.#.#",
         "#.#.##..##",
         "#..#...#.#",
         "#.......##",
         ".##....##.",
         "...####..."]

# A wisteria spray: a hanging cluster of florets, lighter at the top, on a short stem.
WISTERIA = ["..#..",
            ".aba.",
            "abab.",
            ".bab.",
            "..ab.",
            "..b..",
            "..a.."]


def stamp(face, rows, x0, y0, legend):
    for y, row in enumerate(rows):
        for x, ch in enumerate(row):
            if ch in legend:
                face.set(x0 + x, y0 + y, legend[ch])


def ink_clouds(face, role: str, seed: int, base: int = 2, rows=None, density: float = .5):
    """Ink-wash cloud bands: soft horizontal swirls one shade off the cloth, scattered by seed."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        for x in range(face.w):
            band = (y + int(rnd(x // 4, 3, seed) * 3)) % 5
            if band == 0 and rnd(x, y, seed) < density:
                face.set(x, y, k(role, base + 1))
            elif band == 1 and rnd(x, y, seed + 1) < density * .6:
                face.set(x, y, k(role, base - 1))


def brush_stroke(face, x0: int, y0: int, length: int, key: str, slope: float = .35):
    """One calligraphic stroke: a thick start tapering along a gentle slope."""
    for i in range(length):
        y = y0 + round(i * slope)
        face.set(x0 + i, y, key)
        if i < length * .6:
            face.set(x0 + i, y + 1, key)


def back_crest(g, pid: str = "back_crest", role: str = "P", ink: str = "A2", pivot=(0, 1.4, 2.06), base: int = 2,
               texture: str = "weave", bone: str = "TORSO"):
    """The Kurama crest across the shoulder blades at double resolution: a 5 x 5 cloth patch in the
    garment's role with the cloud-in-a-ring stroked in `ink`."""
    plate = g.piece(pid, bone, (-5, 0, 0), (10, 10, 1), pivot=pivot, scale=(.5, .5, .5))
    for face in plate.faces:
        fabric(face, role, texture, 12990, base)
    stamp(plate.back, [r[::-1] for r in CREST], 0, 0, {"#": ink})
    return plate


def kimono_sleeves(g, role: str, texture: str = "weave", seed: int = 0, base: int = 2, length: int = 9, top: float = -2.4,
                   trim: str | None = None, bell: bool = True, sides=("right", "left")):
    """Wide kimono sleeves: a loose tube over the arm from the shoulder, opening into a deeper bell
    above the wrist, the hem edged in `trim`. Returns the sleeve boxes."""
    out = []
    for side in sides:
        tube = g.piece(f"{side}_kimono_sleeve", arm_bone(side), (arm_x(side) - .5, top, -2.5), (5, length, 5), inflate=.12)
        solid(tube, role, texture, seed + (side == "left"), base)
        fabric(tube.top, role, texture, seed, base + 1)
        for f in tube.sides:
            f.vline(f.w - 1, 1, length - 1, k(role, base - 1))
            if trim:
                f.hline(0, f.w - 1, length - 1, trim)
        tube.bottom.fill(k(role, base - 2))
        out.append(tube)
        if bell:
            mouth = g.piece(f"{side}_sleeve_bell", arm_bone(side), (arm_x(side) - 1, top + length - 2, -3), (6, 3, 6),
                            inflate=.05)
            solid(mouth, role, texture, seed + 2 + (side == "left"), base)
            for f in mouth.sides:
                f.hline(0, f.w - 1, 0, k(role, base + 1))
                f.hline(0, f.w - 1, 2, trim or k(role, base - 1))
            mouth.bottom.fill(k(role, base - 2))
            out.append(mouth)
    return out


def wrap_front(face, edge: str, under: str | None = None, rows: int = 7, start: int = 1):
    """The kimono wrap on a body front: a diagonal collar edge from the wearer's right shoulder down
    to the left hip, with an optional under-collar line just inside it."""
    for i in range(rows):
        x = start + i
        if x <= 7:
            face.set(x, i, edge)
            if under and x - 1 >= 0:
                face.set(x - 1, i, under)


def wisteria_hem(face, seed: int, light: str = "A3", dark: str = "A2", stem: str = "S2", step: int = 2, y0: int = 0):
    """Wisteria hanging from a vine along row `y0`: a spray every `step` texels, each a short column of
    florets alternating light and dark, the longer ones tapering to a light tip."""
    face.hline(0, face.w - 1, y0, stem)
    for x in range(int(rnd(seed, 1) * step), face.w, step):
        n = 2 + int(rnd(x, 5, seed) * 3)
        for d in range(n):
            face.set(x, y0 + 1 + d, light if (d + x) % 2 == 0 else dark)
        face.set(x, y0 + n, light)


def splatter(face, seed: int, keys=("A2", "D2", "K2"), density: float = .06, rows=None):
    """Paint spatters: single texels and two-texel drips in a few paint colors."""
    rows = range(face.h) if rows is None else rows
    for y in rows:
        for x in range(face.w):
            r = rnd(x, y, seed)
            if r < density:
                key = keys[int(rnd(x, y, seed + 1) * len(keys))]
                face.set(x, y, key)
                if r < density * .3:
                    face.set(x, y + 1, key)
