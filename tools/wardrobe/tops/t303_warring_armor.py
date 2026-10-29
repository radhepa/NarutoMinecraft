"""Warring States Armor: the clan's battle armor from the age of war, a laced lamellar cuirass over a
dark under-robe, broad plated shoulder guards, a stiff gorget and the crest on the back plate."""
from kit import arm_bone, arm_x
from kit_uchiha import back_crest, lamellar
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Warring States Armor",
    "gender": "unisex",
    "description": "Laced red lamellar cuirass, plated shoulder guards, gorget, crest on the back plate.",
    "tags": ["shinobi", "armor", "uchiha"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 3830, 2)
    cap(body, "D", seed=3830)
    # The cuirass on the jacket layer, laced plates to the waist with a dark edge.
    lamellar(jacket.strip, "P", "K2", 3831, 0, 0, None, 10)
    fabric(jacket.top, "P", "leather", 3831, 3)
    jacket.strip.hline(0, jacket.strip.w - 1, 0, "P3")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "K1")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "K2")
    jacket.front.vline(0, 0, 9, "P1"), jacket.front.vline(7, 0, 9, "P1")
    back_crest(g, "K", pivot=(0, 1.4, 2.35), texture="leather", seed=3832)
    # Gorget: a stiff plated collar round the throat.
    gorget = g.piece("gorget", "TORSO", (-4.5, -1.6, -2.7), (9, 2, 5), inflate=.1)
    solid(gorget, "P", "leather", 3833, 2)
    for face in gorget.sides:
        face.hline(0, face.w - 1, 0, "P3"), face.hline(0, face.w - 1, 1, "K2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 3834 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "D", "weave", 3834, 3)
        # Bracers of black leather over the forearm.
        strip_fabric(arm, "K", "leather", 3836, 2, 6, 10)
        arm.strip.hline(0, arm.strip.w - 1, 6, "K3")
        # Sode: three plated tiers hanging over the shoulder, splaying out.
        sign = -1 if side == "right" else 1
        for i in range(3):
            plate = g.piece(f"{side}_sode_{i}", arm_bone(side), (arm_x(side) - .6 - .2 * i, -2.4 + 1.6 * i, -2.6 - .2 * i),
                            (5, 2, 5), rotation=(0, 0, 4 * sign * (i + 1)), inflate=.05 * i)
            solid(plate, "P", "leather", 3837 + i, 2, edge=False)
            for face in plate.sides:
                face.hline(0, face.w - 1, 0, "P3")
                face.hline(0, face.w - 1, 1, "P1")
                face.set(2, 1, "K2")
            plate.bottom.fill("K1")
