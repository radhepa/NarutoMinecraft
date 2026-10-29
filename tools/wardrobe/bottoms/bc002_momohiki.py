"""Momohiki: close-fitting cotton work leggings from waist to ankle, the craftsman's and the
porter's, worn with split-toe jika-tabi boots fastened up the back."""
from kit_market import jika_tabi
from paint import fabric, k, strip_fabric

META = {"name": "Momohiki", "gender": "unisex",
        "description": "Close-fitting cotton work leggings with split-toe jika-tabi boots.",
        "tags": ["civilian", "trousers", "leggings", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "twill", 36530, 3, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "K4")
    fabric(body.bottom, "K", "twill", 36530, 2)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "K", "twill", 36531 + (side == "left"), 3, 0, 9)
        fabric(leg.top, "K", "twill", 36531, 3)
        leg.front.vline(1 if side == "right" else 2, 0, 6, k("K", 4))
    jika_tabi(g, "D", top=7, seed=36533)
