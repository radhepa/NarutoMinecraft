"""War Tassets: the lower half of the Warring States armor, laced lamellar tassets hanging from the
waist over dark trousers, plated shin guards and sandals. Worn only under armor."""
from kit_shinobi import sandals
from kit_uchiha import lamellar
from paint import fabric, solid, strip_fabric

META = {"name": "War Tassets", "gender": "unisex",
        "description": "Laced lamellar tassets over dark trousers, plated shin guards, sandals.",
        "tags": ["shinobi", "armor"], "requires": ["armor"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 3960, 2, 9, 11)
    fabric(body.bottom, "D", "weave", 3960, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "weave", 3961 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "weave", 3961, 2)
    sandals(g)
    # Tassets: front, back and one at each hip.
    for name, origin, size, pivot, motion in (
            ("front", (-4.5, 0, 0), (9, 5, 1), (0, 10.6, -2.95), "flap_front"),
            ("back", (-4.5, 0, 0), (9, 6, 1), (0, 10.6, 1.95), "flap_back"),
            ("right", (0, 0, -2), (1, 5, 4), (-5.1, 10.6, 0), "none"),
            ("left", (0, 0, -2), (1, 5, 4), (4.1, 10.6, 0), "none")):
        t = g.piece(f"tasset_{name}", "TORSO", origin, size, pivot=pivot, motion=motion)
        solid(t, "P", "leather", 3963, 2, edge=False)
        for face in t.sides:
            lamellar(face, "P", "K2", 3964)
        t.bottom.fill("K1")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        guard = g.piece(f"{side}_shin_guard", bone, (-2.5, 5.0, -2.6), (5, 5, 2), inflate=.05)
        solid(guard, "P", "leather", 3965, 2)
        lamellar(guard.front, "P", "K2", 3966)
        guard.front.hline(0, 4, 0, "K2")
