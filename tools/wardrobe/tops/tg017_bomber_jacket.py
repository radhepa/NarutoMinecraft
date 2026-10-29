"""Bomber Jacket: a short padded jacket half unzipped over a tee, with striped rib knit at the collar,
cuffs and hem and a leaf patch on the left sleeve: the genin who borrowed an older sibling's jacket."""
from glyphs import LEAF, stamp
from kit_academy import shirt
from paint import fabric, k, strip_fabric

META = {
    "name": "Bomber Jacket",
    "gender": "unisex",
    "description": "Short padded jacket half unzipped over a tee, striped rib trim, a leaf patch on the sleeve.",
    "tags": ["shinobi", "genin"],
}


def rib(box, rows):
    for y in rows:
        for x in range(box.strip.w):
            box.strip.set(x, y, "A2" if len(rows) > 1 and y == rows[len(rows) // 2] else k("K", 2 - x % 2))


def build(g):
    body, arms = shirt(g, "S", "plain", 31240, sleeve=0)
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "smooth", 31241, 2)
    fabric(jacket.top, "P", "smooth", 31241, 3)
    for y in (3, 6):
        jacket.strip.hline(0, jacket.strip.w - 1, y, "P1")
    f = jacket.front
    for y in range(6):
        f.clear(3, y), f.clear(4, y)
    f.vline(2, 0, 5, "P3"), f.vline(5, 0, 5, "P1")
    f.vline(4, 6, 9, "M3"), f.set(4, 6, "M4")
    jacket.top.rect(2, 0, 4, 4, None)
    rib(jacket, (9, 10, 11))
    jacket.front.set(4, 9, "M3")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "smooth", 31242 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "smooth", 31242, 3)
        strip_fabric(sleeve, "P", "smooth", 31244, 2, 7, 10)
        rib(sleeve, (8, 9, 10))
    patch = g.piece("sleeve_patch", "LEFT_ARM", (0, 0, -4), (1, 8, 8), pivot=(3.25, .4, 0), scale=(.5, .5, .5))
    for face in patch.faces:
        face.fill("P2")
    fabric(patch.left, "S", "plain", 31245, 2)
    stamp(patch.left, LEAF, 0, 0, {"#": "A2"})
    collar = g.piece("collar", "TORSO", (-4.5, -1.2, -2.7), (9, 1, 5), inflate=.1)
    rib(collar, (0,))
    for face in (collar.top, collar.bottom):
        face.fill("K2")
