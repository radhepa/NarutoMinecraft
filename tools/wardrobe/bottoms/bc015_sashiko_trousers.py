"""Sashiko Trousers: heavy indigo work trousers reinforced with running stitch over the knees and
seat, narrow at the shin and worn with jika-tabi, for the carpenters and roofers."""
from kit_market import jika_tabi, sashiko
from paint import fabric, k, strip_fabric

META = {"name": "Sashiko Trousers", "gender": "unisex",
        "description": "Heavy indigo work trousers stitched over knee and seat, narrow shins, jika-tabi.",
        "tags": ["civilian", "trousers", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 36725, 2, 9, 11)
    fabric(body.bottom, "P", "plain", 36725, 1)
    sashiko(body.back, "P4", 3, rows=range(9, 12))
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "P", "plain", 36726 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "P", "plain", 36726, 2)
        for face in pants.sides:
            fabric(face, "P", "plain", 36728, 2, 0, 2, face.w, 3)
            sashiko(face, "P4", 3, rows=range(2, 5))
        leg.front.vline(1 if side == "right" else 2, 5, 9, k("P", 1))
    jika_tabi(g, "K", top=8, seed=36730)
