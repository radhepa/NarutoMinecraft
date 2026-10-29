"""Field Hakama: wide pleated hakama cut to mid-calf for the farmer on market day, the back board
plain, worn over straw sandals with the shins showing."""
from kit_hyuga import hakama_legs
from kit_market import straw_sandals
from paint import fabric, k, solid, strip_fabric

META = {"name": "Field Hakama", "gender": "unisex",
        "description": "Wide pleated hakama cut to mid-calf, plain back board, straw sandals.",
        "tags": ["civilian", "hakama"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "L", "twill", 36755, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, k("L", 3))
    fabric(body.bottom, "L", "twill", 36755, 1)
    for side in ("right", "left"):
        strip_fabric(g.part(f"{side}_leg"), "L", "twill", 36756, 2, 0, 7)
    hakama_legs(g, "hakama", "L", 36757, flare=4, length=8, top=0.0)
    board = g.piece("waist_board", "TORSO", (-2.5, 0, 0), (5, 2, 1), pivot=(0, 9.0, 2.3))
    solid(board, "L", "twill", 36759, 2)
    straw_sandals(g, role="L")
