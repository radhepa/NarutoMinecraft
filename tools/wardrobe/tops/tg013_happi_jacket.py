"""Happi Jacket: a short festival coat worn open over a dark tank, a broad band down both front edges,
wide short sleeves, a round crest on the back and a twisted rope belt."""
from kit_academy import back_crest
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Happi Jacket",
    "gender": "unisex",
    "description": "Short open festival coat with banded front edges and wide sleeves over a dark tank, a rope belt.",
    "tags": ["shinobi", "genin", "wrap"],
}

RING = ["..####..",
        ".#....#.",
        "#..##..#",
        "#.#..#.#",
        "#.#..#.#",
        "#..##..#",
        ".#....#.",
        "..####.."]


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "rib", 31180, 2)
    cap(body, "K", texture="rib", seed=31180)
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "weave", 31181, 2)
    fabric(jacket.top, "P", "weave", 31181, 3)
    jacket.top.rect(2, 0, 4, 4, None)
    f = jacket.front
    for y in range(12):
        for x in (3, 4):
            f.clear(x, y)
        f.set(2, y, "S3"), f.set(5, y, "S3")
        f.set(1, y, k("S", 2) if y < 7 else "P1")
        f.set(6, y, k("S", 2) if y < 7 else "P1")
    jacket.back.hline(1, 6, 0, "S3")
    for face in jacket.sides:
        face.hline(0, face.w - 1, 11, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(2, 1, 10, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 31182 + (side == "left"), 2, 0, 3)
        fabric(arm.top, "P", "weave", 31182, 3)
        x = -3.5 if side == "right" else -1.5
        sleeve = g.piece(f"{side}_happi_sleeve", "RIGHT_ARM" if side == "right" else "LEFT_ARM", (x, -2.4, -2.5), (5, 5, 5))
        solid(sleeve, "P", "weave", 31184 + (side == "left"), 2)
        for face in sleeve.sides:
            face.hline(0, face.w - 1, 4, "S3")
        sleeve.bottom.fill("P0")
    back_crest(g, "P", "S3", 31186, y=2.6, z=2.3, rows=RING)
    rope = g.piece("waist_rope", "TORSO", (-4.6, 9.0, -2.6), (9, 1, 5), inflate=.15)
    solid(rope, "A", "weave", 31187, 3, edge=False)
    for face in rope.sides:
        for x in range(0, face.w, 2):
            face.set(x, 0, "A1")
    knot = g.piece("rope_knot", "TORSO", (0, 0, 0), (2, 1, 1), pivot=(-1.0, 9.0, -3.0))
    solid(knot, "A", "weave", 31188, 3, edge=False)
