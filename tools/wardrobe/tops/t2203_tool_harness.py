"""Tool Harness: a close indigo sleeveless undershirt under a leather carpenter's harness, braces
over both shoulders crossed at the back, a pull saw slung behind the right shoulder, the steel
square hung down the back, a roll of chisels on the left brace and cloth hand guards on the wrists."""
from kit_kinoshita import chisel, saw, square
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Tool Harness",
    "gender": "unisex",
    "description": "Sleeveless indigo undershirt, a leather harness with a pull saw, steel square and chisels.",
    "tags": ["shinobi", "kinoshita", "work"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "rib", 22341, 2)
    cap(body, "P", seed=22341)
    body.front.set(3, 0, "P0"), body.front.set(4, 0, "P0")
    # Braces: straight down the front, crossed over the back, joined by a chest strap.
    f, b = body.front, body.back
    for x in (1, 6):
        fabric(f, "L", "leather", 22342, 2, x, 0, 1, 12)
    f.hline(1, 6, 4, "L2"), f.set(1, 4, "M3"), f.set(6, 4, "M3")
    for y in range(12):
        b.set(min(7, y * 7 // 11), y, "L2"), b.set(max(0, 7 - y * 7 // 11), y, "L2")
    fabric(body.top, "L", "leather", 22342, 3, 1, 0, 1, 4), fabric(body.top, "L", "leather", 22342, 3, 6, 0, 1, 4)
    for face in (body.right, body.left, f, b):
        face.hline(0, face.w - 1, 10, "L1"), face.hline(0, face.w - 1, 11, "L2")
    f.set(3, 10, "M3"), f.set(4, 10, "M3")
    # The chisel roll on the left brace.
    roll_ = g.piece("chisel_roll", "TORSO", (-1, 0, 0), (2, 4, 1), pivot=(2.6, 1.6, -2.6))
    solid(roll_, "L", "leather", 22343, 1)
    for i, x in enumerate((2.2, 3.0)):
        chisel(g, f"chisel_{i}", (x, 1.8, -2.75), (0, 0, 0))
    # The pull saw over the right shoulder and the steel square down the back.
    saw(g, "saw", (-2.2, 2.4, 2.75), (0, 0, 24), length=12)
    square(g, "square", (1.6, 1.0, 2.6), (0, 0, -4), long=16, short=7)
    # Bare arms, cloth tekko guards over the backs of the hands.
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        fabric(arm.strip, "S", "weave", 22344 + (side == "left"), 3, 0, 8, arm.strip.w, 3)
        arm.strip.hline(0, arm.strip.w - 1, 8, "S2")
        arm.strip.hline(0, arm.strip.w - 1, 10, "P2")
