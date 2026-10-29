"""Dungaree Bib: the top half of a pair of dungarees, a bib with a front pocket and two shoulder straps
buttoned over a short-sleeved tee. It is one garment with the Dungaree Shorts and always worn with them."""
from kit_academy import shirt
from paint import fabric, k, strip_fabric

META = {
    "name": "Dungaree Bib",
    "gender": "unisex",
    "description": "Dungaree bib with a front pocket and buttoned straps over a short-sleeved tee.",
    "tags": ["shinobi", "genin"],
    "locked_to": "bg020_dungaree_shorts",
}


def build(g):
    body, arms = shirt(g, "P", "plain", 31285, sleeve=3, trim="P1")
    body.front.hline(3, 4, 0, "P1")
    jacket = g.part("jacket")
    strip_fabric(jacket, "D", "twill", 31286, 2, 5, 11)
    f, b = jacket.front, jacket.back
    for face in (f, b):
        for y in range(5):
            face.set(1, y, "D2"), face.set(6, y, "D2")
    fabric(jacket.top, "D", "twill", 31286, 3, 1, 0, 1, 4), fabric(jacket.top, "D", "twill", 31286, 3, 6, 0, 1, 4)
    f.set(1, 4, "M3"), f.set(6, 4, "M3")
    f.hline(1, 6, 5, "D3")
    f.rect(2, 6, 4, 3, "D2"), f.hline(2, 5, 6, "D3"), f.vline(2, 7, 8, "D1"), f.vline(5, 7, 8, "D1")
    f.set(4, 6, "A2")
    for face in jacket.sides:
        face.hline(0, face.w - 1, 11, k("D", 1))
