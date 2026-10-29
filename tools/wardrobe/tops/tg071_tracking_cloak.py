"""Tracking Cloak: the long trail cloak of the tracking unit, falling from the shoulders to the
knee behind, its hood worn down, over a fitted shirt with leather bracers and a pair of chest
straps that keep the cloak on in a run."""
from kit_aburame import hood_down
from kit_specialist import shirt
from paint import k, solid, strip_fabric

META = {
    "name": "Tracking Cloak",
    "gender": "unisex",
    "description": "Knee-length trail cloak behind, hood down, fitted shirt with leather bracers and chest straps.",
    "tags": ["shinobi", "cloak", "jonin"],
}


def build(g):
    body = shirt(g, "S", "weave", 34200)
    body.front.vline(4, 0, 4, "S1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "L", "leather", 34201, 2, 6, 10)
        arm.strip.hline(0, arm.strip.w - 1, 6, "L3"), arm.strip.hline(0, arm.strip.w - 1, 10, "L1")
        arm.strip.hline(0, arm.strip.w - 1, 8, "M3")
    jacket = g.part("jacket")
    for face in (jacket.front,):
        face.vline(1, 0, 11, "L2"), face.vline(6, 0, 11, "L2")
        face.hline(1, 6, 5, "L3")
    jacket.back.vline(1, 0, 3, "L2"), jacket.back.vline(6, 0, 3, "L2")
    cloak = g.piece("cloak", "TORSO", (-5, 0, 0), (10, 21, 1), pivot=(0, -.2, 2.5), rotation=(6, 0, 0), motion="flap_back")
    solid(cloak, "P", "twill", 34202, 2)
    for x in range(1, 10, 3):
        cloak.back.vline(x, 4, 20, "P1")
    cloak.back.hline(0, 9, 20, "P0"), cloak.back.hline(0, 9, 0, "P3")
    cloak.front.fill(k("P", 1))
    for side, x in (("right", -4.6), ("left", 4.6)):
        tie = g.piece(f"cloak_{side}_shoulder", "TORSO", (-1.5, 0, -2.5), (3, 1, 5), pivot=(x, -.4, 0), inflate=.1)
        solid(tie, "P", "twill", 34203, 3, edge=False)
    hood_down(g, "P", "twill", 34205)
