"""Potter's Samue: the kiln yard's plain samue jacket, tied closed at the side, the sleeves rolled
and the cotton smeared grey-brown with clay at the cuffs and the belly, a deep chest pocket."""
from kit import roll
from kit_kurama import splatter, wrap_front
from kit_market import pocket
from paint import cap, fabric, k, strip_fabric

META = {
    "name": "Potter's Samue",
    "gender": "unisex",
    "description": "Plain samue jacket tied at the side, rolled sleeves, clay-smeared cuffs and belly, a chest pocket.",
    "tags": ["civilian", "work", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 36420, 2)
    cap(body, "P", texture="twill", seed=36420)
    wrap_front(body.front, k("P", 4), k("P", 1), rows=8, start=1)
    body.front.set(7, 6, "K2"), body.front.set(7, 7, "K2")
    splatter(body.front, 36421, keys=("L2", "L3", "S1"), density=.09, rows=range(7, 12))
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 36422, 2, 0, 4)
        fabric(arm.top, "P", "twill", 36422, 3)
        splatter(arm.strip, 36423 + (side == "left"), keys=("L2", "L3", "S1"), density=.12, rows=range(5, 12))
    roll(g, "P", 4.0, base=2, accent="L2")
    pocket(g, "chest_pocket", "P", (-2.2, 3.0, -2.6), size=(3, 3), seed=36425, base=2)
