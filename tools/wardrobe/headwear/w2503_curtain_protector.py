"""Curtain Protector: the forehead protector on a dark band, with a cloth curtain hung from the band
behind the ears and down over the nape, against the night chill and the watchman's lantern glare."""
from kit_shinobi import forehead_protector
from kit_tobari import pleats
from paint import solid

META = {"name": "Curtain Protector", "gender": "unisex",
        "description": "Forehead protector on a dark band with a pleated neck curtain hung behind the ears."}


def build(g):
    forehead_protector(g, band="K", seed=25840)
    back = g.piece("curtain_back", "HEAD", (-4.5, 0, 0), (9, 7, 1), pivot=(0, -7.2, 4.75), rotation=(6, 0, 0),
                   motion="sway")
    solid(back, "D", "twill", 25845, 2)
    pleats(back.back, "D")
    for side, x in (("right", -4.75), ("left", 4.75)):
        panel = g.piece(f"curtain_{side}", "HEAD", (-.5, 0, 0), (1, 6, 4), pivot=(x, -7.2, .6))
        solid(panel, "D", "twill", 25846 + (x > 0), 2)
        pleats(panel.right if x < 0 else panel.left, "D")
