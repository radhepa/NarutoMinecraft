"""Fur Hood Jacket: the clan's grey zip jacket, long-sleeved and roomy, its hood pushed back with a
thick ruff of pale fur round the rim, red fang triangles on the sleeves and a dark ribbed hem: the
genin who runs with a pup inside the jacket."""
from kit import sleeves
from kit_inuzuka import fang, fur_box, fur_edge
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Fur Hood Jacket",
    "gender": "unisex",
    "description": "Grey zip jacket, the hood pushed back with a pale fur ruff, red fangs on the sleeves.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "plain", 8450, 2)
    cap(body, "P", seed=8450)
    f = body.front
    f.vline(4, 0, 11, "M3"), f.vline(3, 0, 11, "P1")
    f.set(4, 0, "M4")
    # Hand pockets either side of the zip.
    f.vline(1, 6, 8, "P0"), f.vline(6, 6, 8, "P0")
    f.hline(1, 2, 6, "P3"), f.hline(5, 6, 6, "P3")
    strip_fabric(jacket, "K", "rib", 8451, 2, 10, 11)
    jacket.front.set(4, 10, "M3"), jacket.front.set(4, 11, "M2")
    for arm in sleeves(g, "P", "plain", 8452, 2, rows=(0, 9)):
        arm.strip.hline(0, arm.strip.w - 1, 9, "P1")
    for side in ("right", "left"):
        arm, cuff = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(cuff, "K", "rib", 8454, 2, 9, 10)
        # A red fang on the outer shoulder.
        fang(arm.right if side == "right" else arm.left, 2 if side == "right" else 1, 1, "A3", h=3)
    # The hood, pushed back across the shoulders, and the fur ruff round its rim.
    hood = g.piece("hood", "TORSO", (-4.5, 0, -1.5), (9, 4, 3), pivot=(0, -1.0, 3.0), rotation=(26, 0, 0))
    solid(hood, "P", "plain", 8456, 2)
    fabric(hood.top, "P", "plain", 8456, 1)
    hood.back.vline(4, 0, 3, "P1")
    ruff = g.piece("hood_ruff", "TORSO", (-5, -1, -2), (10, 2, 4), pivot=(0, -.6, 2.6), rotation=(26, 0, 0))
    fur_box(ruff, "S", 8457, 2)
    for face in (hood.right, hood.left):
        fur_edge(face, 0, "S", 8458, 2, 2)
