"""Tracker Mantle: a belted tunic under a short shoulder mantle of hide edged with shaggy fur, the
kind a tracker throws on for a night in the hills, with a horn whistle on a cord at the chest."""
from kit import belt, sleeves
from kit_inuzuka import fur_edge, fur_box
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Tracker Mantle",
    "gender": "unisex",
    "description": "Belted tunic under a short hide mantle edged in shaggy fur, a whistle on a cord.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 8600, 2)
    cap(body, "P", texture="weave", seed=8600)
    body.front.vline(4, 4, 9, "P1")
    for arm in sleeves(g, "P", "weave", 8601, 2, rows=(0, 10)):
        arm.strip.hline(0, arm.strip.w - 1, 10, "K2")
    belt(g, "belt", y=9.0, role="L", buckle="M")
    # The mantle: a hide yoke over chest and back, caps over both shoulders and a short drape behind,
    # every hem shaggy with fur.
    yoke = g.piece("mantle", "TORSO", (-4.5, -.4, -2.5), (9, 4, 5), inflate=.35)
    solid(yoke, "L", "leather", 8603, 2)
    fabric(yoke.top, "L", "leather", 8603, 3)
    for face in yoke.sides:
        fur_edge(face, 2, "S", 8604, 2, 2)
    for side, bone, x in (("right", "RIGHT_ARM", -3.0), ("left", "LEFT_ARM", -1.0)):
        cap_ = g.piece(f"mantle_{side}", bone, (x, -2.4, -2), (4, 4, 4), inflate=.4)
        solid(cap_, "L", "leather", 8606 + (side == "left"), 2)
        fabric(cap_.top, "L", "leather", 8606, 3)
        for face in cap_.sides:
            fur_edge(face, 2, "S", 8608, 2, 2)
    drape = g.piece("mantle_drape", "TORSO", (-4.5, 0, 0), (9, 6, 1), pivot=(0, 2.6, 2.6), motion="flap_back")
    solid(drape, "L", "leather", 8609, 2)
    fur_edge(drape.back, 4, "S", 8612, 2, 2)
    cord = g.piece("whistle_cord", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(.6, 3.0, -3.0))
    solid(cord, "K", "plain", 8610, 2, edge=False)
    whistle = g.piece("whistle", "TORSO", (-.5, 0, -.5), (1, 2, 1), pivot=(.6, 6.0, -3.0))
    solid(whistle, "S", "smooth", 8611, 3)
    whistle.front.set(0, 1, "K1")
