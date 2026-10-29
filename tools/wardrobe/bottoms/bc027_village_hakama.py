"""Village Hakama: everyday striped hakama for the house and the schoolroom, the wide legs pleated
and falling loose to the ankle, tied at the front with two bands and stiffened at the back with a
small board, over white tabi and zori."""
from kit_household import stripes, trim, trouser_legs, waist, zori
from paint import solid

META = {"name": "Village Hakama", "gender": "unisex",
        "description": "Wide striped hakama with pleats, front ties and a back board, white tabi and zori.",
        "tags": ["civilian", "hakama"]}


def build(g):
    waist(g, "D", "twill", 37516, band="D3")
    trouser_legs(g, "D", "twill", 37517, rows=(0, 9))
    zori(g, strap="D1")
    for side, sign, bone in (("right", -1, "RIGHT_LEG"), ("left", 1, "LEFT_LEG")):
        leg = g.piece(f"hakama_{side}", bone, (-2.5, 0, -2.6), (5, 10, 5), pivot=(0, 0.2, 0), rotation=(0, 0, -4 * sign),
                      inflate=.12)
        solid(leg, "D", "twill", 37519 + (sign > 0), 2)
        for face in leg.sides:
            stripes(face, "D1", every=2)
            face.hline(0, face.w - 1, 0, "D3")
        trim(leg, 9, "D0")
        leg.bottom.fill("D0")
    band = g.piece("waist_tie", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.3, 0), inflate=.2)
    solid(band, "D", "weave", 37522, 3, edge=False)
    board = g.piece("waist_board", "TORSO", (-2.5, 0, 0), (5, 2, 1), pivot=(0, 9.0, 2.35))
    solid(board, "D", "twill", 37523, 2)
    board.back.hline(0, 4, 0, "D3")
