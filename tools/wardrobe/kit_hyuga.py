"""Hyuga helpers: the long, straight, heavy hair of the clan (blunt fringes, hime side panels, back
sheets that clear the robes, a tail gathered and tied near its tip) and the clan's wrapped garments
(a left-over-right collar, wide kimono sleeves, a knotted obi, hakama legs).

Hair hangs from the crown in sheets rather than spikes: one curtain down the back, a panel over each
ear and narrow locks framing the face, so the silhouette stays smooth and the Byakugan stays clear.
"""
from __future__ import annotations

from anime import bangs, cel_box, curtain, lock, ring_shell, tie
from kit import arm_x, leg_bone
from paint import cap, fabric, k, scalp, solid, strip_fabric

SIDES = (("right", -1), ("left", 1))


# -- hair ------------------------------------------------------------------------------------
def crown(g, seed: int, side_rows: int = 6, back_rows: int = 8, sideburn: int = 4, part: int | None = None, ring_row: int = 1):
    """Scalp paint plus the glossy hat shell: the base of every Hyuga hairstyle."""
    scalp(g, seed, side_rows=side_rows, back_rows=back_rows, sideburn=sideburn, part=part)
    return ring_shell(g, seed + 1, side_rows=min(side_rows, 7), back_rows=back_rows, ring_row=ring_row)


def ear_panels(g, prefix: str, length: int, seed: int, z0: float = -3, depth: int = 7, x: float = 4.6, flare: float = 0,
               top: float = -7.0):
    """A flat sheet of hair over each ear, from the temple down `length` texels."""
    for side, sign in SIDES:
        panel = g.piece(f"{prefix}_{side}", "HEAD", (-.5, 0, z0), (1, length, depth), pivot=(x * sign, top, .6),
                        rotation=(0, 0, -flare * sign))
        cel_box(panel, seed + (sign > 0), ring=1)


def hime_locks(g, prefix: str, length: int, seed: int, x: float = 4.2, z: float = -3.5, width: int = 2, flare: float = 1):
    """The hime cut's blunt face-framing locks: straight, square-ended, cut level at the jaw or below."""
    for side, sign in SIDES:
        lock(g, f"{prefix}_{side}", (x * sign, -7.6, z), (0, 0, -flare * sign), ((width, length),), 1,
             seed + (sign > 0) * 31, ring=1)


def blunt_fringe(g, prefix: str, seed: int, length: int = 2, xs=(-3.0, -1.0, 1.0, 3.0), tips: bool = True):
    """A straight-cut fringe of square locks across the forehead, ending at the brows."""
    specs = []
    for x in xs:
        mid = abs(x) < 2
        segs = ((2, length), (1, 1)) if tips and not mid else ((2, length),)
        specs.append((x, segs, -3 * x))
    bangs(g, prefix, specs, seed)


def parted_fringe(g, prefix: str, seed: int, reach: int = 2, part: float = 0.0):
    """Locks swept out from a part to the temples, leaving the middle of the forehead open."""
    bangs(g, prefix, [(part - 1.6, ((2, 1), (1, 1)), 38), (part - 3.0, ((2, reach), (1, 1)), 18),
                      (part + 1.6, ((2, 1), (1, 1)), -38), (part + 3.0, ((2, reach), (1, 1)), -18)], seed)


def back_sheet(g, prefix: str, length: int, seed: int, width: int = 9, hem=None, pivot=(0, -6.0, 4.6), tilt: float = -5,
               depth: int = 1):
    """The long curtain down the back; `hem` lists (x, width, length) tips, default three soft points."""
    if hem is None:
        third = width // 3
        hem = [(0, third, 2), (third, width - 2 * third, 3), (width - third, third, 2)]
    return curtain(g, prefix, pivot, (tilt, 0, 0), width, length, hem, seed, depth=depth)


def gathered_tail(g, prefix: str, pivot, tilt: float, sections, seed: int, tie_at: int, tie_key: str | None = None,
                  tip=((3, 2), (2, 2), (1, 1)), depth: int = 2):
    """Hair gathered down the back in narrowing sections, tied at section `tie_at`, ending in a tuft.
    `sections` are (width, height); returns the local y where the tail ends."""
    y = 0.0
    rot = (tilt, 0, 0)
    for i, (w, h) in enumerate(sections):
        box = g.piece(f"{prefix}_{i}", "HEAD", (-w / 2, y, -depth / 2), (w, h, depth), pivot=pivot, rotation=rot,
                      motion="sway")
        cel_box(box, seed + i * 7, ring=1 if i == 0 else None, top_delta=1 if i == 0 else 0)
        y += h
        if i == tie_at:
            w0 = sections[i][0]
            tie(g, f"{prefix}_tie", pivot, rot, (max(2, w0 - 1), 1, depth + 1), y=y - .5, key=tie_key, motion="sway")
    for j, (w, h) in enumerate(tip):
        box = g.piece(f"{prefix}_tip_{j}", "HEAD", (-w / 2, y, -min(depth, w) / 2), (w, h, min(depth, w)),
                      pivot=pivot, rotation=rot, motion="sway")
        cel_box(box, seed + 50 + j, top_delta=0)
        y += h
    return y


def hair_tie(g, pid: str, pivot, rotation=(0, 0, 0), size=(3, 1, 2), key: str | None = None, motion: str = "none", y: float = 0):
    return tie(g, pid, pivot, rotation, size, y=y, key=key, motion=motion)


# -- garments --------------------------------------------------------------------------------
def wrap_front(face, role: str = "P", trim: str = "A2", rows: int = 8, start: int = 1):
    """The left-over-right kimono overlap: a trimmed diagonal from the right shoulder to the left hip."""
    for i in range(rows):
        x = start + i
        if x <= 7:
            face.set(x, i, trim)
            if x + 1 <= 7:
                face.set(x + 1, i, k(role, 1))
    face.set(0, 0, trim)


def obi(g, pid: str, role: str = "D", y: float = 7.4, height: int = 3, knot: str | None = "back", accent: str | None = None,
        inflate: float = .15, seed: int = 4990):
    """A wide sash around the waist, an optional cord line, and a flat bow at the back or side."""
    box = g.piece(pid, "TORSO", (-4.6, y, -2.6), (9, height, 5), inflate=inflate)
    solid(box, role, "weave", seed, 2, edge=False)
    for face in box.sides:
        face.hline(0, face.w - 1, 0, k(role, 3))
        face.hline(0, face.w - 1, height - 1, k(role, 1))
        if accent:
            face.hline(0, face.w - 1, height // 2, accent)
    if knot == "back":
        bow = g.piece(f"{pid}_bow", "TORSO", (-2.5, -1, 0), (5, 3, 1), pivot=(0, y + 1.4, 2.75))
        solid(bow, role, "weave", seed + 1, 2)
        bow.back.vline(2, 0, 2, k(role, 1))
        for i, x in enumerate((-.9, .4)):
            end = g.piece(f"{pid}_end_{i}", "TORSO", (0, 0, 0), (1, 4 - i, 1), pivot=(x, y + 2.2, 2.9), rotation=(6, 0, 0),
                          motion="sway")
            solid(end, role, "weave", seed + 2 + i, 2)
    elif knot == "side":
        for i, (x, rz) in enumerate(((3.0, 6), (3.7, -8))):
            end = g.piece(f"{pid}_end_{i}", "TORSO", (-.5, 0, -.5), (1, 5 - i, 1), pivot=(x, y + height - .2, -2.75),
                          rotation=(0, 0, rz), motion="sway")
            solid(end, role, "weave", seed + 2 + i, 2)
    return box


def kimono_sleeves(g, prefix: str, role: str = "P", texture: str = "velvet", seed: int = 0, top: float = 2.5,
                   length: int = 5, trim: str | None = "A2", depth: int = 5, inflate: float = .15, hand_rows: int = 9):
    """Wide hanging kimono sleeves: arm cloth to `hand_rows`, then a loose box from the elbow."""
    out = []
    for side, _ in SIDES:
        bone = "RIGHT_ARM" if side == "right" else "LEFT_ARM"
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, role, texture, seed + (side == "left"), 2, 0, hand_rows)
        fabric(arm.top, role, texture, seed, 3)
        strip_fabric(sleeve, role, texture, seed + 2, 2, 0, 3)
        fabric(sleeve.top, role, texture, seed + 2, 3)
        box = g.piece(f"{prefix}_{side}", bone, (arm_x(side) - .5, top, -2.5), (5, length, depth), inflate=inflate)
        solid(box, role, texture, seed + 3 + (side == "left"), 2)
        if trim:
            for face in box.sides:
                face.hline(0, face.w - 1, length - 1, trim)
        box.bottom.fill(k(role, 0))
        out.append(box)
    return out


def hakama_legs(g, prefix: str, role: str = "D", seed: int = 0, flare: float = 6, length: int = 10, top: float = 0.5,
                pleats: bool = True):
    """Wide, pleated hakama legs: a loose box per leg, flaring a little outward, ending above the feet."""
    out = []
    for side, sign in SIDES:
        box = g.piece(f"{prefix}_{side}", leg_bone(side), (-2.5, 0, -2.6), (5, length, 5), pivot=(0, top, 0),
                      rotation=(0, 0, -flare * sign), inflate=.12)
        solid(box, role, "twill", seed + (sign > 0), 2)
        if pleats:
            for face in box.sides:
                for x in range(1, face.w, 2):
                    face.vline(x, 1, face.h - 2, k(role, 1))
                face.hline(0, face.w - 1, 0, k(role, 3))
        box.bottom.fill(k(role, 0))
        out.append(box)
    return out


def tabi(g, role: str = "S", sole: str = "K1", strap: str = "D2"):
    """Split-toe socks with straw sandals: pale feet, a dark thong strap and sole."""
    for side, _ in SIDES:
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, role, "plain", 4991, 3, 9, 11)
        leg.front.vline(2, 10, 11, k(role, 1))
        leg.front.set(1, 10, strap), leg.front.set(2, 10, strap)
        leg.bottom.fill(sole)
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, sole)
        pants.bottom.fill("K0")


# The clan crest used on formal wear: a ringed eye, drawn at double resolution.
CREST = ["..####..",
         ".#....#.",
         "#..##..#",
         "#.#..#.#",
         "#.#..#.#",
         "#..##..#",
         ".#....#.",
         "..####.."]


def crest(g, pid: str, role: str, ink: str, pivot=(0, 1.4, 2.05), seed: int = 4995):
    """The crest on a half-scale plate, stamped in `ink` on cloth of `role`."""
    from glyphs import stamp
    plate = g.piece(pid, "TORSO", (-4, 0, 0), (8, 8, 1), pivot=pivot, scale=(.5, .5, .5))
    for face in plate.faces:
        fabric(face, role, "velvet", seed, 2)
    stamp(plate.back, CREST, 0, 0, {"#": ink})
    return plate
