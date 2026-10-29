"""Medic Tunic: a medical-nin's rose tunic with a standing collar and long cream sleeves, a cream
panel buttoned down the chest, a sash with a supply pouch at the hip and the circle on each sleeve."""
from kit import belt, pouch, sleeves
from kit_haruno import arm_crest, back_crest, mandarin_collar
from paint import cap, k, strip_fabric

META = {
    "name": "Medic Tunic",
    "gender": "unisex",
    "description": "Rose tunic with a standing collar, cream chest panel and long sleeves, sash and hip pouch, circles on the sleeves.",
    "tags": ["shinobi", "chunin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 19560, 2)
    cap(body, "P", texture="plain", seed=19560)
    f = body.front
    for y in range(0, 8):
        f.hline(2, 5, y, k("S", 3))
    f.vline(2, 0, 7, k("S", 2))
    for y in (2, 4, 6):
        f.set(4, y, k("P", 1))
    body.strip.hline(0, body.strip.w - 1, 11, k("P", 1))
    for box in sleeves(g, "S", "plain", 19561, 3, rows=(0, 10), cuff=k("P", 2)):
        box.strip.hline(0, box.strip.w - 1, 9, k("P", 3))
    for side in ("right", "left"):
        arm_crest(g, side, "S", seed=19563, base=3)
    mandarin_collar(g, "P", 19564, trim=k("S", 3))
    belt(g, "sash", y=8.4, role="A", height=1, buckle=None, inflate=.15)
    pouch(g, "medic_pouch", (-3.4, 9.6, -1.0), size=(2, 2, 2), role="S", flap=k("A", 3))
    back_crest(g, "P", texture="plain", seed=19565, size=8, pivot=(0, 2.0, 2.05))
