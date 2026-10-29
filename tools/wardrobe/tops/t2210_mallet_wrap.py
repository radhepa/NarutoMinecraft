"""Mallet Wrap: a sleeveless cross-collared work top in cedar cloth wrapped right over left, a wide
indigo obi with a coil of marking cord, the carpenter's wooden mallet hanging at the right hip and
cream tekko guards bound over the forearms."""
from kit import belt
from kit_kinoshita import mallet
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Mallet Wrap",
    "gender": "unisex",
    "description": "Sleeveless cedar wrap top, a wide indigo obi, a wooden mallet at the hip, forearm guards.",
    "tags": ["shinobi", "kinoshita", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "A", "weave", 22481, 2)
    cap(body, "A", seed=22481)
    f = body.front
    for y in range(7):
        f.set(1 + y * 5 // 6, y, "S3"), f.set(2 + y * 5 // 6, y, "A1")
    for x in (3, 4):
        f.clear(x, 0)
    for face in (body.right, body.left):
        face.set(0, 0, "A3")
    obi = belt(g, "obi", y=7.6, role="P", height=3, buckle=None, inflate=.12)
    obi.front.hline(0, 8, 1, "P1")
    # The marking cord: an ink line coil tucked in the obi.
    reel = g.piece("ink_reel", "TORSO", (-1, -1, -.5), (2, 2, 1), pivot=(-2.4, 8.9, -2.9))
    solid(reel, "K", "smooth", 22482, 3, edge=False)
    reel.front.set(0, 0, "A3"), reel.front.set(1, 1, "S3")
    mallet(g, "mallet", (-4.9, 10.0, -.6), (0, 0, 8), motion="sway")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        fabric(arm.strip, "S", "weave", 22483 + (side == "left"), 3, 0, 6, arm.strip.w, 5)
        arm.strip.hline(0, arm.strip.w - 1, 6, "S1")
        for y in (7, 9):
            for x in range(0, arm.strip.w, 3):
                arm.strip.set(x, y, "P2")
