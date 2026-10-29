"""Scout Hoodie: a teal zip-up with the hood pushed back onto the shoulders, mustard trim at the
cuffs and hem, a kangaroo pocket and a small leaf crest on the back: the genin who goes ahead."""
from glyphs import LEAF, stamp
from kit import sleeves
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Scout Hoodie",
    "gender": "unisex",
    "description": "Teal zip-up hoodie with the hood down, mustard trim, a kangaroo pocket and a leaf crest.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "plain", 271, 2)
    cap(body, "P", seed=271)
    f = body.front
    f.vline(4, 0, 11, "S3"), f.vline(3, 0, 11, "P1")
    f.set(4, 0, "M4"), f.set(4, 1, "M2")
    # Kangaroo pocket, split by the zip: a stitched top seam and a dark opening down each side.
    for x in (1, 2, 5, 6):
        for y in (7, 8, 9):
            f.set(x, y, "P3" if y == 7 else "P2")
        f.set(x, 6, "P1")
    for y in (7, 8, 9):
        f.set(1, y, "P0"), f.set(6, y, "P0")
    strip_fabric(jacket, "A", "plain", 272, 2, 10, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "A1")
    jacket.front.set(4, 10, "S3"), jacket.front.set(4, 11, "S2")
    for arm in sleeves(g, "P", "plain", 273, 2, rows=(0, 9)):
        arm.strip.hline(0, arm.strip.w - 1, 9, "P1")
    for side in ("right", "left"):
        cuff = g.part(f"{side}_sleeve")
        strip_fabric(cuff, "A", "plain", 274, 2, 9, 10)
        cuff.strip.hline(0, cuff.strip.w - 1, 10, "A1")
    # The hood, pushed back: a deep fold of cloth lying across the shoulders and upper back.
    hood = g.piece("hood", "TORSO", (-4.5, 0, -1.5), (9, 4, 3), pivot=(0, -1.2, 3.0), rotation=(24, 0, 0))
    solid(hood, "P", "plain", 275, 2)
    fabric(hood.top, "A", "plain", 276, 1)   # the lining shows inside the opening
    hood.top.hline(0, 8, 0, "A3"), hood.top.hline(0, 8, 2, "A3")
    hood.back.hline(0, 8, 3, "P1"), hood.back.vline(4, 0, 3, "P1")
    for face in (hood.right, hood.left):
        face.hline(0, face.w - 1, 0, "A2")
    crest = g.piece("back_leaf", "TORSO", (-4, 0, 0), (8, 8, 1), pivot=(0, 4.4, 2.05), scale=(.5, .5, .5))
    fabric(crest.back, "P", "plain", 277, 2)
    stamp(crest.back, LEAF, 0, 0, {"#": "A2"})
    for face in (crest.top, crest.bottom, crest.right, crest.left, crest.front):
        face.fill("P2")
