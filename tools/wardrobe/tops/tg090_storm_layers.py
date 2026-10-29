"""Storm Layers: a quilted hip-length coat over a knit undershirt, a thick wool scarf wound twice
round the neck with one end hanging down the chest, a wide leather belt and dark mittens: dressed
for snow on the high passes."""
from kit import arm_bone, arm_x, belt, sleeves
from paint import fabric, k, solid, strip_fabric

META = {
    "name": "Storm Layers",
    "gender": "unisex",
    "description": "Quilted hip-length coat, a thick wool scarf wound twice with a hanging end, wide belt, mittens.",
    "tags": ["shinobi", "coat", "jonin"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "knit", 35100, 2)
    fabric(body.top, "S", "knit", 35100, 3)
    strip_fabric(jacket, "P", "quilt", 35101, 2, 1, 11)
    f = jacket.front
    f.vline(4, 1, 11, "P0"), f.vline(5, 1, 11, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    sleeves(g, "P", "quilt", 35102, 2, rows=(0, 8))
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "K", "knit", 35103, 3, 9, 11)
        fabric(arm.bottom, "K", "knit", 35103, 2)
        cuff = g.piece(f"{side}_cuff", arm_bone(side), (arm_x(side) - .4, 6.4, -2.4), (5, 1, 5))
        solid(cuff, "P", "quilt", 35104 + (side == "left"), 1, edge=False)
    belt(g, "wide_belt", y=8.6, role="L", height=2, buckle="M")
    # The scarf: two thick turns round the neck and an end hanging down the left of the chest.
    for i, y in enumerate((-1.9, -.4)):
        turn = g.piece(f"scarf_turn_{i}", "TORSO", (-4.6, y, -2.8), (9, 2, 5), inflate=.12 + .1 * i)
        solid(turn, "A", "knit", 35106 + i, 2)
        for face in turn.sides:
            face.hline(0, face.w - 1, 0, k("A", 3))
    end = g.piece("scarf_end", "TORSO", (-1, 0, 0), (3, 7, 1), pivot=(1.6, 1.2, -3.4), rotation=(0, 0, -4), motion="flap_front")
    solid(end, "A", "knit", 35108, 2)
    end.front.hline(0, 2, 6, "S3"), end.front.hline(0, 2, 5, "S2")
