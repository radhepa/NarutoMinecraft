"""Archivist Jacket: the records clerk's hip-length wrap jacket over a pale under-collar, with cloth
oversleeves tied over the forearms to keep the cuffs clean (they never do) and a document satchel
slung on a strap at the hip."""
from kit_kurama import wrap_front
from kit_specialist import ink_stains, strap
from paint import cap, solid, strip_fabric

META = {
    "name": "Archivist Jacket",
    "gender": "unisex",
    "description": "Hip-length wrap jacket, inky cloth oversleeves on the forearms, a document satchel on a strap.",
    "tags": ["shinobi", "jacket", "chunin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 34140, 2)
    cap(body, "P", texture="weave", seed=34140)
    wrap_front(body.front, "S3", "S2", rows=7, start=1)
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 34141 + (side == "left"), 2, 0, 11)
        strip_fabric(sleeve, "S", "plain", 34143 + (side == "left"), 3, 5, 11)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 5, "S4"), sleeve.strip.hline(0, sleeve.strip.w - 1, 6, "K2")
        sleeve.strip.hline(0, sleeve.strip.w - 1, 11, "S2")
        ink_stains(sleeve.strip, 34145 + (side == "left"), range(8, 12), .2 if side == "right" else .1)
    strap(g, "satchel_strap", (.4, 4.6), -40, 15, -2.7, seed=34147)
    bag = g.piece("satchel", "TORSO", (-2, 0, -1), (4, 3, 2), pivot=(3.6, 9.4, -.6))
    solid(bag, "L", "leather", 34148, 2)
    bag.front.hline(0, 3, 0, "L3"), bag.front.set(2, 1, "M3")
    roll = g.piece("satchel_scroll", "TORSO", (-.5, -1.5, -.5), (1, 2, 1), pivot=(3.2, 9.2, -.6))
    solid(roll, "S", "plain", 34149, 3, edge=False)
