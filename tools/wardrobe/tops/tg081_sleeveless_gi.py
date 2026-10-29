"""Sleeveless Gi: a heavy cotton gi top with the sleeves torn off at the shoulder, the lapels crossed
left over right and a dark belt knotted with two long tails, the forearms wound in bandages: the
taijutsu fighter who trains until the cloth gives out."""
from kit import belt, neckline
from kit_rugged import ragged
from kit_shinobi import bandage
from paint import fabric, line, solid, strip_fabric

META = {
    "name": "Sleeveless Gi",
    "gender": "unisex",
    "description": "Heavy gi top with torn-off sleeves, crossed lapels, a dark knotted belt and bandaged forearms.",
    "tags": ["shinobi", "genin", "wrap", "taijutsu"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 35010, 2, 0, 10)
    fabric(body.top, "P", "weave", 35010, 3)
    strip_fabric(jacket, "P", "weave", 35011, 2, 0, 9)
    fabric(jacket.top, "P", "weave", 35011, 3)
    for face in (body.front, jacket.front):
        neckline(face, "v", "P")
    # The wearer's left lapel crosses over the right down to the belt, a thick seam along its edge.
    f = jacket.front
    line(f, 2, 0, 5, 9, "P0"), line(f, 1, 0, 4, 9, "P3")
    line(f, 6, 1, 6, 9, "P1")
    # Torn armholes: frayed shoulders on the overlay.
    for face in (jacket.right, jacket.left):
        ragged(face, 0, 35012, .5)
        face.vline(face.w // 2, 2, 9, "P1")
    jacket.back.vline(3, 1, 9, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        bandage(arm.strip, 0, 6, arm.strip.w - 1, 10)
        arm.strip.hline(0, arm.strip.w - 1, 6, "S2")
    # The dark belt, knotted at the front with two long tails.
    obi = belt(g, "gi_belt", y=9.2, role="K", base=3, buckle=None)
    obi.front.hline(0, obi.front.w - 1, 1, "K2")
    knot = g.piece("belt_knot", "TORSO", (-1, 0, 0), (2, 2, 1), pivot=(0, 9.2, -2.9))
    solid(knot, "K", "weave", 35013, 3, edge=False)
    for i, (x, rz) in enumerate(((-.5, 10), (.6, -12))):
        tail = g.piece(f"belt_tail_{i}", "TORSO", (-.5, 0, -.5), (1, 4, 1), pivot=(x, 10.8, -3.0), rotation=(0, 0, rz),
                       motion="flap_front")
        solid(tail, "K", "weave", 35014 + i, 3)
