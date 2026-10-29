"""Shoku Armor: grown-up Choji's armor (Part II), red lacquered plates over a deep red bodysuit, the
食 ("food") crest in a white disc on the chest, a rounded stack of belly lames, two-tier shoulder
sode, plated forearm guards and a leather belt with a snack pouch."""
from kit import arm_bone, arm_x, belt
from kit_akimichi import lames, shoku_disc, snack_pouch, sode
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Shoku Armor",
    "gender": "unisex",
    "description": "Red plates over a deep red bodysuit: food crest, rounded belly lames, shoulder sode, forearm guards.",
    "tags": ["shinobi", "armor", "akimichi"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 6681, 1)
    cap(body, "P", seed=6681, base=1)
    # The cuirass and the belly lames, each a little deeper than the last so the front rounds out.
    lames(g, "chest_plate", [(.2, 4, .3)], seed=6682, lacing=None)
    lames(g, "belly_lame", [(4.2, 2, .42), (6.2, 2, .5), (8.0, 2, .4)], seed=6684)
    shoku_disc(g, "chest_crest", (0, 2.3, -2.82), ground="P2")
    sode(g, "sode", seed=6690)
    belt(g, "belt", y=10.0, role="L", height=2, inflate=.42)
    snack_pouch(g, "pouch", (2.6, 11.4, -2.9), role="A", size=(2, 2, 1), seed=6694)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 6695 + (side == "left"), 1, 0, 11)
        fabric(arm.top, "P", "weave", 6695, 2)
        fabric(arm.bottom, "P", "weave", 6695, 0)
        guard = g.piece(f"{side}_guard", arm_bone(side), (arm_x(side) - .3, 5.4, -2.3), (4, 4, 4), inflate=.12)
        solid(guard, "P", "smooth", 6697 + (side == "left"), 2, edge=False)
        for face in guard.sides:
            face.hline(0, face.w - 1, 0, "P3"), face.hline(0, face.w - 1, 3, "P1")
            face.set(1, 2, "A2"), face.set(2, 2, "A2")
