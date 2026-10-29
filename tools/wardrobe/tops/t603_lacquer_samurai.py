"""Lacquer Samurai: the clan head's armor, a deep red lacquered cuirass laced in gold over a dark
green robe, the 食 crest ringed in gold on the chest, broad three-tier sode, a skirt of plates
(kusazuri) to mid-thigh and plated sleeves."""
from kit import arm_bone, arm_x, belt, flaps
from kit_akimichi import lames, shoku_disc, sode
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Lacquer Samurai",
    "gender": "unisex",
    "description": "Lacquered cuirass laced in gold over a green robe, food crest, broad sode, plate skirt.",
    "tags": ["shinobi", "armor", "akimichi"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 6731, 2)
    cap(body, "D", seed=6731)
    # The robe's crossed collar shows above the cuirass.
    body.front.set(3, 0, "S3"), body.front.set(4, 0, "S3"), body.front.set(2, 0, "D1"), body.front.set(5, 0, "D1")
    lames(g, "cuirass", [(.4, 4, .32), (4.3, 2, .44), (6.2, 2, .52), (8.1, 2, .46)], seed=6732, lacing="A3")
    shoku_disc(g, "chest_crest", (0, 2.4, -2.84), ground="P2", disc="S", ink="P0", rim="A2")
    belt(g, "obi", y=9.9, role="A", height=2, buckle=None, inflate=.5)
    sode(g, "sode", seed=6740, tiers=3, lacing="A3", stud="A3", flare=.05)
    # The kusazuri: plates front and back that follow the stride, laced in rows.
    for face in flaps(g, "kusazuri", 5, "P", "smooth", 6746, width=9, top=11.2, front_z=-3.1, back_z=2.1):
        for y in (1, 3):
            face.hline(0, face.w - 1, y, "P1")
            for x in range(1, face.w - 1, 3):
                face.set(x, y, "A3")
    for side, x in (("right", -5.1), ("left", 4.1)):
        panel = g.piece(f"kusazuri_{side}", "TORSO", (0, 0, -2), (1, 4, 4), pivot=(x, 11.2, 0))
        solid(panel, "P", "smooth", 6748, 2)
        for face in panel.sides:
            face.hline(0, face.w - 1, 1, "A3")
    # Plated sleeves (kote) over the robe's sleeves.
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 6750 + (side == "left"), 2)
        fabric(arm.top, "D", "weave", 6750, 3)
        fabric(arm.bottom, "K", "smooth", 6750, 1)
        arm.strip.hline(0, arm.strip.w - 1, 10, "K2"), arm.strip.hline(0, arm.strip.w - 1, 11, "K1")
        kote = g.piece(f"{side}_kote", arm_bone(side), (arm_x(side) - .3, 5.0, -2.3), (4, 5, 4), inflate=.1)
        solid(kote, "K", "smooth", 6752 + (side == "left"), 2, edge=False)
        for face in kote.sides:
            for y in (0, 2, 4):
                face.hline(0, face.w - 1, y, "P2")
            face.hline(0, face.w - 1, 0, "A3")
        fabric(kote.bottom, "K", "smooth", 6754, 1)
