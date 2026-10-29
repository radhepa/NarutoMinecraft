"""Tobari building blocks: the night-curtain crest, the layered drape mantle with its hood worn down,
the muffler wound round the neck, the small paper-lantern charm and the soft-soled split-toe boots of
the clan's scouts and night watch.

The family dresses in P (deep indigo, charcoal or moon-grey) and S (moon-grey), with one warm accent:
A is the lantern-amber of the charm, the crest's moon and a single trim line, never more."""
from glyphs import stamp
from paint import cap, fabric, k, solid, strip_fabric

# The Tobari crest (an invention, drawn at double resolution): a round moon seen between two curtains
# drawn back and tied, under the curtain rod. 'r' rod, 'c' curtain, 'f' a fold, 'o' the moon.
CREST = ["rrrrrrrrrrrrrr",
         "ccf........fcc",
         "cf...oooo...fc",
         "c...oooooo...c",
         "c..oooooooo..c",
         "cf.oooooooo.fc",
         "cf.oooooooo.fc",
         "c..oooooooo..c",
         "cf..oooooo..fc",
         "ccf..oooo..fcc",
         "cccf......fccc",
         "ccccff..ffcccc"]

CREST_INK = {"r": "S4", "c": "S3", "f": "S2", "o": "A3"}

# A paper lantern seen from the front, for a half-scale tag: 'K' caps, 'a' paper, 'r' ribs, 'l' glow.
LANTERN = [".KK.",
           "aaaa",
           "rrrr",
           "alla",
           "rrrr",
           "aaaa",
           ".KK."]


def decal(g, pid: str, ground: str, pivot, bone: str = "TORSO", face: str = "back", pad: int = 1, ink=None):
    """The crest on a double-resolution flat plate, the rest filled with `ground`."""
    w, h = len(CREST[0]) + 2 * pad, len(CREST) + 2 * pad
    z0 = 0 if face == "back" else -1
    box = g.piece(pid, bone, (-w / 2, 0, z0), (w, h, 1), pivot=pivot, scale=(.5, .5, .5))
    for f in box.faces:
        f.fill(ground)
    rows = [r[::-1] for r in CREST] if face == "back" else CREST
    stamp(getattr(box, face), rows, pad, pad, ink or CREST_INK)
    return box


def pleats(face, role: str, base: int = 2, step: int = 2, start: int = 1, hem: bool = True):
    """Curtain pleats: a shaded fold every `step` texels from the second row down, a lit top edge and
    a dark hem."""
    for x in range(start, face.w, step):
        face.vline(x, 1, face.h - 1, k(role, base - 1))
    face.hline(0, face.w - 1, 0, k(role, base + 1))
    if hem:
        face.hline(0, face.w - 1, face.h - 1, k(role, base - 2))


def mantle(g, prefix: str = "mantle", role: str = "P", texture: str = "twill", seed: int = 25950, length: int = 6,
           tiers: int = 2, trim: str | None = "A2", hood: bool = True, open_front: bool = False):
    """The layered drape mantle: a pleated lower cape round chest and back, a shorter upper tier over
    the shoulders in a lighter shade (and its own capelet on each arm, so it swings with them), the
    hood worn down on the back. `trim` runs one thin line along the lower tier's hem."""
    out = []
    lower = g.piece(f"{prefix}_lower", "TORSO", (-4.5, 0, -2.5), (9, length, 5), pivot=(0, -.2, 0), inflate=.3)
    solid(lower, role, texture, seed, 2)
    for face in lower.sides:
        pleats(face, role)
        if trim:
            face.hline(0, face.w - 1, face.h - 2, trim)
    lower.bottom.fill(k(role, 0))
    if open_front:
        lower.front.vline(4, 1, length - 1, k(role, 0))
    out.append(lower)
    if tiers > 1:
        upper = g.piece(f"{prefix}_upper", "TORSO", (-4.5, 0, -2.5), (9, 3, 5), pivot=(0, -.4, 0), inflate=.55)
        solid(upper, role, texture, seed + 1, 2)
        for face in upper.sides:
            pleats(face, role, base=2, step=3, start=2)
            face.hline(0, face.w - 1, 0, k(role, 3))
        upper.bottom.fill(k(role, 0))
        out.append(upper)
    for side, bone, x in (("right", "RIGHT_ARM", -3.6), ("left", "LEFT_ARM", -.4)):
        cape = g.piece(f"{prefix}_{side}_capelet", bone, (x, -2.4, -2.5), (4, 4 if tiers > 1 else 5, 5), inflate=.3)
        solid(cape, role, texture, seed + 2 + (side == "left"), 2)
        for face in cape.sides:
            pleats(face, role, step=2)
        cape.bottom.fill(k(role, 0))
        out.append(cape)
    if hood:
        out.append(hood_down(g, f"{prefix}_hood", role, texture, seed + 4))
    return out


def hood_down(g, pid: str = "hood", role: str = "P", texture: str = "twill", seed: int = 25955, lining: str = "K"):
    """A soft hood worn down: a fold of cloth lying across the shoulder blades, its dark lining showing
    along the top, ending in a rounded point."""
    hood = g.piece(pid, "TORSO", (-4, 0, -1), (8, 4, 2), pivot=(0, -1.2, 3.1), rotation=(16, 0, 0))
    solid(hood, role, texture, seed, 2)
    fabric(hood.top, lining, "plain", seed, 1)
    hood.top.hline(0, 7, 0, k(role, 3))
    hood.back.vline(4, 1, 3, k(role, 1))
    tip = g.piece(f"{pid}_point", "TORSO", (-1.5, 4, -1), (3, 1, 2), pivot=(0, -1.2, 3.1), rotation=(16, 0, 0))
    solid(tip, role, texture, seed + 1, 2, edge=False)
    return hood


def muffler(g, prefix: str = "muffler", role: str = "S", texture: str = "knit", seed: int = 25960, tails: str = "front",
            stripe: str | None = None, base: int = 2):
    """A thick muffler worn down round the neck: a fat wrap on the collarbones and its ends hanging,
    one down the chest (`tails` "front"), both down the back ("back") or none (None)."""
    wrap = g.piece(prefix, "TORSO", (-4.5, -1.8, -2.7), (9, 3, 5), inflate=.2)
    solid(wrap, role, texture, seed, base + 1, edge=False)
    for face in wrap.sides:
        face.hline(0, face.w - 1, 2, k(role, base - 1))
        face.hline(0, face.w - 1, 0, k(role, base + 2))
    wrap.bottom.fill(k(role, 0))
    ends = {"front": [(-2.1, -3.1, 4, 6), (-0.6, -3.0, -6, 5)], "back": [(-1.2, 3.1, 6, 7), (1.0, 3.2, -4, 6)]}
    for i, (x, z, rz, n) in enumerate(ends.get(tails, [])):
        end = g.piece(f"{prefix}_end_{i}", "TORSO", (-1, 0, -.5), (2, n, 1), pivot=(x, 1.0, z), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, role, texture, seed + 1 + i, base + (i == 0))
        for face in end.sides:
            if stripe:
                face.hline(0, face.w - 1, n - 2, stripe)
            face.hline(0, face.w - 1, n - 1, k(role, base - 1))
    return wrap


def lantern(g, prefix: str = "lantern", pivot=(2.6, 9.6, -2.9), bone: str = "TORSO", cord: str = "K"):
    """The clan's paper-lantern charm: a short cord from the sash, a round amber paper lantern with
    dark ribs and caps and a little dark tassel, swaying on the hip. Built at half scale."""
    half = (.5, .5, .5)
    string = g.piece(f"{prefix}_cord", bone, (-.5, 0, -.5), (1, 2, 1), pivot=pivot, scale=half, motion="sway")
    solid(string, cord, "smooth", 25970, 2, edge=False)
    body = g.piece(f"{prefix}_body", bone, (-1.5, 2, -1.5), (3, 4, 3), pivot=pivot, scale=half, motion="sway")
    for face in body.sides:
        fabric(face, "A", "plain", 25971, 3)
        face.hline(0, 2, 0, "A2"), face.set(1, 1, "A4"), face.hline(0, 2, 2, "A1"), face.hline(0, 2, 3, "A2")
    body.top.fill(k(cord, 1)), body.bottom.fill(k(cord, 1))
    for i, y in enumerate((1.5, 6)):
        rim = g.piece(f"{prefix}_rim_{i}", bone, (-1, y, -1), (2, 1, 2), pivot=pivot, scale=half, motion="sway")
        solid(rim, cord, "smooth", 25972 + i, 2, edge=False)
    tassel = g.piece(f"{prefix}_tassel", bone, (-.5, 7, -.5), (1, 2, 1), pivot=pivot, scale=half, motion="sway")
    solid(tassel, cord, "smooth", 25974, 1, edge=False)
    return body


def lantern_tag(face, x0: int, y0: int, cord: str = "K"):
    """The lantern drawn flat on a face (one texel per pixel), for tops too small for the charm."""
    stamp(face, LANTERN, x0, y0, {"K": k(cord, 1), "a": "A3", "r": "A1", "l": "A4"})


def split_toe_boots(g, top: int = 6, role: str = "K", base: int = 2, tie: str | None = "L2", sole: str = "S1"):
    """Soft-soled split-toe boots (jika-tabi) from the shin to the toe, fastened up the inside with
    a row of clasps, a tie round the top and a pale, thin sole: the split shows as a dark notch at the
    front of each toe."""
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, role, "smooth", 25980 + (side == "left"), base, top, 11)
        leg.strip.hline(0, leg.strip.w - 1, 11, sole)
        inner = leg.left if side == "right" else leg.right
        for y in range(top + 1, 11, 2):
            inner.set(1, y, "M3")
        split = 1 if side == "right" else 2
        leg.front.vline(split, 10, 11, k(role, 0))
        leg.front.set(split, 11, k(role, 0))
        leg.bottom.fill(sole)
        if tie:
            leg.strip.hline(0, leg.strip.w - 1, top, tie)
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, sole)
        pants.front.set(split, 11, k(role, 0))
        pants.front.set(split, 10, k(role, base - 1))
        pants.bottom.fill(sole)


def shin_wraps(g, top: int, bottom: int, role: str = "S"):
    """Close dark-and-grey shin wraps wound on a slant, the night watch's answer to white bandages."""
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        for y in range(top, bottom + 1):
            for x in range(leg.strip.w):
                leg.strip.set(x, y, k(role, 1) if (x + y * 2) % 4 == 0 else k(role, 2))


def sash(g, pid: str, role: str = "D", y: float = 9.2, height: int = 2, knot: str = "left", base: int = 2):
    """A wide cloth sash round the waist, knotted at one hip with a short end hanging."""
    box = g.piece(pid, "TORSO", (-4.5, y, -2.5), (9, height, 5), inflate=.12)
    solid(box, role, "weave", 25990, base, edge=False)
    for face in box.sides:
        face.hline(0, face.w - 1, 0, k(role, base + 1))
    sign = 1 if knot == "left" else -1
    end = g.piece(f"{pid}_end", "TORSO", (-.5, 0, -.5), (2, 4, 1), pivot=(2.6 * sign, y + 1, -2.9),
                  rotation=(0, 0, -8 * sign), motion="sway")
    solid(end, role, "weave", 25991, base)
    return box


def plain_body(g, role: str, texture: str = "weave", seed: int = 0, base: int = 2):
    body = g.part("body")
    strip_fabric(body, role, texture, seed, base)
    cap(body, role, texture=texture, seed=seed)
    return body
