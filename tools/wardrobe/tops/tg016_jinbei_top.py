"""Jinbei Top: a light summer top that wraps and ties at the side, piped along the crossing edge, with
straight short sleeves and vented side seams: the genin who trains in the heat."""
from kit_academy import shirt
from paint import solid

META = {
    "name": "Jinbei Top",
    "gender": "unisex",
    "description": "Summer wrap top piped along the crossing edge and tied at the side, straight short sleeves.",
    "tags": ["shinobi", "genin", "wrap"],
}


def build(g):
    body, arms = shirt(g, "P", "weave", 31225, sleeve=4)
    f = body.front
    for y in range(10):
        x = 1 + y * 5 // 9
        f.set(x, y, "S3")
        if x + 1 <= 7:
            f.set(x + 1, y, "P1")
    f.vline(6, 0, 3, "S3")
    for arm in arms:
        arm.strip.hline(0, arm.strip.w - 1, 4, "S3")
        arm.front.vline(1, 0, 3, "P1")
    for face in (body.right, body.left):
        face.vline(1, 8, 11, "P0")
    body.strip.hline(0, body.strip.w - 1, 11, "S3")
    for i, (y, n) in enumerate(((6.0, 3), (6.4, 2))):
        tie = g.piece(f"tie_{i}", "TORSO", (0, 0, 0), (1, n, 1), pivot=(-2.4 + i * .8, y, -2.6), rotation=(0, 0, 12 - 24 * i),
                      motion="flap_front", scale=(.5, 1, .5))
        solid(tie, "S", "plain", 31226 + i, 3, edge=False)
