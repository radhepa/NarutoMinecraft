"""Kasuri Long Skirt: a plain ankle-length skirt of kasuri cotton for the market women and the
teahouse girls, a darker band at the hem, worn with straw zori."""
from kit import flaps, side_panels
from kit_market import kasuri, straw_sandals
from paint import fabric, k, strip_fabric

META = {"name": "Kasuri Long Skirt", "gender": "unisex",
        "description": "Ankle-length kasuri cotton skirt with a darker hem band, straw zori.",
        "tags": ["civilian", "skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 36785, 2, 9, 11)
    fabric(body.bottom, "D", "weave", 36785, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "weave", 36786, 1, 0, 9)
        fabric(leg.top, "D", "weave", 36786, 1)
    for face in flaps(g, "skirt", 11, "D", "weave", 36787, width=9, hem=k("D", 0), top=11.2):
        kasuri(face, k("S", 2), 36788, rows=range(1, 9))
        face.hline(0, 8, 9, k("D", 1))
    side_panels(g, "skirt_side", 11, "D", "weave", hem=k("D", 0), top=11.2)
    straw_sandals(g)
