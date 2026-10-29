"""Proctor Vest: the flak vest of a jonin seconded to the Academy and the exams, over a dark
long-sleeved shirt, with a plain duty armband in the corps colour on the left arm and an
examiner's clipboard of scrolls on a cord at the hip."""
from kit_shinobi import flak_vest
from kit_specialist import cross_armband, scroll_tube, shirt
from paint import solid

META = {
    "name": "Proctor Vest",
    "gender": "unisex",
    "description": "Flak vest over a dark shirt, plain duty armband, a cord of exam scrolls at the hip.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    shirt(g, "D", "weave", 34260, cuff="D1")
    flak_vest(g, shoulder_swirls=True, seed=34262)
    cross_armband(g, "left", y=.4, band="A", mark=None, base=2, seed=34270)
    cord = g.piece("scroll_cord", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(-4.4, 9.2, -1.0))
    solid(cord, "A", "weave", 34271, 2, edge=False)
    for i, z in enumerate((-1.4, .2)):
        scroll_tube(g, f"exam_scroll_{i}", (-4.9, 11.4, z), (90, 0, 0), length=3, role="S", end="A2", seed=34272 + i)
