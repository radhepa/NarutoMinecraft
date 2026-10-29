"""Wrapped Slacks: slate slacks cut narrow, bound from the calf to the ankle in dark cloth and
finished in soft closed shoes, so no insect crawls in at the hem."""
from kit import footwear, legs, waistband
from paint import k

META = {"name": "Wrapped Slacks", "gender": "unisex",
        "description": "Narrow slate slacks bound in dark cloth from calf to ankle, soft closed shoes.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "D", "weave", 10831)
    legs(g, "D", "weave", 10832, rows=(0, 9))
    for side in ("right", "left"):
        pants = g.part(f"{side}_pants")
        for face in pants.sides:
            for y in range(5, 10):
                for x in range(face.w):
                    face.set(x, y, k("D", 0 if (x + y) % 4 == 0 else 1))
            face.hline(0, face.w - 1, 5, "D2")
    footwear(g, "shoe", top=10, role="L", base=2, sole="K0")
