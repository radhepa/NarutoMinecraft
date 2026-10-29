"""Jika-Tabi Trousers: slim trousers to the ankle over dark split-toe work boots fastened up the back
with metal clasps, quiet on rooftops and sure on wet stone."""
from kit_field import trousers
from paint import fabric, k, strip_fabric

META = {"name": "Jika-Tabi Trousers", "gender": "unisex",
        "description": "Slim ankle trousers over dark split-toe work boots with metal clasps.",
        "tags": ["shinobi"]}


def build(g):
    trousers(g, "D", 32600, length=8, crease=True)
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "K", "smooth", 32602 + (side == "left"), 2, 9, 11)
        leg.strip.hline(0, leg.strip.w - 1, 9, k("K", 3))
        leg.front.vline(1 if side == "right" else 2, 10, 11, "K0")
        leg.bottom.fill("K0")
        leg.back.set(1, 9, "M3"), leg.back.set(1, 10, "M3"), leg.back.set(2, 9, "M2"), leg.back.set(2, 10, "M2")
        for face in pants.sides:
            fabric(face, "K", "smooth", 32604, 2, 0, 10, face.w, 2)
            face.hline(0, face.w - 1, 11, "K0")
        pants.front.vline(1 if side == "right" else 2, 10, 11, "K0")
        pants.bottom.fill("K0")
        leg.strip.hline(0, leg.strip.w - 1, 8, k("D", 1))
