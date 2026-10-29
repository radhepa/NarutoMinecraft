"""Village Long Skirt: a plain skirt to the ankles with a band of waves above the hem, worn with
simple sandals: the everyday skirt of the clan's harbor."""
from kit import flaps, side_panels
from kit_shinobi import sandals
from kit_uzumaki import waves
from paint import fabric, strip_fabric

META = {"name": "Village Long Skirt", "gender": "unisex",
        "description": "Plain ankle-length skirt with a wave band above the hem, sandals.",
        "tags": ["skirt"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 2410, 2, 9, 11)
    fabric(body.bottom, "P", "plain", 2410, 1)
    for side in ("right", "left"):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "P", "plain", 2411, 1, 0, 9)
        fabric(leg.top, "P", "plain", 2411, 1)
    sandals(g)
    for face in flaps(g, "skirt", 11, "P", "plain", 2412, width=9, hem="P1", top=11.2):
        waves(face, 8, "S", 3)
    side_panels(g, "skirt_side", 11, "P", "plain", hem="P1", top=11.2)
