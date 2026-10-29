"""Ink Crop Jacket: a short purple jacket with a stand collar and half sleeves, cropped above a
chain-mesh shirt, bandaged forearms and an ink scroll slung across the back: the painter's kit."""
from kit import collar
from kit_shinobi import mesh
from kit_yamanaka import wrapped
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Ink Crop Jacket",
    "gender": "unisex",
    "description": "Cropped purple jacket with half sleeves over a mesh shirt, bandaged forearms, ink scroll.",
    "tags": ["shinobi", "yamanaka", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    mesh(body.strip, 0, 0, body.strip.w - 1, 11, "K2")
    mesh(body.top, 0, 0, body.top.w - 1, body.top.h - 1, "K2")
    strip_fabric(jacket, "P", "weave", 7350, 2, 0, 6)
    cap(jacket, "P", texture="weave", seed=7350)
    jacket.strip.hline(0, jacket.strip.w - 1, 6, "P1")
    jacket.front.vline(4, 0, 6, "S3"), jacket.front.vline(3, 1, 6, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 6, "P1")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "weave", 7351, 2, 0, 4)
        fabric(arm.top, "P", "weave", 7351, 3)
        strip_fabric(sleeve, "P", "weave", 7352 + (side == "left"), 2, 0, 4)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 4, "S3")
        wrapped(arm.strip, 0, 6, arm.strip.w - 1, 10)
    neck = collar(g, "collar", "P", "weave", height=2, y=-1.4)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "S3")
    # The ink scroll across the back, capped in the accent, on a leather strap.
    scroll = g.piece("scroll", "TORSO", (-1, -5, -1), (2, 10, 2), pivot=(0, 5.0, 2.9), rotation=(0, 0, 60))
    solid(scroll, "S", "plain", 7354, 3)
    for face in scroll.sides:
        face.hline(0, 1, 0, "A2"), face.hline(0, 1, 9, "A2"), face.hline(0, 1, 4, "K2")
    strap = g.piece("strap", "TORSO", (-.5, -7, -.5), (1, 14, 1), pivot=(0, 5.0, 2.4), rotation=(0, 0, -50))
    solid(strap, "L", "leather", 7355, 2)
