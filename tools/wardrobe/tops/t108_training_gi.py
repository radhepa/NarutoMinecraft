"""Training Gi: a sleeveless cream gi wrapped and edged in the clan colour, a thick rope belt knotted
at the front with hanging ends, and bandaged forearms: the clan's dojo and forest-training wear."""
from kit_shinobi import bandage
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Training Gi",
    "gender": "unisex",
    "description": "Sleeveless cream gi edged in colour, knotted rope belt, bandaged forearms.",
    "tags": ["shinobi", "senju"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 1600, 2)
    cap(body, "S", seed=1600)
    f = body.front
    for i in range(9):
        x = 1 + i * 6 // 9
        f.set(x, i, "P2"), f.set(x + 1, i, "P1")
    f.set(6, 0, "P2"), f.set(7, 0, "P2")
    for face in (body.right, body.left):
        face.vline(0, 0, 11, "S1")
    # Shoulder caps of the gi on the arms.
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 1601, 2, 0, 1)
        fabric(arm.top, "S", "weave", 1601, 3)
        arm.strip.hline(0, arm.strip.w - 1, 1, "P2")
        bandage(arm.strip, 6, 6, 15, 10) if side == "left" else bandage(arm.strip, 0, 6, 15, 10)
    rope = g.piece("rope_belt", "TORSO", (-4.5, 0, -2.5), (9, 2, 5), pivot=(0, 8.6, 0), inflate=.3)
    for face in rope.faces:
        for y in range(face.h):
            for x in range(face.w):
                face.set(x, y, "L3" if (x + y) % 2 else "L2")
    knot = g.piece("rope_knot", "TORSO", (-1, 0, -1), (2, 2, 1), pivot=(.6, 8.6, -2.9))
    solid(knot, "L", "weave", 1602, 3, edge=False)
    for i, (x, rz) in enumerate(((.1, 8), (1.1, -6))):
        end = g.piece(f"rope_end_{i}", "TORSO", (0, 0, 0), (1, 4, 1), pivot=(x, 10.4, -3.0), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "L", "weave", 1603 + i, 2)
        end.front.set(0, 3, "L1")
