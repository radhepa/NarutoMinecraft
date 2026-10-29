"""Fish Market Boots: work trousers tucked into tall black rubber boots that come up to the knee,
for the hosed-down floors of the fish market."""
from kit import leg_ring
from paint import fabric, k, strip_fabric

META = {"name": "Fish Market Boots", "gender": "unisex",
        "description": "Work trousers tucked into tall black rubber boots to the knee.",
        "tags": ["civilian", "trousers", "work", "boots"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 36665, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 36665, 1)
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "D", "twill", 36666 + (side == "left"), 2, 0, 4)
        fabric(leg.top, "D", "twill", 36666, 2)
        strip_fabric(leg, "K", "smooth", 36668, 2, 5, 11)
        strip_fabric(pants, "K", "smooth", 36669 + (side == "left"), 3, 5, 11)
        pants.strip.hline(0, pants.strip.w - 1, 11, "K1")
        pants.front.vline(1, 6, 10, k("K", 4))
        leg.bottom.fill("K1"), pants.bottom.fill("K0")
    for ring in leg_ring(g, "boot_top", 4.4, "K", 3, (5, 1, 5), "smooth"):
        for face in ring.sides:
            face.hline(0, face.w - 1, 0, "K4")
