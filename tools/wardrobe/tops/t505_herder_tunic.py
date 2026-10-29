"""Herder Tunic: the deer keeper's work tunic, sleeves rolled to the elbow, a leather apron front with
a pocket of feed, a cross strap and an antler-tip toggle at the collar."""
from kit import belt, roll
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Herder Tunic",
    "gender": "unisex",
    "description": "Rolled-sleeve work tunic with a leather apron, a cross strap and an antler toggle.",
    "tags": ["shinobi", "nara", "work"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 5541, 2)
    cap(body, "P", texture="weave", seed=5541)
    f = body.front
    f.set(3, 0, None), f.set(4, 0, None), f.set(3, 1, "P0"), f.set(4, 1, "P0")
    # The apron: leather from the chest to the hip, a feed pocket across the front.
    fabric(f, "L", "leather", 5542, 2, 1, 3, 6, 7)
    f.hline(1, 6, 3, "L3")
    f.hline(2, 5, 7, "L1"), f.set(2, 8, "L1"), f.set(5, 8, "L1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 5543 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "P", "weave", 5543, 3)
    roll(g, "P", 3.6, prefix="sleeve_roll")
    belt(g, "belt", y=9.0, role="L", height=1, buckle="M")
    # The cross strap from the right shoulder to the left hip.
    strap = g.piece("strap", "TORSO", (-.5, -7.5, -.5), (1, 15, 1), pivot=(0, 5.0, -2.45), rotation=(0, 0, 36))
    solid(strap, "L", "leather", 5545, 1, edge=False)
    # Antler-tip toggle at the collar.
    toggle = g.piece("toggle", "TORSO", (-1, 0, 0), (2, 1, 1), pivot=(0, 1.6, -2.6), rotation=(0, 0, -20))
    solid(toggle, "S", "smooth", 5546, 3, edge=False)
    toggle.front.set(1, 0, "S2")
