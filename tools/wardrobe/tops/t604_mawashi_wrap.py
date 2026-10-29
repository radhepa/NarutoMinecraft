"""Mawashi Wrap: a padded jacket with short quilted sleeves crossed over the belly, the thick folded
mawashi sash of a sumo wrestler round the waist with its knot at the back, and bandaged forearms:
an Akimichi's training wear."""
from kit_akimichi import quilt
from kit_shinobi import bandage
from paint import fabric, solid, strip_fabric

META = {
    "name": "Mawashi Wrap",
    "gender": "unisex",
    "description": "Padded crossed jacket, a thick mawashi sash knotted at the back, bandaged forearms.",
    "tags": ["shinobi", "genin", "akimichi"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 6756, 2)
    fabric(body.top, "S", "weave", 6756, 3)
    for face in jacket.sides:
        quilt(face, "P", 6757, 2, 0, 0, face.w, 9)
    fabric(jacket.top, "P", "weave", 6757, 3)
    # The jacket crosses left over right: a diagonal trimmed edge.
    f = jacket.front
    for y in range(9):
        x = 6 - y // 2
        f.set(x, y, "S3"), f.set(x - 1, y, "S2")
    f.set(6, 0, "S3"), f.set(7, 0, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        sleeve = g.part(f"{side}_sleeve")
        for face in sleeve.sides:
            quilt(face, "P", 6758, 2, 0, 0, face.w, 3)
        fabric(sleeve.top, "P", "weave", 6758, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 3, "P1")
        bandage(arm.strip, 0, 6, arm.strip.w - 1, 10)
        arm.strip.hline(0, arm.strip.w - 1, 6, "S1")
    # The mawashi: a thick folded band of heavy silk, its knot standing at the back.
    band = g.piece("mawashi", "TORSO", (-4.5, 8.2, -2.5), (9, 3, 5), inflate=.55)
    solid(band, "K", "rib", 6760, 2, edge=False)
    for face in band.sides:
        face.hline(0, face.w - 1, 0, "K4"), face.hline(0, face.w - 1, 2, "K1")
    knot = g.piece("mawashi_knot", "TORSO", (-1.5, 0, 0), (3, 3, 1), pivot=(0, 8.4, 2.9))
    solid(knot, "K", "rib", 6761, 3, edge=False)
