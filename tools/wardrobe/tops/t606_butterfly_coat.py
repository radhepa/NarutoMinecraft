"""Butterfly Coat: a fitted sleeveless coat with gold trim and two long back tails that flare out
like wings, a broad white sash tied in a bow at the back, and long fingerless gloves."""
from kit import belt
from paint import fabric, solid, strip_fabric

META = {
    "name": "Butterfly Coat",
    "gender": "unisex",
    "description": "Sleeveless coat with gold trim and wing-like back tails, a white bow sash, long gloves.",
    "tags": ["shinobi", "akimichi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 6806, 2)
    fabric(body.top, "P", "weave", 6806, 3)
    strip_fabric(jacket, "P", "velvet", 6807, 2, 0, 9)
    fabric(jacket.top, "P", "velvet", 6807, 3)
    f = jacket.front
    # Gold-trimmed fronts meeting edge to edge, a dark inner panel showing in a V at the throat.
    for y in range(4):
        for x in range(2 + y // 2, 6 - y // 2):
            f.set(x, y, "K2")
    f.vline(3, 3, 9, "A3"), f.vline(4, 3, 9, "A2")
    for y in range(3):
        f.set(1 + y // 2, y, "A3"), f.set(6 - y // 2, y, "A2")
    jacket.strip.hline(0, jacket.strip.w - 1, 9, "A2")
    for face in (jacket.right, jacket.left):
        face.vline(face.w // 2, 0, 8, "P1")
    sash = belt(g, "sash", y=9.0, role="S", height=2, buckle=None, inflate=.32)
    sash.front.hline(0, sash.front.w - 1, 1, "S1")
    for i, (x, rz) in enumerate(((-1.6, 30), (1.6, -30))):
        loop = g.piece(f"bow_loop_{i}", "TORSO", (-1.5, -1, 0), (3, 2, 1), pivot=(x, 9.6, 3.0), rotation=(0, 0, rz))
        solid(loop, "S", "weave", 6808 + i, 3, edge=False)
    knot = g.piece("bow_knot", "TORSO", (-.5, -.5, 0), (1, 2, 1), pivot=(0, 9.5, 3.1))
    solid(knot, "S", "weave", 6810, 2, edge=False)
    # The wing tails, splayed out and trimmed in gold.
    for i, (x, ry, rz) in enumerate(((-2.2, -14, 12), (2.2, 14, -12))):
        tail = g.piece(f"wing_{i}", "TORSO", (-2, 0, 0), (4, 8, 1), pivot=(x, 10.8, 2.3), rotation=(10, ry, rz),
                       motion="flap_back")
        solid(tail, "P", "velvet", 6811 + i, 2)
        for face in tail.sides:
            face.hline(0, face.w - 1, face.h - 1, "A2")
        tail.back.vline(0 if i else 3, 0, 7, "A3")
        tail.back.set(1 if i else 2, 7, "P0")
    # Bare shoulders, long fingerless gloves.
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "K", "smooth", 6815, 2, 4, 10)
        arm.strip.hline(0, arm.strip.w - 1, 4, "A2")
