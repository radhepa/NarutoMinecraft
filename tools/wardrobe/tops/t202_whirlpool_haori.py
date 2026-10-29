"""Whirlpool Haori: a short red haori worn open over a dark shirt, three-quarter sleeves edged in
orange waves, and a great whirlpool crest across the back."""
from kit_uzumaki import crest_patch, waves
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Whirlpool Haori",
    "gender": "unisex",
    "description": "Short open red haori over a dark shirt, wave-edged sleeves, a great whirlpool on the back.",
    "tags": ["shinobi", "haori"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 2220, 2)
    cap(body, "D", seed=2220)
    body.front.vline(4, 1, 8, "D1")
    strip_fabric(jacket, "P", "weave", 2221, 2)
    cap(jacket, "P", seed=2221)
    for x in range(2, 6):
        for y in range(12):
            jacket.front.clear(x, y)
    jacket.front.vline(1, 0, 11, "S3"), jacket.front.vline(6, 0, 11, "S3")
    for face in (jacket.right, jacket.back, jacket.left):
        waves(face, 10, "A", 2)
    jacket.front.set(0, 10, "A2"), jacket.front.set(7, 10, "A2"), jacket.front.set(0, 11, "A2"), jacket.front.set(7, 11, "A2")
    crest_patch(g, "back_crest", "TORSO", (0, 1.4, 2.3), ground="S3", ink="A2")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "weave", 2222, 2, 0, 6)
        fabric(arm.top, "P", "weave", 2222, 3)
        strip_fabric(sleeve, "P", "weave", 2223, 2, 0, 7)
        fabric(sleeve.top, "P", "weave", 2223, 3)
        waves(sleeve.strip, 6, "A", 2)
    for name, x in (("right", -3.6), ("left", 2.6)):
        lapel = g.piece(f"lapel_{name}", "TORSO", (0, 0, 0), (1, 11, 1), pivot=(x, .2, -2.75))
        solid(lapel, "S", "weave", 2224, 3)
    cord = g.piece("haori_cord", "TORSO", (-1.5, 0, 0), (3, 1, 1), pivot=(0, 5.0, -2.8))
    solid(cord, "A", "smooth", 2225, 3, edge=False)
