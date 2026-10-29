"""Ramen Cook's Jacket: the noodle stand's white cook jacket, wrapped and tied at the side, the
sleeves cut short of the wrist to stay out of the broth, a tenugui towel round the neck and a dark
cord at the waist."""
from kit_kurama import wrap_front
from kit_market import sash, sleeves, towel_at_neck
from paint import cap, strip_fabric

META = {
    "name": "Ramen Cook's Jacket",
    "gender": "unisex",
    "description": "White wrapped cook jacket tied at the side, sleeves cut above the wrist, towel at the neck, dark waist cord.",
    "tags": ["civilian", "work", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 36020, 3)
    cap(body, "P", seed=36020, base=3)
    wrap_front(body.front, "P1", "P4", rows=8, start=1)
    # The inner tie at the wearer's left hip, and the seam down each side.
    body.front.set(7, 7, "D2"), body.front.set(7, 8, "D2")
    for y in range(12):
        body.right.set(3, y, "P2"), body.left.set(0, y, "P2")
    sleeves(g, "P", "weave", 36021, rows=(0, 7), base=3)
    towel_at_neck(g, "S", 36024, accent="A2")
    sash(g, "waist_cord", "D", 36026, y=8.8, height=1, knot="front")
