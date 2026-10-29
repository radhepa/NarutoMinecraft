"""Gekko Hakama: wide pleated swordsman's trousers in deep indigo, the legs flaring to the ankle over
dark tabi-sandals, the front ties wrapped twice round the waist and knotted at the front."""
from kit import SIDES, leg_bone
from paint import fabric, k, solid, strip_fabric

META = {"name": "Gekko Hakama", "gender": "unisex",
        "description": "Wide pleated indigo hakama to the ankle, waist ties knotted in front, dark tabi-sandals.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 15500, 2, 9, 11)
    body.strip.hline(0, body.strip.w - 1, 9, "D3")
    fabric(body.bottom, "D", "twill", 15500, 1)
    for side in SIDES:
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 15501 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "twill", 15501, 2)
        strip_fabric(leg, "K", "smooth", 15503, 2, 10, 11)
        leg.front.hline(0, 3, 10, "K3")
        leg.bottom.fill("K1")
    # The wide legs: a pleated shell around each leg, flaring out at the hem.
    for side, sign in (("right", -1), ("left", 1)):
        bone = leg_bone(side)
        shell = g.piece(f"{side}_hakama", bone, (-2.5, 0, -2.5), (5, 8, 5), inflate=.3)
        strip_fabric(shell, "D", "twill", 15505 + (sign > 0), 2)
        fabric(shell.top, "D", "twill", 15505, 3), fabric(shell.bottom, "D", "twill", 15505, 0)
        for face in shell.sides:
            for x in range(1, face.w, 2):
                face.vline(x, 1, face.h - 1, "D1")
            face.hline(0, face.w - 1, 0, "D3")
        flare = g.piece(f"{side}_hakama_hem", bone, (-3, 8, -3), (6, 2, 6), inflate=.1)
        strip_fabric(flare, "D", "twill", 15507, 2)
        fabric(flare.top, "D", "twill", 15507, 2), fabric(flare.bottom, "D", "twill", 15507, 0)
        for face in flare.sides:
            for x in range(1, face.w, 2):
                face.vline(x, 0, 1, "D1")
            face.hline(0, face.w - 1, 1, "D0")
    # Waist ties: a band round the hips, a knot and two short ends at the front.
    band = g.piece("waist_ties", "TORSO", (-4.5, 9.4, -2.5), (9, 1, 5), inflate=.32)
    solid(band, "D", "weave", 15508, 3, edge=False)
    knot = g.piece("waist_knot", "TORSO", (-1, 0, 0), (2, 1, 1), pivot=(0, 9.4, -2.95))
    solid(knot, "D", "weave", 15509, 3)
    for i, (x, rz) in enumerate(((-.6, 8), (.6, -8))):
        end = g.piece(f"waist_tie_{i}", "TORSO", (-.5, 0, 0), (1, 3, 1), pivot=(x, 10.2, -3.0), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "D", "weave", 15510 + i, 3)
        end.front.set(0, 2, k("D", 1))
