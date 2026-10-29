"""Instructor Vest: the Academy teacher's cloth vest, buttoned over a long-sleeved shirt with the
collar points showing, two chest pockets (a brush in one, chalk in the other) and the shirt
sleeves pushed to the elbow for the blackboard."""
from kit import roll
from kit_specialist import shirt
from paint import cap, solid, strip_fabric

META = {
    "name": "Instructor Vest",
    "gender": "unisex",
    "description": "Buttoned cloth vest over a collared shirt with sleeves pushed up, two chest pockets.",
    "tags": ["shinobi", "vest", "chunin"],
}


def build(g):
    body = shirt(g, "S", "weave", 34240, arm_rows=(0, 6))
    body.front.set(3, 0, "S4"), body.front.set(4, 0, "S4")
    roll(g, "S", 4.4)
    jacket = g.part("jacket")
    strip_fabric(jacket, "P", "weave", 34242, 2, 0, 11)
    cap(jacket, "P", texture="weave", seed=34242)
    f = jacket.front
    for x, y in [(2, 0), (3, 0), (4, 0), (5, 0), (3, 1), (4, 1), (3, 2), (4, 2)]:
        f.clear(x, y)
    f.vline(4, 3, 11, "P0"), f.vline(3, 3, 11, "P3")
    for y in (4, 6, 8, 10):
        f.set(3, y, "M3")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "P1")
    for face in (jacket.right, jacket.left):
        face.vline(1, 0, 11, "P1")
    for i, x in enumerate((-3.5, 1.5)):
        pocket = g.piece(f"chest_pocket_{i}", "TORSO", (0, 0, 0), (2, 2, 1), pivot=(x, 3.4, -2.75))
        solid(pocket, "P", "weave", 34244 + i, 2)
        pocket.front.hline(0, 1, 0, "P3")
    brush = g.piece("pocket_brush", "TORSO", (-.5, -2, -.5), (1, 2, 1), pivot=(-2.4, 3.6, -2.9), scale=(.5, .5, .5))
    solid(brush, "L", "smooth", 34246, 3, edge=False)
    brush.top.fill("K1")
    chalk = g.piece("pocket_chalk", "TORSO", (-.5, -2, -.5), (1, 2, 1), pivot=(2.6, 3.6, -2.9), scale=(.5, .5, .5))
    for face in chalk.faces:
        face.fill("S4")
