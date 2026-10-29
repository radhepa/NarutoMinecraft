"""Padded Hanten: the winter jacket of the night stalls and the cold mornings, thick quilted cotton
with a dark collar band, wide sleeves to the wrist and two ties at the front."""
from kit import flaps
from kit_market import sleeves
from paint import cap, k, strip_fabric

META = {
    "name": "Padded Hanten",
    "gender": "unisex",
    "description": "Thick quilted winter jacket with a dark collar band, wide sleeves to the wrist and front ties.",
    "tags": ["civilian", "jacket", "coat"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "quilt", 36460, 2)
    cap(body, "P", seed=36460)
    strip_fabric(jacket, "P", "quilt", 36461, 2)
    jacket.top.fill(k("P", 3))
    for y in range(12):
        jacket.front.clear(3, y), jacket.front.clear(4, y)
        jacket.front.set(2, y, "K3"), jacket.front.set(5, y, "K3")
    body.front.vline(3, 0, 11, "K2"), body.front.vline(4, 0, 11, k("P", 1))
    for y in (4, 7):
        jacket.front.set(3, y, k("A", 2)), jacket.front.set(4, y, k("A", 2))
    sleeves(g, "P", "quilt", 36462, rows=(0, 10), cuff="K3")
    for face in flaps(g, "hanten_hem", 2, "P", "quilt", 36464, width=9, top=11.0, front_z=-3.0, back_z=2.0, slit=True):
        face.hline(0, 8, 1, k("P", 1))
