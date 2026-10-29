"""Medic Field Vest: a zipped vest with a low collar and a single chest pocket, a ring of small kit
pouches round the belt and a pale armband with an accent stripe on the left arm: the team medic."""
from kit import belt
from kit_field import collar, pocket, shirt, vest
from paint import k, solid

META = {
    "name": "Medic Field Vest",
    "gender": "unisex",
    "description": "Zip vest with a low collar, a ring of belt pouches and a pale armband on the left arm.",
    "tags": ["shinobi", "vest", "chunin"],
}


def build(g):
    shirt(g, "D", 32360)
    vest(g, "P", 32364, hem=9, ribs=(3, 6))
    collar(g, "collar", "P", 32365, style="low")
    pocket(g, "chest_pocket", (2.4, 2.6, -2.3), (4, 4, 1), "P", 32366, snap="S3")
    belt(g, "belt", y=9.6, role="L", inflate=.1)
    for i, (x, z, ry) in enumerate(((-2.8, -2.75, 0), (-.9, -2.75, 0), (2.8, -2.75, 0), (-4.8, 0, 90), (4.8, 0, -90))):
        pocket(g, f"kit_pouch_{i}", (x, 9.3, z), (3, 4, 2), "L", 32367 + i, rotation=(0, ry, 0), snap="M3")
    band = g.piece("armband", "LEFT_ARM", (-1, 1.0, -2), (4, 2, 4), inflate=.3)
    solid(band, "S", "plain", 32374, 3, edge=False)
    for face in band.sides:
        face.hline(0, face.w - 1, 1, k("A", 2))
