"""Shrine Haori: the guardian's long plum haori open over a pale under-kimono, tied at the waist with
the twisted shimenawa rope of the mountain shrine and its paper streamers, the hem edged in web lines."""
from kit import body, flaps, sleeves
from kit_tsuchigumo import shimenawa, spider_crest, web_hem
from paint import k

META = {
    "name": "Shrine Haori",
    "gender": "unisex",
    "description": "Long plum haori over a pale under-kimono, belted with a shrine rope and paper streamers.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body(g, "S", "weave", 23521)
    coat = body(g, "P", "velvet", 23522, layer="jacket")
    f = coat.front
    for y in range(12):   # open front showing the pale under-kimono in a narrowing V
        for x in range(2, 6):
            if abs(x - 3.5) < 2.2 - y * .12:
                f.clear(x, y)
    f.vline(1, 0, 11, "A2"), f.vline(6, 0, 11, "A2")
    for arm in sleeves(g, "P", "velvet", 23523, rows=(0, 9), layer="sleeve"):
        for face in arm.sides:
            web_hem(face, 9, "A2", "A1")
    faces = flaps(g, "haori", 6, "P", "velvet", 23525, hem="A2")
    for face in faces:
        web_hem(face, 5, "A2", "A1")
        face.vline(4, 1, 4, k("P", 1))
    shimenawa(g, "rope", y=8.4)
    spider_crest(g, "back_crest", "P", "A3", pivot=(0, 1.4, 2.15))
