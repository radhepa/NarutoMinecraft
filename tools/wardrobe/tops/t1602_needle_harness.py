"""Needle Harness: a fitted steel-grey shirt with a stand collar, two leather straps crossed over
the chest and back studded with senbon heads, a cuff of needles on each wrist and a plain belt: the
working kit of a senbon specialist."""
from kit import belt, collar
from kit_shiranui import bandolier, wrist_holster
from paint import cap, fabric, strip_fabric

META = {
    "name": "Needle Harness",
    "gender": "unisex",
    "description": "Fitted shirt with a stand collar, crossed leather straps studded with senbon, wrist cuffs.",
    "tags": ["shinobi"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 16770, 2)
    cap(body, "P", seed=16770)
    for face in (body.front, body.back):
        bandolier(face, "L", rows=9)
        bandolier(face, "L", rows=9, mirror=True)
    belt(g, "belt", y=9.4, role="L", buckle="M", inflate=.1)
    collar(g, "collar", "P", height=1, y=-.9)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 16772 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "P", "weave", 16772, 3)
        arm.strip.hline(0, arm.strip.w - 1, 11, "P1")
        wrist_holster(g, side, seed=16774, y=7.4)
