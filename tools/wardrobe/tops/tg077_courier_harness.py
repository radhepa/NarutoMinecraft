"""Courier Harness: the messenger corps' light kit, a short-sleeved tunic under a leather harness
crossing the chest and back, a message tube strapped across the back and wrapped forearms: the
runner who carries the village's scrolls from post to post."""
from kit_specialist import scroll_tube, strap
from kit_yamanaka import wrapped
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Courier Harness",
    "gender": "unisex",
    "description": "Short-sleeved tunic, crossed leather chest harness, message tube on the back, wrapped forearms.",
    "tags": ["shinobi", "tunic", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 34320, 2)
    cap(body, "P", texture="weave", seed=34320)
    body.strip.hline(0, body.strip.w - 1, 11, "S3")
    body.front.hline(2, 5, 0, "S3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 34321, 2, 0, 3)
        fabric(arm.top, "P", "weave", 34321, 3)
        arm.strip.hline(0, arm.strip.w - 1, 3, "S3")
        wrapped(arm.strip, 0, 7, arm.strip.w - 1, 10, "S")
    for i, rz in enumerate((-34, 34)):
        strap(g, f"harness_front_{i}", (0, 5.0), rz, 13, -2.6, seed=34322 + i)
        strap(g, f"harness_back_{i}", (0, 5.0), rz, 13, 2.6, seed=34324 + i)
    ring = g.piece("harness_ring", "TORSO", (-1, -1, 0), (2, 2, 1), pivot=(0, 5.0, -3.0))
    solid(ring, "M", "plain", 34326, 3, edge=False)
    scroll_tube(g, "message_tube", (-3.2, 1.0, 3.6), (0, 0, -40), length=10, role="L", seed=34327)
    belt_ = g.piece("harness_belt", "TORSO", (-4.6, 9.2, -2.6), (9, 1, 5), inflate=.08)
    solid(belt_, "L", "leather", 34328, 2, edge=False)
