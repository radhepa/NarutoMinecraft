"""Pleated Hakama: wide formal hakama in dark cloth, pressed pleats down a skirt that falls to the
ankle over the legs, a stiff back board, white tabi socks and straw sandals."""
from kit import flaps
from paint import fabric, k, solid, strip_fabric

META = {"name": "Pleated Hakama", "gender": "unisex",
        "description": "Wide dark pleated hakama to the ankle, stiff back board, white tabi, straw sandals.",
        "tags": ["hakama"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 1720, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 1720, 1)
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "D", "twill", 1721 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "twill", 1721, 2)
        strip_fabric(pants, "D", "twill", 1723, 2, 0, 9)
        for x in range(0, pants.strip.w, 2):
            pants.strip.vline(x, 0, 9, "D1")
        pants.strip.hline(0, pants.strip.w - 1, 9, "D0")
        # Tabi and straw zori.
        strip_fabric(leg, "S", "plain", 1724, 3, 10, 11)
        leg.front.vline(1, 10, 11, "S1")
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, k("L", 3))
        pants.bottom.fill("L2"), leg.bottom.fill("L1")
    for face in flaps(g, "hakama", 8, "D", "twill", 1725, width=9, top=11.0, front_z=-2.85, back_z=1.85):
        for x in (1, 3, 5, 7):
            face.vline(x, 1, 7, "D1")
    board = g.piece("waist_koshi_ita", "TORSO", (-2.5, 0, 0), (5, 2, 1), pivot=(0, 9.0, 2.1))
    solid(board, "D", "twill", 1726, 3, edge=False)
    tie = g.piece("waist_himo", "TORSO", (-4.5, 0, -2.5), (9, 1, 5), pivot=(0, 9.8, 0), inflate=.35)
    for face in tie.faces:
        face.fill("D3")
    tie.front.hline(3, 5, 0, "S3")
