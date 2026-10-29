"""Short Haori: a hip-length open haori with wide half sleeves and dark lapel bands, its cords tied
across a high-necked fitted undershirt: a jonin's off-duty layer that still fights well."""
from kit import sleeves
from kit_kunoichi import kimono_sleeves
from paint import cap, fabric, strip_fabric

META = {
    "name": "Short Haori",
    "gender": "unisex",
    "description": "Hip-length open haori with half sleeves and dark lapels, cords over a high-neck shirt.",
    "tags": ["shinobi", "jonin", "coat"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "smooth", 33240, 2)
    cap(body, "K", texture="smooth", seed=33240)
    strip_fabric(jacket, "P", "weave", 33241, 2)
    fabric(jacket.top, "P", "weave", 33241, 3)
    for y in range(12):
        for x in (2, 3, 4, 5):
            jacket.front.clear(x, y)
        jacket.front.set(1, y, "K2"), jacket.front.set(6, y, "K2")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for x in range(2, 6):
        jacket.front.set(x, 5, "S3")
    sleeves(g, "K", "smooth", 33242, rows=(0, 10), cuff="K1")
    kimono_sleeves(g, "haori_sleeve", "P", 33244, length=7, trim="K2")
