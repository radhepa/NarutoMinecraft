"""Academy and genin building blocks: the everyday clothes of the village's young ninja.

Tees, hoodies and track tops share a few shapes: a short or long sleeve on the base arm, ribbed
trim bands, a hood pushed back onto the shoulders, a half-scale crest on the back, forearm wraps.
Bottoms share a waist, a leg length and a turned hem. Everything paints key colors, so a piece
follows whichever palette the resident draws, and every piece here mixes with the other
collections: tops paint the whole torso, bottoms the waist rows, and belt pieces start with
"waist" so a long top can hide them."""
from __future__ import annotations

from glyphs import LEAF, stamp
from kit import SIDES, arm_bone, arm_x, leg_bone
from kit_shinobi import bandage
from paint import cap, fabric, k, solid, strip_fabric


# -- tops ------------------------------------------------------------------------------------
def shirt(g, role: str, texture: str = "plain", seed: int = 0, sleeve: int = 3, sleeve_role: str | None = None,
          trim: str | None = None, base: int = 2):
    """A shirt on the base body and arms: body rows 0-11, sleeves down to arm row `sleeve` (0 for
    none, 11 for full length) with an optional trim band at the sleeve end and the hem."""
    body = g.part("body")
    strip_fabric(body, role, texture, seed, base)
    cap(body, role, texture=texture, seed=seed, base=base)
    if trim:
        body.strip.hline(0, body.strip.w - 1, 11, trim)
    arms = []
    for side in SIDES:
        arm = g.part(f"{side}_arm")
        if sleeve > 0:
            strip_fabric(arm, sleeve_role or role, texture, seed + 2 + (side == "left"), base, 0, sleeve)
            fabric(arm.top, sleeve_role or role, texture, seed + 2, base + 1)
            if trim:
                arm.strip.hline(0, arm.strip.w - 1, sleeve, trim)
        arms.append(arm)
    return body, arms


def ribbed(box, rows, role: str, base: int = 2):
    """Ribbed knit trim around a box: alternating columns light and shaded."""
    for y in rows:
        for x in range(box.strip.w):
            box.strip.set(x, y, k(role, base - (x % 2)))


def stripes(box, rows, key: str):
    """Horizontal stripes right round a box, one row each."""
    for y in rows:
        box.strip.hline(0, box.strip.w - 1, y, key)


def side_stripe(arm, side: str, rows, key: str, double: str | None = None):
    """A track stripe down the outside of a sleeve or trouser leg; `double` adds a second line."""
    outer = arm.right if side == "right" else arm.left
    x = 1 if side == "right" else 2
    outer.vline(x, rows[0], rows[1], key)
    if double:
        outer.vline(x + (1 if side == "right" else -1), rows[0], rows[1], double)


def zip_front(face, top: int = 0, bottom: int = 11, tape: str = "S3", fold: str | None = None):
    face.vline(4, top, bottom, tape)
    if fold:
        face.vline(3, top, bottom, fold)
    face.set(4, top, "M4"), face.set(4, top + 1, "M2")


def zip_pull(g, seed: int, y: float = 1.0):
    pull = g.piece("zip_pull", "TORSO", (0, 0, -1), (1, 2, 1), pivot=(.1, y, -2.05), scale=(.5, .5, .5))
    solid(pull, "M", "plain", seed, 3, edge=False)


def hood_down(g, role: str, lining: str, seed: int, depth: float = 3.0, tilt: float = 24):
    """A hood pushed back: a fold of cloth across the shoulders and upper back, lining showing."""
    hood = g.piece("hood", "TORSO", (-4.5, 0, -1.5), (9, 4, 3), pivot=(0, -1.2, depth), rotation=(tilt, 0, 0))
    solid(hood, role, "plain", seed, 2)
    fabric(hood.top, lining, "plain", seed + 1, 2)
    hood.top.hline(0, 8, 0, k(lining, 3))
    hood.back.hline(0, 8, 3, k(role, 1)), hood.back.vline(4, 0, 3, k(role, 1))
    for face in (hood.right, hood.left):
        face.hline(0, face.w - 1, 0, k(lining, 2))
    return hood


def drawstrings(g, key: str, seed: int, y: float = .2, length: int = 4):
    for i, x in enumerate((-1.2, 1.2)):
        cord = g.piece(f"drawstring_{i}", "TORSO", (-.5, 0, -.5), (1, length, 1), pivot=(x, y, -2.45),
                       scale=(.5, .5, .5), motion="flap_front")
        solid(cord, key[0], "plain", seed + i, int(key[1]), edge=False)
        cord.front.set(0, length - 1, "M3")


def back_crest(g, role: str, mark: str, seed: int, y: float = 3.0, z: float = 2.05, rows=LEAF, pid: str = "back_crest"):
    """A half-scale crest sewn on the back: a cloth patch in `role` with the mark in `mark`."""
    w, h = len(rows[0]), len(rows)
    crest = g.piece(pid, "TORSO", (-w / 2, 0, 0), (w, h, 1), pivot=(0, y, z), scale=(.5, .5, .5))
    fabric(crest.back, role, "plain", seed, 2)
    stamp(crest.back, rows, 0, 0, {"#": mark})
    for face in (crest.top, crest.bottom, crest.right, crest.left, crest.front):
        face.fill(k(role, 2))
    return crest


def forearm_wraps(g, top: int = 6, bottom: int = 10, layer: str = "arm"):
    """Bandage wound round each forearm, with a tucked end."""
    for side in SIDES:
        arm = g.part(f"{side}_{layer}")
        bandage(arm.strip, 0, top, arm.strip.w - 1, bottom)
        arm.strip.hline(0, arm.strip.w - 1, top, "S2")


def sash(g, role: str, seed: int, y: float = 9.4, knot_x: float = 1.6, tails: int = 2):
    """A cloth sash round the waist, knotted at the hip with hanging tails."""
    band = g.piece("sash", "TORSO", (-4.6, y, -2.6), (9, 2, 5), inflate=.05)
    solid(band, role, "weave", seed, 2, edge=False)
    for face in band.sides:
        face.hline(0, face.w - 1, 0, k(role, 3))
    knot = g.piece("sash_knot", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(knot_x, y, -3.1))
    solid(knot, role, "weave", seed + 1, 3, edge=False)
    for i in range(tails):
        tail = g.piece(f"sash_tail_{i}", "TORSO", (0, 0, 0), (1, 4 - i, 1), pivot=(knot_x + .1 + i, y + 1.8, -3.0),
                       rotation=(0, 0, 8 - 16 * i), motion="flap_front")
        solid(tail, role, "weave", seed + 2 + i, 2)


def sleeve_roll(g, role: str, y: float, seed: int, base: int = 2):
    """A turned-up cuff ring round each upper arm, for short sleeves with a rolled edge."""
    for side in SIDES:
        ring = g.piece(f"{side}_cuff", arm_bone(side), (arm_x(side) - .5, y, -2.5), (5, 1, 5))
        solid(ring, role, "plain", seed + (side == "left"), base, edge=False)
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, k(role, base + 1))


# -- bottoms ---------------------------------------------------------------------------------
def waist(g, role: str, texture: str = "twill", seed: int = 0, band: str | None = None, base: int = 2):
    """The waist rows 9-11 of the body: cloth with a lit waistband on row 9."""
    body = g.part("body")
    strip_fabric(body, role, texture, seed, base, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, band or k(role, base + 1))
    fabric(body.bottom, role, texture, seed, base - 1)
    return body


def leg_cloth(g, role: str, texture: str = "twill", seed: int = 0, rows=(0, 5), base: int = 2):
    """Both legs from rows[0] to rows[1] (row 5 is the knee, row 9 mid-shin, 11 the ankle)."""
    legs = []
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, role, texture, seed + (side == "left"), base, rows[0], rows[1])
        if rows[0] == 0:
            fabric(leg.top, role, texture, seed, base)
        legs.append(leg)
    return legs


def turned_hem(g, prefix: str, y: float, role: str, seed: int, height: int = 1, base: int = 2, texture: str = "twill"):
    """A turned-up hem ring round each leg at leg-local height `y`."""
    rings = []
    for side in SIDES:
        ring = g.piece(f"{side}_{prefix}", leg_bone(side), (-2.5, y, -2.5), (5, height, 5))
        solid(ring, role, texture, seed + (side == "left"), base, edge=False)
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, k(role, base + 1))
            if height > 1:
                face.hline(0, face.w - 1, height - 1, k(role, base - 1))
        rings.append(ring)
    return rings


def waist_pouch(g, seed: int, role: str = "L", x: float = -1.5):
    pouch = g.piece("waist_pouch", "TORSO", (0, 0, 0), (3, 2, 1), pivot=(x, 9.4, 2.2))
    solid(pouch, role, "leather", seed, 2)
    pouch.back.hline(0, 2, 0, k(role, 3))
    return pouch


def holster(g, seed: int, y: float = 1.2, strap: str | None = "S"):
    """A kunai holster on the right thigh, over a wrap or a strap ring."""
    if strap:
        wrap = g.piece("thigh_wrap", "RIGHT_LEG", (-2.45, y + .2, -2.45), (5, 2, 5))
        solid(wrap, strap, "plain", seed, 3, edge=False)
        for face in wrap.sides:
            face.hline(0, face.w - 1, 1, k(strap, 2))
    box = g.piece("holster", "RIGHT_LEG", (0, 0, 0), (1, 3, 2), pivot=(-3.0, y, -1.0))
    solid(box, "K", "leather", seed + 1, 3)
    box.right.set(0, 0, "M3"), box.right.set(1, 0, "M2")


def shin_wraps(g, top: int = 6, bottom: int = 9, role: str = "S"):
    """Wraps wound on a slant round each shin, in any cloth role."""
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        for y in range(top, bottom + 1):
            for x in range(leg.strip.w):
                leg.strip.set(x, y, k(role, 2) if (x + y * 2) % 5 == 0 else k(role, 3))
