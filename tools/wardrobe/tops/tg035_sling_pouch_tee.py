"""Sling-Pouch Tee: a short-sleeved field tee with an accent tab at the collar, a strap crossing the
chest to a pouch riding at the back of the right hip, forearms taped at the wrists."""
from kit_field import half_sleeves, pocket, shirt, strap, tape

META = {
    "name": "Sling-Pouch Tee",
    "gender": "unisex",
    "description": "Short-sleeved tee with a collar tab, a chest strap to a hip pouch, taped wrists.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = shirt(g, "D", 32280, sleeve=-1, texture="knit")
    body.front.hline(2, 5, 0, "D1"), body.front.set(3, 1, "A2"), body.front.set(4, 1, "A2")
    half_sleeves(g, "D", 32283, length=3, texture="knit")
    strap(g, "sling", (.2, 5.0, -2.55), (0, 0, 38), length=14, role="P", seed=32285)
    strap(g, "sling_back", (.2, 5.0, 2.55), (0, 0, -38), length=14, role="P", seed=32286)
    pocket(g, "sling_pouch", (-3.6, 8.6, 0), (4, 4, 3), "P", 32287, rotation=(0, 90, 0), scale=.7, snap="M3")
    for side in ("right", "left"):
        tape(g.part(f"{side}_arm"), (8, 9))
