"""Messenger Jacket: the courier corps' short zipped jacket with contrasting shoulder panels, sleeves
pushed up, a satchel strap across the chest and a capped message tube clipped to the hip."""
from kit import roll
from kit_specialist import scroll_tube, strap
from paint import cap, solid, strip_fabric

META = {
    "name": "Messenger Jacket",
    "gender": "unisex",
    "description": "Short zip jacket with contrast shoulder panels, pushed-up sleeves, chest strap and hip tube.",
    "tags": ["shinobi", "jacket", "chunin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 34340, 2)
    cap(body, "P", texture="weave", seed=34340)
    strip_fabric(body, "S", "weave", 34341, 3, 0, 2)
    body.strip.hline(0, body.strip.w - 1, 3, "S1")
    body.front.vline(4, 0, 11, "M2"), body.front.set(4, 0, "M3")
    body.strip.hline(0, body.strip.w - 1, 11, "P1"), body.strip.hline(0, body.strip.w - 1, 10, "P3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 34342, 3, 0, 1)
        strip_fabric(arm, "P", "weave", 34343 + (side == "left"), 2, 2, 6)
        cap(arm, "S", texture="weave", seed=34342, base=3)
    roll(g, "P", 4.4)
    strap(g, "chest_strap", (.2, 5.0), 40, 15, -2.6, seed=34345)
    strap(g, "back_strap", (.2, 5.0), -40, 15, 2.6, seed=34346)
    scroll_tube(g, "hip_tube", (4.6, 7.6, -.2), (0, 0, 8), length=5, role="L", seed=34347)
    pouch = g.piece("hip_pouch", "TORSO", (-1, 0, -1), (2, 2, 2), pivot=(-4.6, 9.6, -.6))
    solid(pouch, "L", "leather", 34348, 2)
