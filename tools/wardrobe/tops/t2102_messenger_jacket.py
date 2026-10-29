"""Messenger Jacket: a short gunmetal zip jacket for running dispatches between the gate and the
Hokage's tower, an off-white yoke across the shoulders, rust piping at the hem, plated bracers and
a dispatch satchel slung across the body."""
from kit import sleeves
from kit_hagane import bracers
from paint import cap, solid, strip_fabric

META = {
    "name": "Messenger Jacket",
    "gender": "unisex",
    "description": "Short gunmetal zip jacket, off-white shoulder yoke, rust piping, plated bracers, a dispatch satchel.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 21890, 2)
    cap(body, "D", seed=21890)
    strip_fabric(jacket, "P", "plain", 21891, 2, 0, 10)
    cap(jacket, "P", seed=21891)
    strip_fabric(jacket, "S", "plain", 21892, 2, 0, 2)
    jacket.strip.hline(0, jacket.strip.w - 1, 2, "A2")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "A2")
    jacket.front.vline(4, 0, 10, "M3"), jacket.front.vline(3, 3, 10, "P1")
    for arm in sleeves(g, "P", "plain", 21893, 2, rows=(0, 7)):
        strip_fabric(arm, "S", "plain", 21892, 2, 0, 2)
        arm.strip.hline(0, arm.strip.w - 1, 2, "A2")
    bracers(g, top=7.0, height=4, seed=21894)
    strap = g.piece("satchel_strap", "TORSO", (-.5, -7, -.5), (1, 14, 1), pivot=(0, 5.0, -2.7), rotation=(0, 0, -36))
    solid(strap, "L", "leather", 21895, 2)
    back = g.piece("satchel_strap_back", "TORSO", (-.5, -7, -.5), (1, 14, 1), pivot=(0, 5.0, 2.7), rotation=(0, 0, -36))
    solid(back, "L", "leather", 21896, 2)
    satchel = g.piece("satchel", "TORSO", (-1.5, 0, -2), (3, 3, 4), pivot=(-4.9, 8.6, 0))
    solid(satchel, "L", "leather", 21897, 2)
    satchel.right.hline(0, 3, 0, "L3"), satchel.right.set(2, 1, "M3")
