"""Smith's Leather Apron: the forge's heavy leather bib apron from the collarbone to the knee over
a sleeveless work shirt, scorched with sparks, the bare arms bound at the wrist and a sweat towel
slung round the neck."""
from kit_market import bib, towel_at_neck, waist_apron
from paint import cap, fabric, rnd, strip_fabric

META = {
    "name": "Smith's Leather Apron",
    "gender": "unisex",
    "description": "Heavy scorched leather bib apron to the knee over a sleeveless shirt, wrist wraps, a towel at the neck.",
    "tags": ["civilian", "work", "apron"],
    "tucked": True,
}


def scorch(face, seed: int):
    for y in range(face.h):
        for x in range(face.w):
            if rnd(x, y, seed) < .07:
                face.set(x, y, "L0" if rnd(y, x, seed) < .5 else "K2")


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 36140, 2)
    cap(body, "P", texture="twill", seed=36140)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 36141, 2, 0, 1)
        fabric(arm.top, "P", "twill", 36141, 3)
        for y in (9, 10):
            for x in range(arm.strip.w):
                arm.strip.set(x, y, "S2" if (x + y) % 3 == 0 else "S3")
    chest = bib(g, "leather", "L", 36143, length=9, width=6, top=.4, base=2, texture="leather", strap="L1")
    scorch(chest, 36144)
    skirt = waist_apron(g, "leather_skirt", "L", 7, 36145, width=8, base=2, top=9.4, z=-3.0, texture="leather", band="L1")
    scorch(skirt, 36146)
    towel_at_neck(g, "S", 36148)
