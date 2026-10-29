"""Fume Mask: the half-face cloth mask the Suzuran tie on before they open a jar of toxin, white
cotton pleated over the nose and mouth, edged in leaf green, with a sprig of bells stitched on the
cheek and the ties knotted behind the head."""
from kit_suzuran import bell_sprig
from paint import k, solid

META = {"name": "Fume Mask", "gender": "unisex", "covers_mouth": True,
        "description": "White pleated half mask over the nose and mouth, green edge, a stitched bell sprig, tied behind."}


def build(g):
    mask = g.piece("fume_mask", "HEAD", (-4, -1.75, -4), (8, 2, 8), inflate=.25)
    solid(mask, "S", "weave", 24801, 3, edge=False)
    for face in mask.sides:
        face.hline(0, face.w - 1, 0, "D2")
    mask.front.hline(1, 6, 1, k("S", 2))
    mask.front.vline(3, 0, 1, "S4"), mask.front.set(4, 1, "S2")
    bell_sprig(mask.right, 4, 0, stem="D2", bell="S4", shade="S2", bells=2)
    pleat = g.piece("fume_mask_pleat", "HEAD", (-3, -.6, -4), (6, 1, 1), inflate=.3)
    solid(pleat, "S", "weave", 24802, 2, edge=False)
    pleat.front.hline(0, 5, 0, "S2")
    knot = g.piece("fume_mask_knot", "HEAD", (-1, -1, 0), (2, 2, 1), pivot=(0, -1.0, 4.4))
    solid(knot, "S", "weave", 24803, 3)
    for i, (x, rz) in enumerate(((-.5, 16), (.5, -12))):
        tie = g.piece(f"fume_mask_tie_{i}", "HEAD", (-.5, 0, 0), (1, 3, 1), pivot=(x, -.4, 4.7), rotation=(14, 0, rz),
                      motion="sway")
        solid(tie, "S", "weave", 24804 + i, 3)
        tie.back.set(0, 2, "D2")
