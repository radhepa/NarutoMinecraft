"""Storm Trousers: quilted padded trousers under a short oiled storm apron hanging front and back
from the belt, tall leather boots: the bottom half of a heavy-weather kit."""
from kit import flaps, footwear, legs, waistband
from paint import solid

META = {"name": "Storm Trousers", "gender": "unisex",
        "description": "Quilted padded trousers under a short oiled storm apron front and back, tall leather boots.",
        "tags": ["shinobi"]}


def build(g):
    waistband(g, "P", "quilt", 35400, 2)
    legs(g, "P", "quilt", 35401, 2, rows=(0, 6), crease=False)
    footwear(g, "boot", top=6, role="L", base=2)
    for face in flaps(g, "waist_apron", 5, "D", "smooth", 35402, width=9, top=10.2):
        face.vline(2, 1, 4, "D3"), face.vline(6, 1, 4, "D3")
        face.hline(0, face.w - 1, 4, "D0")
    belt = g.piece("waist_belt", "TORSO", (-4.6, 9.4, -2.6), (9, 1, 5), inflate=.1)
    solid(belt, "L", "leather", 35404, 2, edge=False)
    belt.front.set(4, 0, "M3")
