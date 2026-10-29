"""Messenger Jacket: a short zip jacket with accent bands round the upper sleeves, a notched collar,
and a message tube slung across the back on a strap over the left shoulder: the courier's kit."""
from kit_field import collar, shirt, strap
from paint import cap, k, solid, strip_fabric

META = {
    "name": "Messenger Jacket",
    "gender": "unisex",
    "description": "Short zip jacket with accent sleeve bands, a notched collar and a message tube on the back.",
    "tags": ["shinobi", "jacket", "chunin"],
}


def build(g):
    shirt(g, "P", 32320, texture="twill")
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "twill", 32322, 2, 0, 11)
    cap(jacket, "P", texture="twill", seed=32322)
    jacket.front.vline(4, 0, 10, "M3"), jacket.front.vline(3, 0, 10, "P1")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P3"), jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for side in ("right", "left"):
        sleeve = g.part(f"{side}_sleeve")
        strip_fabric(sleeve, "P", "twill", 32323, 2, 1, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 2, "A2"), sleeve.strip.hline(0, sleeve.strip.w - 1, 1, "A3")
        sleeve.strip.hline(0, sleeve.strip.w - 1, 3, "P1")
        g.part(f"{side}_arm").strip.hline(0, 15, 11, "P1")
    collar(g, "collar", "P", 32324, style="notch")
    strap(g, "tube_strap", (0, 5.0, -2.45), (0, 0, -40), length=14, role="L", seed=32325)
    tube = g.piece("message_tube", "TORSO", (-1, -5, -1), (2, 10, 2), pivot=(0, 5.0, 3.3), rotation=(0, 0, 40))
    solid(tube, "L", "leather", 32326, 2, edge=False)
    for face in tube.sides:
        face.hline(0, 1, 0, k("M", 3)), face.hline(0, 1, 9, k("M", 2)), face.hline(0, 1, 4, k("A", 2))
    tube.top.fill("M3"), tube.bottom.fill("M1")
