"""Timber Cuirass: the fortification crew's breastplate of planed hinoki slats laced edge to edge
with indigo cord, timber shoulder boards on cords over an indigo work shirt with rolled sleeves and
a cedar sash. Ordinary joinery, nothing grown: the slats are pegged and the pegs show."""
from kit import belt, roll
from kit_kinoshita import wood_grain
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Timber Cuirass",
    "gender": "unisex",
    "description": "Breastplate of planed slats laced with indigo cord, shoulder boards, rolled indigo sleeves.",
    "tags": ["shinobi", "kinoshita", "armor"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 22441, 2)
    cap(body, "P", seed=22441)
    # The cuirass: vertical slats, laced across the middle, pegged at the top.
    plate = g.piece("cuirass", "TORSO", (-4.5, .6, -2.65), (9, 8, 5), inflate=.08)
    for face in plate.sides:
        wood_grain(face, "S", 22442 + face.x0, 2)
        for x in range(0, face.w, 3):
            face.vline(x, 0, face.h - 1, "S1")
        face.hline(0, face.w - 1, 0, "S3")
        face.hline(0, face.w - 1, face.h - 1, "S0")
        face.hline(0, face.w - 1, 4, "P2")
    fabric(plate.top, "S", "smooth", 22443, 3), fabric(plate.bottom, "S", "smooth", 22443, 1)
    for x in (1, 4, 7):
        plate.front.set(x, 1, "L1")
    belt(g, "sash", y=8.8, role="A", height=2, buckle=None, inflate=.12)
    # Shoulder boards on cords.
    for side, bone, ox in (("right", "RIGHT_ARM", -3.0), ("left", "LEFT_ARM", -1.0)):
        board = g.piece(f"{side}_board", bone, (ox - .4, -.6, -2.6), (5, 3, 5), inflate=.05)
        for face in board.sides:
            wood_grain(face, "S", 22444, 2)
            face.hline(0, face.w - 1, 0, "S3"), face.hline(0, face.w - 1, 2, "S0")
        fabric(board.top, "S", "smooth", 22445, 3), fabric(board.bottom, "S", "smooth", 22445, 1)
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 22446 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "P", "weave", 22446, 3)
    roll(g, "P", 4.0)
