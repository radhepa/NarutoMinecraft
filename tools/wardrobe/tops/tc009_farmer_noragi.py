"""Farmer's Noragi: the field jacket mended season after season, indigo cotton patched in other
blues and creams, sashiko running stitch over the shoulders, a rope belt and a towel round the neck."""
from kit_kurama import wrap_front
from kit_market import patch, sashiko, sleeves, towel_at_neck
from paint import cap, solid, strip_fabric

META = {
    "name": "Farmer's Noragi",
    "gender": "unisex",
    "description": "Patched indigo field jacket with sashiko stitching, a rope belt and a towel at the neck.",
    "tags": ["civilian", "jacket", "work", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 36180, 2)
    cap(body, "P", seed=36180)
    for face in body.sides:
        sashiko(face, "P4", 4, rows=range(0, 4))
    wrap_front(body.front, "P4", "P1", rows=8, start=1)
    patch(body.front, 5, 5, 2, 2, "S", 2), patch(body.back, 1, 6, 3, 3, "D", 2, stitch="S3")
    patch(body.right, 1, 7, 2, 2, "A", 1)
    sleeves(g, "P", "weave", 36181, rows=(0, 10))
    for side in ("right", "left"):
        sleeve = g.part(f"{side}_sleeve")
        sashiko(sleeve.strip, "P4", 4, rows=range(0, 3))
    patch(g.part("left_sleeve").front, 0, 6, 3, 2, "D", 2, stitch="S3")
    rope = g.piece("rope_belt", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.0, 0), inflate=.15)
    solid(rope, "L", "weave", 36183, 3, edge=False)
    for face in rope.sides:
        face.paint(lambda x, y, cur: "L3" if x % 2 else "L2")
    towel_at_neck(g, "S", 36185, accent="P2")
