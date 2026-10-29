"""Akimichi building blocks: the 食 ("food") crest on a disc, lacquered armor lames that round out
the torso, shoulder sode, padded quilting, snack pouches and the sake gourd, and the curly puffs
and wild outward spikes of the clan's hair.

Bodies are all one size, so the clan's bulk comes from layers: rings of plates a little wider and
deeper than the torso, padding over the shoulders and thick sashes at the waist."""
from __future__ import annotations

from anime import cel_box
from glyphs import stamp
from kit import arm_bone, arm_x
from paint import curls_box, k, rnd, solid

# 食, "food": a peaked roof with a dot under it over a stacked box, the left stroke running down
# into a hooked foot and a long sweep to the lower right. 14 x 15, drawn at triple resolution
# with two-texel strokes so the roof survives at a distance.
SHOKU = ["......##......",
         ".....####.....",
         "....##..##....",
         "..###....###..",
         "###...##...###",
         "..............",
         "...########...",
         "...##....##...",
         "...########...",
         "...##....##...",
         "...########...",
         "...##..##.....",
         "...##...##....",
         "...##.#..###..",
         "..#####...###."]


def shoku_disc(g, pid: str, pivot, bone: str = "TORSO", ground: str = "P2", disc: str = "S", ink: str = "K1",
               rim: str | None = None, side: str = "front", rotation=(0, 0, 0)):
    """The 食 crest in a round disc, 18 x 18 texels at triple resolution (6 model pixels across).
    `pivot` is the centre of the disc's face; `ground` paints the corners outside the disc so they
    melt into the garment beneath, `rim` rings the disc in another key."""
    box = g.piece(pid, bone, (-9, -9, 0 if side == "back" else -1), (18, 18, 1), pivot=pivot, rotation=rotation,
                  scale=(1 / 3, 1 / 3, 1 / 3))
    for f in box.faces:
        f.fill(ground)
    face = box.back if side == "back" else box.front
    for y in range(18):
        for x in range(18):
            d = ((x - 8.5) ** 2 + (y - 8.5) ** 2) ** .5
            if d <= 8.9:
                face.set(x, y, k(disc, 3 if d < 7.6 else 2))
                if rim and d > 7.9:
                    face.set(x, y, rim)
    rows = SHOKU if side == "front" else [r[::-1] for r in SHOKU]
    stamp(face, rows, 2, 1, {"#": ink})
    return box


def lames(g, prefix: str, rows, role: str = "P", texture: str = "smooth", seed: int = 6993, lacing: str | None = "A2",
          width: int = 9, depth: int = 5, front: float = -2.5):
    """Lacquered plates ringing the torso: rows are (y, height, inflate). Each lame gets a lit upper
    edge, a dark lower edge and, with `lacing`, the cord stitches that hold samurai plates together."""
    boxes = []
    for i, (y, h, inflate) in enumerate(rows):
        box = g.piece(f"{prefix}_{i}", "TORSO", (-width / 2, y, front), (width, h, depth), inflate=inflate)
        solid(box, role, texture, seed + i, 2, edge=False)
        for face in box.sides:
            face.hline(0, face.w - 1, 0, k(role, 3))
            face.hline(0, face.w - 1, h - 1, k(role, 1))
            if lacing and h >= 2:
                for x in range(1, face.w - 1, 3):
                    face.set(x, h - 1, lacing)
        boxes.append(box)
    return boxes


def sode(g, prefix: str, role: str = "P", tiers: int = 2, seed: int = 6994, lacing: str | None = "A2", stud: str = "M3",
         flare: float = 0.0):
    """Shoulder sode: stacked plates over each upper arm, the top tier capping the shoulder."""
    out = []
    for side in ("right", "left"):
        for t in range(tiers):
            y = -2.7 + t * 1.8
            box = g.piece(f"{side}_{prefix}_{t}", arm_bone(side), (arm_x(side) - .5, y, -2.5), (5, 2, 5),
                          inflate=.15 + .05 * t + flare * t, rotation=(0, 0, 0))
            solid(box, role, "smooth", seed + t * 2 + (side == "left"), 2, edge=False)
            for face in box.sides:
                face.hline(0, face.w - 1, 0, k(role, 3)), face.hline(0, face.w - 1, 1, k(role, 1))
                if lacing:
                    face.set(1, 1, lacing), face.set(face.w - 2, 1, lacing)
            if t == 0 and stud:
                outer = box.right if side == "right" else box.left
                outer.set(2, 0, stud)
            out.append(box)
    return out


def quilt(face, role: str, seed: int, base: int = 2, x0: int = 0, y0: int = 0, w: int | None = None, h: int | None = None):
    """Thick padding: horizontal channels stitched every two rows, each puffed in the middle."""
    w = face.w - x0 if w is None else w
    h = face.h - y0 if h is None else h
    for y in range(y0, y0 + h):
        for x in range(x0, x0 + w):
            s = base + (1 if (y - y0) % 2 == 0 else 0)
            if (y - y0) % 2 == 1 and rnd(x, y, seed) < .25:
                s -= 1
            face.set(x, y, k(role, s))


def snack_pouch(g, pid: str, pivot, role: str = "A", size=(2, 3, 1), rotation=(0, 0, 0), bone: str = "TORSO",
                seed: int = 6995, motion: str = "none"):
    """A crinkled snack bag: a crimped top edge, a bright label band and a little tear notch."""
    w, h, d = size
    box = g.piece(pid, bone, (-w / 2, 0, -d / 2), size, pivot=pivot, rotation=rotation, motion=motion)
    solid(box, role, "smooth", seed, 2)
    for face in box.sides:
        face.hline(0, face.w - 1, 0, k(role, 4))
        if h >= 3:
            face.hline(0, face.w - 1, 1, "S3")
    return box


def gourd(g, pid: str, pivot, bone: str = "TORSO", role: str = "L", cord: str = "A2", rotation=(0, 0, 12),
          motion: str = "none", seed: int = 6996):
    """A sake gourd on a cord: a small neck, a waist tied with the cord and a fat bottom bulb."""
    parts = [((-.5, -1, -.5), (1, 1, 1)), ((-1, 0, -1), (2, 2, 2)), ((-.5, 2, -.5), (1, 1, 1)), ((-1.5, 3, -1.5), (3, 3, 3))]
    boxes = []
    for i, (o, s) in enumerate(parts):
        box = g.piece(f"{pid}_{i}", bone, o, s, pivot=pivot, rotation=rotation, motion=motion)
        solid(box, role, "smooth", seed + i, 3 if i % 2 else 2)
        if i == 2:
            box.fill(cord)
        boxes.append(box)
    stopper = g.piece(f"{pid}_stopper", bone, (-.5, -2, -.5), (1, 1, 1), pivot=pivot, rotation=rotation, motion=motion)
    stopper.fill(cord)
    return boxes


# -- hair --------------------------------------------------------------------------------------
def puff(g, pid: str, pivot, size=(4, 4, 4), rotation=(0, 0, 0), seed: int = 6997, base: int = 2, motion: str = "none"):
    """A round curly puff: a box of tight coils with the top lit, centred on `pivot`."""
    w, h, d = size
    box = g.piece(pid, "HEAD", (-w / 2, -h / 2, -d / 2), size, pivot=pivot, rotation=rotation, motion=motion)
    curls_box(box, seed, base)
    return box


def flick(g, pid: str, pivot, rotation, segments=((3, 2), (2, 2), (1, 1)), depth: int = 2, seed: int = 6998,
          base: int = 2, motion: str = "none"):
    """A wild spike growing outward from the head along local +y, wide at the root to a point."""
    y = 0.0
    for i, (w, h) in enumerate(segments):
        box = g.piece(f"{pid}_{i}", "HEAD", (-w / 2, y, -depth / 2), (w, h, depth), pivot=pivot, rotation=rotation,
                      motion=motion)
        cel_box(box, seed + i * 5, base + (1 if i == 0 else 0), None, top_delta=1)
        y += h

