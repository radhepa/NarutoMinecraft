"""Grocer's Shirt: the greengrocer's open-collar shirt with the sleeves held up by elastic garters,
under a canvas waist apron with a clasp purse for the day's coins at the front."""
from kit_market import waist_apron
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Grocer's Shirt",
    "gender": "unisex",
    "description": "Open-collar shirt with sleeve garters under a canvas waist apron with a clasp purse for coins.",
    "tags": ["civilian", "casual", "apron"],
    "tucked": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 36380, 3)
    cap(body, "S", seed=36380, base=3)
    f = body.front
    f.clear(3, 0), f.clear(4, 0), f.clear(3, 1)
    f.set(2, 0, "S4"), f.set(5, 0, "S4"), f.set(2, 1, "S4"), f.set(4, 1, "S1")
    f.vline(4, 2, 11, "S2")
    for y in (3, 6):
        f.set(4, y, "M3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 36381, 3, 0, 10)
        fabric(arm.top, "S", "weave", 36381, 4)
        arm.strip.hline(0, arm.strip.w - 1, 2, k("A", 2))
        arm.strip.hline(0, arm.strip.w - 1, 10, "S2")
    front = waist_apron(g, "canvas", "D", 7, 36383, width=8, base=2, top=9.6, z=-3.0, texture="twill", band="D1")
    front.hline(0, 7, 3, k("D", 1))
    purse = g.piece("coin_purse", "TORSO", (-1, 0, 0), (2, 2, 1), pivot=(1.4, 10.6, -3.6))
    solid(purse, "L", "leather", 36385, 2)
    purse.front.hline(0, 1, 0, "M3")
    purse.top.fill("M3")
