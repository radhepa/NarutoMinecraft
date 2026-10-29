"""Battle Greaves: the lower half of the Third Hokage's battle dress. Close black leggings, armored
plates down the thighs, steel shin greaves with a knee cop and dark split-toe boots."""
from kit import footwear
from paint import fabric, k, solid, strip_fabric

META = {"name": "Battle Greaves", "gender": "unisex",
        "description": "Black leggings, plated thighs, steel shin greaves with knee cops, dark boots.",
        "tags": ["shinobi", "armor"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 9630, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "K3")
    fabric(body.bottom, "K", "plain", 9630, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "plain", 9631 + (side == "left"), 2, 0, 8)
        fabric(leg.top, "K", "plain", 9631, 2)
    footwear(g, "boot", top=9, role="K", base=2, sole="K0")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        plate = g.piece(f"{side}_thigh_plate", bone, (-2.3, 0.4, -2.6), (5, 3, 1), inflate=.05)
        solid(plate, "L", "leather", 9633, 2)
        plate.front.hline(0, 4, 1, "L1"), plate.front.hline(0, 4, 0, "L3")
        cop = g.piece(f"{side}_knee_cop", bone, (-1.5, 3.8, -2.9), (3, 2, 1))
        solid(cop, "M", "smooth", 9634, 3)
        greave = g.piece(f"{side}_greave", bone, (-2.1, 5.8, -2.55), (4, 3, 1), inflate=.05)
        solid(greave, "M", "smooth", 9635, 1)
        greave.front.hline(0, 3, 0, "M3"), greave.front.vline(1, 1, 2, "M2"), greave.front.vline(2, 1, 2, "M0")
        strap = g.piece(f"{side}_greave_strap", bone, (-2.4, 7.0, -2.4), (5, 1, 5))
        solid(strap, "L", "leather", 9637, 2, edge=False)
    for i, x in enumerate((-2.6, 2.6)):
        tasset = g.piece(f"waist_tasset_{i}", "TORSO", (-1.5, 0, -.5), (3, 3, 1), pivot=(x, 10.6, -2.6))
        solid(tasset, "M", "smooth", 9636 + i, 2)
        tasset.front.hline(0, 2, 1, k("M", 1))
