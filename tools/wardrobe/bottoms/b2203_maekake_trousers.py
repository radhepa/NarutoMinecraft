"""Maekake Trousers: straight indigo trousers under a long canvas maekake, the shop apron tied round
the hips and falling to the knee with the crest stencilled at its foot, a cedar waist cord and
cream tabi with straw-soled sandals."""
from glyphs import stamp
from kit import legs, waistband
from kit_kinoshita import CREST, tabi
from paint import fabric, solid

META = {"name": "Maekake Trousers", "gender": "unisex",
        "description": "Straight indigo trousers, a long canvas shop apron with the crest, a cedar cord and tabi.",
        "tags": ["shinobi", "kinoshita"]}


def build(g):
    waistband(g, "D", "twill", 22641)
    legs(g, "D", "twill", 22642, rows=(0, 9))
    tabi(g, top=10, role="S", base=3, clasps=False)
    cord = g.piece("waist_cord", "TORSO", (-4.6, 9.2, -2.6), (9, 1, 5), inflate=.1)
    for face in cord.faces:
        face.paint(lambda x, y, cur: "A3" if x % 2 else "A1")
    apron = g.piece("maekake", "TORSO", (-4, 0, 0), (8, 8, 1), pivot=(0, 9.8, -2.85), motion="flap_front")
    solid(apron, "S", "weave", 22643, 2)
    a = apron.front
    a.hline(0, 7, 0, "S3"), a.hline(0, 7, 7, "S1")
    mark = g.piece("maekake_crest", "TORSO", (-6, 0, 0), (12, 12, 1), pivot=(0, 13.6, -3.0), scale=(1 / 3, 1 / 3, 1 / 3),
                   motion="flap_front")
    fabric(mark.front, "S", "weave", 22644, 2)
    stamp(mark.front, CREST, 0, 0, {"#": "P2"})
    for face in (mark.top, mark.bottom, mark.right, mark.left, mark.back):
        face.fill("S2")
