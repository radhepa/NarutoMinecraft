"""Shrine Hakama: the vermilion hakama of the shrine attendants, deep box pleats down each wide leg,
the white waist ties wound twice and knotted in front, over white tabi and pale zori. It keeps the
red of every palette, so the shrine white-and-red reads whatever the outfit."""
from kit_household import trim, trouser_legs, waist, zori
from paint import solid

META = {"name": "Shrine Hakama", "gender": "unisex",
        "description": "Vermilion pleated hakama with white waist ties knotted in front, white tabi and zori.",
        "tags": ["civilian", "hakama"]}


def build(g):
    waist(g, "A", "twill", 37532, band="A3")
    trouser_legs(g, "A", "twill", 37533, rows=(0, 9))
    zori(g, strap="S2", sole="S2")
    for side, sign, bone in (("right", -1, "RIGHT_LEG"), ("left", 1, "LEFT_LEG")):
        leg = g.piece(f"hakama_{side}", bone, (-2.5, 0, -2.6), (5, 10, 5), pivot=(0, 0.2, 0), rotation=(0, 0, -5 * sign),
                      inflate=.12)
        solid(leg, "A", "twill", 37535 + (sign > 0), 2)
        for face in leg.sides:
            for x in range(1, face.w, 2):
                face.vline(x, 1, face.h - 2, "A1")
            face.hline(0, face.w - 1, 0, "A3")
        trim(leg, 9, "A0")
        leg.bottom.fill("A0")
    for i, y in enumerate((9.0, 9.9)):
        tie = g.piece(f"waist_tie_{i}", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, y, 0), inflate=.2 + .02 * i)
        solid(tie, "S", "weave", 37538 + i, 3, edge=False)
    bow = g.piece("waist_bow", "TORSO", (-1.5, 0, 0), (3, 2, 1), pivot=(0, 9.2, -2.9))
    solid(bow, "S", "weave", 37540, 3, edge=False)
    for i, x in enumerate((-.9, .2)):
        end = g.piece(f"waist_end_{i}", "TORSO", (0, 0, 0), (1, 3, 1), pivot=(x, 10.6, -2.95), motion="sway")
        solid(end, "S", "weave", 37541 + i, 3)
