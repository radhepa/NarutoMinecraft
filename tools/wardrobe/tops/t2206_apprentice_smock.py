"""Apprentice Smock: an Academy child's short-sleeved indigo smock with the crest on the chest, a
cream canvas half apron tied at the waist with a pocket of nails, a carpenter's pencil in the collar
and a cloth tool bag on a cord across the body."""
from glyphs import stamp
from kit_kinoshita import CREST
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Apprentice Smock",
    "gender": "unisex",
    "description": "Short-sleeved indigo smock, a cream half apron with a nail pocket, a tool bag on a cord.",
    "tags": ["shinobi", "kinoshita", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 22401, 2)
    cap(body, "P", seed=22401)
    f = body.front
    for x in (3, 4):
        f.clear(x, 0)
    f.set(2, 0, "S3"), f.set(5, 0, "S3"), f.set(3, 1, "S3"), f.set(4, 1, "S3")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    # The crest small on the left breast, at double resolution.
    patch = g.piece("chest_crest", "TORSO", (-6, 0, 0), (12, 12, 1), pivot=(2.0, 2.6, -2.55), scale=(.25, .25, .25))
    fabric(patch.front, "P", "weave", 22402, 2)
    stamp(patch.front, CREST, 0, 0, {"#": "S4"})
    for face in (patch.top, patch.bottom, patch.right, patch.left, patch.back):
        face.fill("P2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 22403 + (side == "left"), 2, 0, 3)
        fabric(arm.top, "P", "weave", 22403, 3)
        arm.strip.hline(0, arm.strip.w - 1, 3, "A2")
    # The half apron: a waist tie and a cream panel to mid-thigh with a nail pocket.
    tie = g.piece("apron_tie", "TORSO", (-4.6, 8.8, -2.6), (9, 1, 5), inflate=.08)
    solid(tie, "S", "weave", 22405, 3, edge=False)
    apron = g.piece("apron", "TORSO", (-3, 0, 0), (6, 6, 1), pivot=(0, 9.8, -2.75), motion="flap_front")
    solid(apron, "S", "weave", 22406, 3)
    a = apron.front
    a.hline(0, 5, 0, "S4"), a.hline(1, 4, 2, "S2"), a.vline(1, 2, 4, "S2"), a.vline(4, 2, 4, "S2")
    a.set(2, 2, "M3"), a.set(3, 2, "M4")
    # The pencil behind the collar and a cloth bag on a cord.
    pencil = g.piece("pencil", "TORSO", (-.5, -3, -.5), (1, 3, 1), pivot=(-2.4, 1.0, -2.45), rotation=(0, 0, -16))
    solid(pencil, "A", "smooth", 22407, 3, edge=False)
    pencil.top.fill("K1")
    cord = g.piece("bag_cord", "TORSO", (-.5, -7, -.5), (1, 14, 1), pivot=(0, 5.0, 2.45), rotation=(0, 0, -36))
    solid(cord, "L", "leather", 22408, 2, edge=False)
    bag = g.piece("tool_bag", "TORSO", (-1.5, 0, -1), (3, 3, 2), pivot=(-3.6, 8.4, 1.4))
    solid(bag, "S", "weave", 22409, 2)
    bag.top.fill("K1"), bag.top.set(1, 0, "L3")
