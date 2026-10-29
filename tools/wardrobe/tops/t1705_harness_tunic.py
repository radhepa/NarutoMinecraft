"""Harness Tunic: a high-necked dark slate tunic with long sleeves, crossed at the chest by a black
leather harness on steel rings, black gloves to the wrist."""
from kit import collar
from kit_morino import gloves
from paint import cap, fabric, line, solid, strip_fabric

META = {
    "name": "Harness Tunic",
    "gender": "unisex",
    "description": "High-necked dark slate tunic crossed by a black leather harness on steel rings, black gloves.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 17261, 2)
    cap(body, "D", seed=17261)
    body.strip.hline(0, body.strip.w - 1, 11, "D1")
    j = jacket
    for face in (j.front, j.back):
        line(face, 0, 0, 7, 9, "K2"), line(face, 7, 0, 0, 9, "K2")
    j.front.set(3, 4, "M3"), j.front.set(4, 4, "M3"), j.front.set(3, 5, "M2"), j.front.set(4, 5, "M2")
    j.strip.hline(0, j.strip.w - 1, 9, "K1"), j.strip.hline(0, j.strip.w - 1, 10, "K2")
    j.front.set(4, 9, "M3")
    for face in (j.top, j.bottom):
        face.fill("K1")
    collar(g, "collar", "D", "weave", height=2, y=-1.4, inflate=.08)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 17262 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "D", "weave", 17262, 3)
    gloves(g, top=9)
