"""Hakama: wide pleated hakama in the dark cloth, tied at the front with crossed bands, the legs
falling loose to the ankle over white tabi and straw sandals. Worn under wrapped tops."""
from kit_hyuga import hakama_legs, tabi
from paint import fabric, solid, strip_fabric

META = {"name": "Hakama", "gender": "unisex",
        "description": "Wide pleated dark hakama with a front tie, white tabi and straw sandals.",
        "tags": ["hyuga", "hakama"], "requires": ["wrap", "kimono", "robe"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 4911, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    fabric(body.bottom, "D", "twill", 4911, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 4912, 2, 0, 8)
    hakama_legs(g, "hakama", "D", 4913, flare=4, length=10, top=0.0)
    tabi(g)
    # The waist ties crossing at the front and the stiff back board.
    band = g.piece("waist_tie", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.2, 0), inflate=.2)
    solid(band, "D", "weave", 4915, 3, edge=False)
    for face in band.sides:
        face.hline(0, face.w - 1, 0, "D3")
    board = g.piece("waist_board", "TORSO", (-2.5, 0, 0), (5, 2, 1), pivot=(0, 9.0, 2.3))
    solid(board, "D", "twill", 4916, 2)
    board.back.hline(0, 4, 0, "D3")
