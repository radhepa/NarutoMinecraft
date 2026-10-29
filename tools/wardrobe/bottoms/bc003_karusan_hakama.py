"""Karusan Work Hakama: the tradesman's hakama, full and pleated through the thigh and caught in
tight below the knee so it stays out of the mud, over wrapped shins and straw sandals."""
from kit_market import kyahan, loose_legs, straw_sandals
from paint import fabric, k, solid, strip_fabric

META = {"name": "Karusan Work Hakama", "gender": "unisex",
        "description": "Hakama full through the thigh and caught tight below the knee, wrapped shins, straw sandals.",
        "tags": ["civilian", "hakama", "work"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 36545, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, k("D", 3))
    fabric(body.bottom, "D", "twill", 36545, 1)
    for box in loose_legs(g, "hakama", "D", 36546, length=6, flare=2):
        for face in box.sides:
            for x in range(1, face.w, 2):
                face.vline(x, 1, 4, k("D", 1))
            face.hline(0, face.w - 1, 5, k("D", 0))
    for side in ("right", "left"):
        strip_fabric(g.part(f"{side}_leg"), "D", "twill", 36548, 2, 0, 5)
    kyahan(g, "D", rows=(6, 9), seed=36549, tie="S3")
    band = g.piece("waist_tie", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.2, 0), inflate=.2)
    solid(band, "D", "weave", 36551, 3, edge=False)
    straw_sandals(g)
