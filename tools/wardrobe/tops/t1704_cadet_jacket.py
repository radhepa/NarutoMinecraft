"""Cadet Jacket: an academy child's short slate zip jacket, the collar and zip piped in oxblood, the
sleeves pushed up to the elbow over a black undershirt."""
from kit import collar
from paint import cap, fabric, strip_fabric

META = {
    "name": "Cadet Jacket",
    "gender": "unisex",
    "description": "Short slate zip jacket piped in oxblood, sleeves pushed to the elbow over a black undershirt.",
    "tags": ["shinobi", "genin", "jacket"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "weave", 17251, 2)
    cap(body, "K", seed=17251)
    strip_fabric(jacket, "S", "weave", 17252, 2, 0, 10)
    cap(jacket, "S", seed=17252)
    jacket.front.vline(3, 0, 10, "A2"), jacket.front.vline(4, 0, 10, "S1")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "S1")
    for y in (3, 4):
        jacket.front.set(1, y + 3, "S0"), jacket.front.set(6, y + 3, "S0")
    neck = collar(g, "collar", "A", "weave", height=1, y=-.8, inflate=.1)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "K", "weave", 17253, 2, 0, 7)
        fabric(arm.top, "K", "weave", 17253, 3)
        strip_fabric(sleeve, "S", "weave", 17254 + (side == "left"), 2, 0, 5)
        fabric(sleeve.top, "S", "weave", 17254, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 5, "S3"), sleeve.strip.hline(0, sleeve.strip.w - 1, 6, "S1")
