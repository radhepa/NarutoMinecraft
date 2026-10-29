"""Harbor Tunic: a sea-field work tunic in the clan color with the sleeves rolled above the elbow, a
sand sash wound twice round the waist with its ends hanging at the left hip and a wave stitched
along the hem."""
from kit import belt, roll
from kit_umino import waves
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Harbor Tunic",
    "gender": "unisex",
    "description": "Rolled-sleeve work tunic, a sand sash with hanging ends, a wave stitched along the hem.",
    "tags": ["shinobi", "work"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 18521, 2)
    cap(body, "P", seed=18521)
    f = body.front
    for i in range(4):
        f.set(2 + i, i, "P0")
    f.set(1, 0, "P3")
    waves(body.strip, 10, "A3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 18522 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "P", "weave", 18522, 3)
    roll(g, "P", 3.4)
    belt(g, "sash", y=7.8, role="S", height=2, buckle=None, inflate=.1)
    for i, (x, rz) in enumerate(((2.6, -6), (3.4, 8))):
        end = g.piece(f"sash_end_{i}", "TORSO", (-.5, 0, -.5), (1, 4, 1), pivot=(x, 9.4, -2.75), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "S", "weave", 18524 + i, 2)
