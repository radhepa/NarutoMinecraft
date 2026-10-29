"""Painter's Smock: a loose cream smock worn for work at the easel, sleeves rolled to the elbow, a
canvas apron tied over it and splashed with paint, a brush and a rag tucked in the bib pocket."""
from kit import roll
from kit_kurama import splatter
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Painter's Smock",
    "gender": "unisex",
    "description": "Loose cream smock with rolled sleeves, a paint-splashed apron, a brush in the bib pocket.",
    "tags": ["shinobi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 12700, 2)
    cap(body, "S", seed=12700)
    body.front.set(3, 0, None), body.front.set(4, 0, None), body.front.set(3, 1, "S1")
    for face in body.sides:
        face.vline(1, 2, 11, "S1")
    # The apron: bib and skirt on the jacket layer, straps over the shoulders and round the sides.
    j = jacket.front
    for y in range(2, 12):
        for x in range(1, 7):
            j.set(x, y, k("L", 3 if y > 2 else 4))
    splatter(j, 12701, keys=("A2", "D3", "K2", "P2"), density=.12, rows=range(3, 12))
    for face in (jacket.right, jacket.left):
        face.hline(0, face.w - 1, 7, "L2")
    jacket.back.hline(0, 7, 7, "L2")
    j.vline(1, 0, 1, "L2"), j.vline(6, 0, 1, "L2")
    jacket.back.vline(1, 0, 6, "L2"), jacket.back.vline(6, 0, 6, "L2")
    # The bib pocket, a brush standing in it and a rag hanging out.
    pocket = g.piece("pocket", "TORSO", (0, 0, 0), (3, 2, 1), pivot=(-.6, 3.2, -2.75))
    solid(pocket, "L", "weave", 12702, 3)
    pocket.front.hline(0, 2, 0, "L4")
    brush = g.piece("brush", "TORSO", (-.5, -3, -.5), (1, 4, 1), pivot=(-.1, 3.4, -2.3), rotation=(0, 0, -10),
                    scale=(.5, 1, .5))
    solid(brush, "L", "smooth", 12703, 1)
    brush.top.fill("K1")
    for face in brush.sides:
        face.set(0, 0, "K2"), face.set(0, 1, "M3")
    rag = g.piece("rag", "TORSO", (0, 0, 0), (1, 3, 1), pivot=(1.4, 3.2, -2.9), motion="sway")
    solid(rag, "A", "weave", 12704, 3)
    # Apron skirt to mid-thigh.
    apron = g.piece("apron_skirt", "TORSO", (-3, 0, 0), (6, 5, 1), pivot=(0, 11.6, -2.8), motion="flap_front")
    solid(apron, "L", "weave", 12705, 3)
    splatter(apron.front, 12706, keys=("A2", "D3", "K2", "P2"), density=.14)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 12707, 2, 0, 3)
        fabric(arm.top, "S", "weave", 12707, 3)
        splatter(arm.strip, 12708 + (side == "left"), keys=("A2", "D3"), density=.04, rows=range(5, 10))
    roll(g, "S", 1.6, base=3)
