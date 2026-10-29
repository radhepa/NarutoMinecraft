"""Corset Obi Top: a long-sleeved fitted top with wide sleeve cuffs, cinched by a tall corset-like
obi laced up the front, the lacing crossed in the accent."""
from kit import belt, sleeves
from paint import cap, strip_fabric

META = {
    "name": "Corset Obi Top",
    "gender": "female",
    "description": "Long-sleeved fitted top with flared cuffs, a tall laced corset obi.",
    "tags": ["shinobi", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "smooth", 33300, 2)
    cap(body, "S", texture="smooth", seed=33300)
    body.front.hline(2, 5, 0, "S1")
    sleeves(g, "S", "smooth", 33301, rows=(0, 9))
    for side in ("right", "left"):
        cuff = g.part(f"{side}_sleeve")
        strip_fabric(cuff, "P", "smooth", 33303, 2, 7, 9)
        cuff.strip.hline(0, 15, 7, "P3"), cuff.strip.hline(0, 15, 9, "P1")
    corset = belt(g, "corset", y=5.8, role="P", height=4, buckle=None, inflate=.14)
    for face in corset.sides:
        face.hline(0, face.w - 1, 3, "P1")
    for y in range(4):
        corset.front.set(3 + (y % 2), y, "A3"), corset.front.set(4 - (y % 2), y, "A1")
