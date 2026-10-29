"""Fang Parka: the older tracker's heavy dark parka, a deep ruff of fur round the shoulders where the
hood lies, red trim stitched down both sides of the zip, toggled pockets low on the front and
fur-lined cuffs."""
from kit import sleeves
from kit_inuzuka import fur_box
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Fang Parka",
    "gender": "unisex",
    "description": "Heavy dark parka with a deep fur ruff at the shoulders, red trim by the zip, fur cuffs.",
    "tags": ["shinobi", "chunin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 8480, 2)
    cap(body, "P", texture="weave", seed=8480)
    strip_fabric(jacket, "P", "weave", 8481, 2, 2, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P0")
    f = jacket.front
    f.vline(4, 2, 11, "M3"), f.vline(3, 2, 11, "P0")
    f.vline(2, 2, 7, "A2"), f.vline(5, 2, 7, "A2")
    # Patch pockets with a toggle each.
    for x0 in (0, 5):
        f.hline(x0, x0 + 2, 8, "P3"), f.vline(x0, 8, 10, "P1"), f.vline(x0 + 2, 8, 10, "P1")
        f.set(x0 + 1, 9, "L3")
    for arm in sleeves(g, "P", "weave", 8482, 2, rows=(0, 9)):
        arm.strip.hline(0, arm.strip.w - 1, 4, "P1")
    for side, bone, x in (("right", "RIGHT_ARM", -3.0), ("left", "LEFT_ARM", -1.0)):
        cuff = g.piece(f"{side}_fur_cuff", bone, (x - .5, 8.4, -2.5), (5, 2, 5))
        fur_box(cuff, "S", 8483 + (side == "left"), 2)
    # The fur ruff: a thick collar ring and a deeper fold at the back where the hood lies.
    ruff = g.piece("ruff", "TORSO", (-5, -1.6, -3), (10, 3, 6), inflate=.05)
    fur_box(ruff, "S", 8486, 2)
    back = g.piece("ruff_back", "TORSO", (-4.5, 0, 0), (9, 4, 2), pivot=(0, 1.0, 2.2), rotation=(12, 0, 0))
    fur_box(back, "S", 8488, 2)
    hood = g.piece("hood", "TORSO", (-4, 0, 0), (8, 3, 1), pivot=(0, 4.6, 2.3), rotation=(8, 0, 0))
    solid(hood, "P", "weave", 8489, 2)
    hood.back.hline(0, 7, 2, "P1")
