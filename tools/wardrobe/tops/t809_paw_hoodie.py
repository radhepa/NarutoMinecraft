"""Paw Hoodie: the academy pup's pullover, a soft hoodie with the hood down, a big kangaroo pocket, red
drawstrings, and a paw print and two pup ears sewn on the hood."""
from kit import sleeves
from kit_inuzuka import paw
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Paw Hoodie",
    "gender": "unisex",
    "description": "Soft pullover hoodie, hood down with sewn pup ears, kangaroo pocket, a paw print on the back.",
    "tags": ["shinobi", "academy"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "plain", 8690, 2)
    cap(body, "P", seed=8690)
    f = body.front
    f.hline(1, 6, 6, "P3")
    for y in range(7, 10):
        f.hline(1, 6, y, "P2")
    f.vline(1, 7, 9, "P0"), f.vline(6, 7, 9, "P0")
    f.vline(3, 0, 3, "A2"), f.vline(4, 0, 3, "A2")
    f.set(3, 4, "S3"), f.set(4, 4, "S3")
    paw(body.back, 1, 4, "S3")
    strip_fabric(jacket, "P", "rib", 8691, 2, 10, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for arm in sleeves(g, "P", "plain", 8692, 2, rows=(0, 10)):
        arm.strip.hline(0, arm.strip.w - 1, 10, "P1")
    hood = g.piece("hood", "TORSO", (-4.5, 0, -1.5), (9, 4, 3), pivot=(0, -1.0, 3.0), rotation=(24, 0, 0))
    solid(hood, "P", "plain", 8693, 2)
    fabric(hood.top, "S", "plain", 8694, 2)
    hood.back.vline(4, 0, 3, "P1")
    for i, x in enumerate((-3.0, 3.0)):
        ear = g.piece(f"hood_ear_{i}", "TORSO", (-1, -2, 0), (2, 2, 1), pivot=(x, -1.0, 3.8), rotation=(24, 0, 0))
        solid(ear, "P", "plain", 8695 + i, 1, edge=False)
        ear.back.set(0, 1, "S3"), ear.back.set(1, 1, "S3")
