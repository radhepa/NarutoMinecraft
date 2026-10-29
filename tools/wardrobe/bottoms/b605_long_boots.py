"""Long Boots: snug dark shorts to mid-thigh and long black shinobi boots laced up the front to just
below the knee, with a turned-down cuff: Chocho's boots, worn by Akimichi who prefer to move fast."""
from kit import footwear
from paint import fabric, solid, strip_fabric

META = {"name": "Long Boots", "gender": "unisex",
        "description": "Snug dark shorts to mid-thigh and long black boots laced to below the knee.",
        "tags": ["shinobi", "akimichi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 6975, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 6975, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 6976 + (side == "left"), 2, 0, 2)
        fabric(leg.top, "D", "twill", 6976, 2)
        leg.strip.hline(0, leg.strip.w - 1, 2, "D3")
    footwear(g, "boot", top=5, role="K", base=2, toe="K3")
    for side in ("right", "left"):
        pants = g.part(f"{side}_pants")
        for y in range(6, 10, 2):
            pants.front.set(1, y, "K3"), pants.front.set(2, y + 1, "K3")
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        cuff = g.piece(f"{side}_boot_cuff", bone, (-2.5, 4.4, -2.5), (5, 1, 5), inflate=.12)
        solid(cuff, "K", "leather", 6978, 3, edge=False)
