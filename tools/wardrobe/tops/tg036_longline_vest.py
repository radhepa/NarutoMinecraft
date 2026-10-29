"""Longline Vest: a jonin vest cut long, its padded skirt split at the sides and falling past the hips,
belted at the waist over a dark shirt, two chest pockets and a pouch on the belt."""
from kit import belt, flaps
from kit_field import collar, pocket, shirt, vest
from paint import k

META = {
    "name": "Longline Vest",
    "gender": "unisex",
    "description": "Long padded vest split at the sides past the hips, belted, over a dark shirt.",
    "tags": ["shinobi", "vest", "jonin"],
    "covers_waist": True,
}


def build(g):
    shirt(g, "D", 32300)
    vest(g, "P", 32304, ribs=(3, 6))
    collar(g, "collar", "P", 32305, style="stand")
    front, back = flaps(g, "skirt", 4, "P", "plain", 32306, width=8, top=10.4, front_z=-2.8, back_z=1.8)
    for face in (front, back):
        face.vline(3, 1, 3, k("P", 1)), face.hline(0, 7, 3, k("P", 1))
    belt(g, "belt", y=9.2, role="L", inflate=.18)
    for i, x in enumerate((-2.4, 2.4)):
        pocket(g, f"pocket_{i}", (x, 2.4, -2.3), (3, 5, 1), "P", 32308 + i)
    pocket(g, "belt_pouch", (2.6, 9.0, -2.85), (3, 3, 2), "L", 32310, snap="M3")
