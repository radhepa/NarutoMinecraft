"""Ink Crop Jacket: Inojin's kit, a short black collarless jacket with half sleeves over a purple
shirt and chain mesh, accent straps crossing the chest, bandaged forearms and an ink scroll slung
across the back."""
from kit_shinobi import mesh
from kit_yamanaka import wrapped
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Ink Crop Jacket",
    "gender": "unisex",
    "description": "Black collarless crop jacket with accent straps over a purple shirt and mesh, bandaged forearms, ink scroll.",
    "tags": ["shinobi", "yamanaka", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "plain", 7349, 2)
    fabric(body.top, "P", "plain", 7349, 3)
    mesh(body.strip, 0, 7, body.strip.w - 1, 11, "K3")
    strip_fabric(jacket, "K", "weave", 7350, 3, 0, 6)
    cap(jacket, "K", texture="weave", seed=7350, base=3)
    jacket.strip.hline(0, jacket.strip.w - 1, 6, "K1")
    for x in (3, 4):
        jacket.front.clear(x, 0), jacket.front.clear(x, 1)
    for y in range(6):
        jacket.front.set(1 + y, y, "A2"), jacket.front.set(6 - y, y, "A2")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 6, "K1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "K", "weave", 7351, 3, 0, 4)
        fabric(arm.top, "K", "weave", 7351, 4)
        strip_fabric(sleeve, "K", "weave", 7352 + (side == "left"), 3, 0, 4)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "A2")
        wrapped(arm.strip, 0, 6, arm.strip.w - 1, 10)
    # The ink scroll across the back, capped in the accent, on a leather strap.
    scroll = g.piece("scroll", "TORSO", (-1, -5, -1), (2, 10, 2), pivot=(0, 5.0, 2.9), rotation=(0, 0, 60))
    solid(scroll, "S", "plain", 7354, 3)
    for face in scroll.sides:
        face.hline(0, 1, 0, "A2"), face.hline(0, 1, 9, "A2"), face.hline(0, 1, 4, "K2")
    strap = g.piece("strap", "TORSO", (-.5, -7, -.5), (1, 14, 1), pivot=(0, 5.0, 2.4), rotation=(0, 0, -50))
    solid(strap, "L", "leather", 7355, 2)
