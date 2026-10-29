"""Training Wrap: an Academy-age Hatake's practice wear, a navy wrap top crossed left over right with a
white edge, short sleeves, a slate sash, bandaged forearms and the clan crest small on the back."""
from kit_hatake import CREST, decal
from kit_shinobi import bandage
from paint import cap, fabric, line, solid, strip_fabric

META = {
    "name": "Training Wrap",
    "gender": "unisex",
    "description": "Navy wrap top with a white edge, short sleeves, a slate sash and bandaged forearms.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 11801, 2)
    cap(body, "D", seed=11801)
    f = body.front
    line(f, 1, 0, 6, 7, "S3"), line(f, 0, 0, 5, 7, "S2")
    line(f, 6, 0, 4, 3, "D1")
    strip_fabric(jacket, "P", "weave", 11802, 2, 8, 9)
    jacket.strip.hline(0, jacket.strip.w - 1, 8, "P3")
    knot = g.piece("sash_knot", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(1.6, 8.0, -2.85))
    solid(knot, "P", "weave", 11803, 2)
    decal(g, "back_crest", CREST, {"o": "S3", "f": "S4"}, "D2", (0, 1.6, 2.1))
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "weave", 11804, 2, 0, 3)
        fabric(arm.top, "D", "weave", 11804, 3)
        strip_fabric(sleeve, "D", "weave", 11805, 2, 0, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 3, "S3")
        for face in arm.sides:
            bandage(face, 0, 6, face.w - 1, 10)
