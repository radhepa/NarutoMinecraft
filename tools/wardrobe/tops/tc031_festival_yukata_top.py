"""Festival Yukata Top: the summer-night yukata of the lantern festival, cotton printed with
morning glories, wide hanging sleeves, a white under-collar at the throat and a broad obi tied at
the back in a butterfly bow with two trailing tails. Tucked, so it meets any skirt or trousers."""
from kit_household import overlap, sash, sprigs, wide_sleeves
from paint import cap, strip_fabric

META = {
    "name": "Festival Yukata Top",
    "gender": "female",
    "description": "Morning-glory yukata with wide sleeves, a white under-collar and a broad obi in a butterfly bow.",
    "tags": ["civilian", "kimono", "wrap"],
    "tucked": True,
}


def glories(face, rows=None):
    sprigs(face, "A3", "S4", step=5, seed=3, rows=rows)


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 37100, 2)
    cap(body, "P", seed=37100)
    glories(body.strip)
    overlap(body.front, "P0", "P1", rows=7, under="S4")
    wide_sleeves(g, "sleeve", "P", "plain", 37101, top=2.0, length=8, pattern=glories, arm_rows=9)
    obi = sash(g, "obi", "D", y=6.6, height=3, knot="bow", seed=37106, stripe="A3")
    obi.front.set(4, 1, "S4")
