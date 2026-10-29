"""Magaki Coat: the long dark coat of the Magaki faction, who wanted the forbidden jutsu turned on
the clan's enemies: high split collar, ochre edging, skirts to the knee and a web stitched in black
on the back."""
from kit import belt, body, collar, flaps, sleeves
from kit_tsuchigumo import web
from paint import k

META = {
    "name": "Magaki Coat",
    "gender": "unisex",
    "description": "Long dark coat with a high split collar, ochre edging, knee skirts and a black web on the back.",
    "tags": ["shinobi", "coat"],
    "covers_waist": True,
}


def build(g):
    body(g, "D", "twill", 23581)
    coat = body(g, "D", "twill", 23582, layer="jacket")
    f = coat.front
    f.vline(3, 0, 11, "A2"), f.vline(4, 0, 11, k("D", 0))
    web(coat.back, 3, 0, "K1", rings=(3, 6, 9))
    for arm in sleeves(g, "D", "twill", 23583, rows=(0, 11), layer="sleeve", cuff="A2", cuff_row=10):
        pass
    neck = collar(g, "collar", "D", "twill", height=3, y=-2.2)
    neck.front.vline(4, 0, 2, "K1")
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "A2")
    belt(g, "belt", y=8.8, role="K", height=1, buckle="A")
    for face in flaps(g, "skirt", 7, "D", "twill", 23585, hem="A2", slit=True):
        face.hline(0, face.w - 1, 5, k("D", 1))
