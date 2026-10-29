"""Ankle-Tie Trousers: straight light trousers split at the ankle and tied off with cloth ties whose
ends trail at the heel, a waist sash and open-toe sandals."""
from kit_academy import leg_cloth, waist
from kit_shinobi import sandals
from paint import k, solid

META = {"name": "Ankle-Tie Trousers", "gender": "unisex",
        "description": "Straight trousers tied off at the ankle with trailing cloth ties, open-toe sandals.",
        "tags": ["shinobi", "genin"]}


def build(g):
    waist(g, "D", "weave", 31580, band="A2")
    for side, leg in zip(("right", "left"), leg_cloth(g, "D", "weave", 31581, (0, 9))):
        leg.front.vline(1 if side == "right" else 2, 1, 8, "D3")
        leg.strip.hline(0, leg.strip.w - 1, 9, "A2")
        outer = leg.right if side == "right" else leg.left
        outer.vline(2, 7, 9, "D0")
    sandals(g)
    for side, bone, x in (("right", "RIGHT_LEG", -2.3), ("left", "LEFT_LEG", 2.3)):
        for i in range(2):
            tie = g.piece(f"{side}_ankle_tie_{i}", bone, (0, 0, 0), (1, 2 - i, 1), pivot=(x, 9.4, -.4 + i * .6),
                          rotation=(0, 0, (20 + 14 * i) * (1 if x < 0 else -1)), scale=(.5, 1, .5), motion="sway")
            solid(tie, "A", "weave", 31583 + i, 2, edge=False)
            tie.front.set(0, 0, k("A", 3))
