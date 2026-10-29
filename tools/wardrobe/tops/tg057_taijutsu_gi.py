"""Taijutsu Gi: a short wrap gi with the sleeves rolled to the elbow and a dark band at the lapel,
tied with a thick knotted belt whose ends hang at the front, taped knuckles."""
from kit import roll, sleeves
from kit_kunoichi import wrap_front
from paint import cap, solid, strip_fabric

META = {
    "name": "Taijutsu Gi",
    "gender": "unisex",
    "description": "Short wrap gi, sleeves rolled to the elbow, a thick knotted belt, taped knuckles.",
    "tags": ["shinobi", "genin", "wrap", "taijutsu"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 33320, 3)
    cap(body, "S", texture="weave", seed=33320, base=3)
    wrap_front(body.front, "K", rows=8, base=2)
    sleeves(g, "S", "weave", 33321, base=3, rows=(0, 4))
    roll(g, "S", 3.0, base=3, prefix="gi_roll")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        arm.strip.hline(0, 15, 10, "S3"), arm.strip.hline(0, 15, 11, "S2")
    knot = g.piece("belt", "TORSO", (-4.6, 9.2, -2.6), (9, 2, 5), inflate=.06)
    solid(knot, "P", "weave", 33323, 2, edge=False)
    for i, (x, rz) in enumerate(((-1.4, 10), (-.4, -8))):
        end = g.piece(f"belt_end_{i}", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(x, 11.0, -2.9), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "P", "weave", 33324 + i, 2)
