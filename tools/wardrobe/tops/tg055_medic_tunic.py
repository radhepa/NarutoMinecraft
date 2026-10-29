"""Medic Tunic: the medical corps' fitted tunic, buttoned across the chest from the collar to the
side seam, short sleeves, a pale band at the hem and a medical pouch on each hip."""
from kit import collar, pouch, sleeves
from kit_kunoichi import frog_buttons
from paint import cap, strip_fabric

META = {
    "name": "Medic Tunic",
    "gender": "unisex",
    "description": "Fitted side-buttoned medic tunic, short sleeves, a pale hem band, pouches on both hips.",
    "tags": ["shinobi", "chunin", "tunic"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 33280, 2)
    cap(body, "P", seed=33280)
    f = body.front
    f.vline(5, 0, 10, "P3"), f.vline(6, 0, 10, "P1")
    frog_buttons(f, [(4, 2), (4, 5), (4, 8)], key="S4", loop="S2")
    body.strip.hline(0, body.strip.w - 1, 10, "S3"), body.strip.hline(0, body.strip.w - 1, 11, "S2")
    sleeves(g, "P", "plain", 33281, rows=(0, 4), cuff="S3")
    neck = collar(g, "collar", "P", "plain", height=1, y=-.8)
    neck.front.set(5, 0, "P0")
    for i, x in enumerate((-3.2, 3.2)):
        pouch(g, f"hip_pouch_{i}", (x, 9.6, -2.3), size=(2, 2, 2), role="S", flap="A2")
