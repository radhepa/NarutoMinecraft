"""Genin Jacket: the young strategist's short-sleeved jacket worn open over a mesh shirt, trimmed in
the accent color round the front and cuffs, with the clan crest on the back."""
from kit_nara import back_crest, mesh_shirt
from paint import cap, fabric, strip_fabric

META = {
    "name": "Genin Jacket",
    "gender": "unisex",
    "description": "Open short-sleeved jacket with trim over a mesh shirt, clan crest on the back.",
    "tags": ["shinobi", "genin", "nara"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    # The mesh shirt over bare skin, a plain undershirt hem at the waist.
    mesh_shirt(g, (0, 8))
    strip_fabric(body, "K", "weave", 5521, 2, 9, 11)
    cap(body, "K", seed=5521)
    strip_fabric(jacket, "P", "weave", 5522, 2)
    cap(jacket, "P", seed=5522)
    f = jacket.front
    for y in range(12):
        for x in range(2, 6):
            f.clear(x, y)
        f.set(1, y, "A2"), f.set(6, y, "A2")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "A2")
    for x in (1, 6):
        f.set(x, 11, "A2")
    back_crest(g, "P", "A2", 5523, y=1.6)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 5524, 2, 0, 4)
        fabric(arm.top, "P", "weave", 5524, 3)
        strip_fabric(sleeve, "P", "weave", 5525 + (side == "left"), 2, 0, 5)
        fabric(sleeve.top, "P", "weave", 5525, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 5, "A2")
