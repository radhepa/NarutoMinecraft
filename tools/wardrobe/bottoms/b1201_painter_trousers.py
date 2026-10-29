"""Painter's Trousers: Yakumo's loose, baggy trousers in a deep violet, gathered at the ankle over the
sandal strap, roomy enough to kneel at an easel all afternoon."""
from kit_shinobi import sandals
from paint import fabric, k, solid, strip_fabric

META = {"name": "Painter's Trousers", "gender": "unisex",
        "description": "Baggy deep-violet trousers gathered at the ankle, open-toe sandals.", "tags": ["shinobi"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 12850, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    fabric(body.bottom, "D", "twill", 12850, 1)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 12851 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "twill", 12851, 2)
        # The baggy leg: a loose shell from the hip to the shin, with soft vertical folds.
        bag = g.piece(f"{side}_bag", bone, (-2.5, -.2, -2.5), (5, 8, 5), inflate=.1)
        solid(bag, "D", "twill", 12853 + (side == "left"), 2)
        for f in bag.sides:
            for x in range(1, f.w, 2):
                f.vline(x, 1, 6, k("D", 1))
            f.hline(0, f.w - 1, 7, k("D", 1))
        bag.top.fill(k("D", 2))
        cuff = g.piece(f"{side}_gather", bone, (-2.2, 7.8, -2.2), (4, 2, 4), inflate=.12)
        solid(cuff, "D", "twill", 12855, 2)
        for f in cuff.sides:
            f.hline(0, f.w - 1, 0, k("D", 3))
            f.hline(0, f.w - 1, 1, k("D", 1))
    sandals(g)
