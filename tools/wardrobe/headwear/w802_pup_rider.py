"""Pup Rider: a small white ninken puppy riding on top of its partner's head, lying with its paws
over the brow, ears flopped, tail curled at the back and a red collar."""
from paint import fabric, solid

META = {"name": "Pup Rider", "gender": "unisex", "hides_hair": ["crown"],
        "description": "A small white puppy riding on the head, paws over the brow, a red collar."}


def build(g):
    body = g.piece("pup_body", "HEAD", (-2, -3, -2), (4, 3, 6), pivot=(0, -8.0, 0))
    solid(body, "S", "plain", 8930, 3)
    fabric(body.top, "S", "plain", 8930, 4)
    head = g.piece("pup_head", "HEAD", (-2, -4, -2), (4, 4, 3), pivot=(0, -8.4, -3.2))
    solid(head, "S", "plain", 8931, 3)
    fabric(head.top, "S", "plain", 8931, 4)
    f = head.front
    f.fill("S3")
    f.hline(0, 3, 0, "S4")
    f.set(0, 1, "K0"), f.set(3, 1, "K0")
    # The snout at half scale so the nose can be one small dark button.
    snout = g.piece("pup_snout", "HEAD", (-2, -4, -2), (4, 4, 2), pivot=(0, -8.4, -5.2), scale=(.5, .5, .5))
    solid(snout, "S", "plain", 8932, 4, edge=False)
    snout.front.fill("S4")
    snout.front.hline(1, 2, 0, "K0"), snout.front.set(1, 1, "K1"), snout.front.set(2, 1, "K1")
    snout.front.hline(0, 3, 3, "S2")
    collar = g.piece("pup_collar", "HEAD", (-2, -1, -.5), (4, 1, 1), pivot=(0, -8.4, -1.6), inflate=.1)
    solid(collar, "A", "plain", 8933, 2, edge=False)
    for i, (x, rz) in enumerate(((-2.2, -20), (2.2, 20))):
        ear = g.piece(f"pup_ear_{i}", "HEAD", (-.5, 0, -1), (1, 3, 2), pivot=(x, -12.2, -3.2), rotation=(0, 0, rz))
        solid(ear, "L", "plain", 8934 + i, 3, edge=False)
    for i, x in enumerate((-1.4, 1.4)):
        pawb = g.piece(f"pup_paw_{i}", "HEAD", (-.5, -1, -1), (1, 1, 2), pivot=(x, -8.0, -4.4))
        solid(pawb, "S", "plain", 8936 + i, 3, edge=False)
    tail = g.piece("pup_tail", "HEAD", (-.5, -3, -.5), (1, 3, 1), pivot=(.6, -10.0, 4.0), rotation=(-30, 0, 20))
    solid(tail, "S", "plain", 8938, 3, edge=False)
