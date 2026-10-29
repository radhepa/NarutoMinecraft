"""Fishmonger's Apron: the fish market's long dark waterproof apron from the chest to below the
knee, over a striped work shirt with the sleeves rolled to the elbow."""
from kit import roll
from kit_market import bib, stripes, waist_apron
from paint import cap, fabric, k, strip_fabric

META = {
    "name": "Fishmonger's Apron",
    "gender": "unisex",
    "description": "Long dark waterproof apron from chest to below the knee over a striped shirt with rolled sleeves.",
    "tags": ["civilian", "work", "apron"],
    "tucked": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 36220, 3)
    cap(body, "S", seed=36220, base=3)
    for face in body.sides:
        stripes(face, k("P", 2), 2, vertical=False)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 36221, 3, 0, 4)
        stripes(arm.strip, k("P", 2), 2, vertical=False, rows=range(0, 5))
        fabric(arm.top, "S", "weave", 36221, 4)
    roll(g, "S", 4.0, base=3, accent=k("P", 2))
    front = bib(g, "rubber", "K", 36223, length=9, width=6, top=1.0, base=3, texture="smooth", strap="K2")
    front.vline(0, 1, 8, "K4")
    skirt = waist_apron(g, "rubber_skirt", "K", 10, 36225, width=8, base=3, top=9.6, z=-3.0, texture="smooth", band="K2")
    skirt.vline(1, 1, 9, "K4")
