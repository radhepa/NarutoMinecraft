"""Shop Haori: the head of the household's beige haori worn open over a cream kimono, its front edges
lined in the accent colour, wide sleeves hanging past the elbow, white circle mon on the chest and a
large circle on the back."""
from kit import arm_bone, arm_x
from kit_haruno import back_crest, chest_crest, kimono_trim
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Shop Haori",
    "gender": "unisex",
    "description": "Open beige haori over a cream kimono, accent-lined fronts, wide hanging sleeves, circle mon and back crest.",
    "tags": ["shinobi", "robe"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 19600, 2)
    cap(body, "S", texture="weave", seed=19600)
    kimono_trim(body.front, [(0, 3), (1, 3), (2, 3)], "S", base=2)
    body.strip.hline(0, body.strip.w - 1, 9, k("A", 2))
    strip_fabric(jacket, "P", "weave", 19601, 2)
    cap(jacket, "P", texture="weave", seed=19601)
    f = jacket.front
    for y in range(12):
        for x in (2, 3, 4, 5):
            f.clear(x, y)
        f.set(1, y, k("A", 2)), f.set(6, y, k("A", 2))
    jacket.strip.hline(0, jacket.strip.w - 1, 11, k("P", 1))
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "S", "weave", 19602, 2, 0, 10)
        strip_fabric(sleeve, "P", "weave", 19603 + (side == "left"), 2, 0, 5)
        fabric(sleeve.top, "P", "weave", 19603, 3)
        drop = g.piece(f"{side}_hanging_sleeve", arm_bone(side), (arm_x(side) - .6, 2.5, -2.6), (5, 6, 5), inflate=.1,
                       motion="sway")
        solid(drop, "P", "weave", 19605 + (side == "left"), 2)
        for face in drop.sides:
            face.hline(0, face.w - 1, 5, k("A", 2))
        drop.bottom.fill(k("P", 0))
    for i, x in enumerate((-3.0, 2.0)):
        chest_crest(g, f"mon_{i}", x, y=1.4, z=-2.4, role="P", seed=19607 + i)
    back_crest(g, "P", texture="weave", seed=19609, size=12, pivot=(0, 1.0, 2.35))
