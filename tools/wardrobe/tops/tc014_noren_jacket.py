"""Noren Jacket: a short cotton work jacket printed at the hem like a shop's doorway curtain, three
split panels with a pale mark on each, toggled down the front with cord loops."""
from kit_market import sleeves
from paint import cap, k, strip_fabric

META = {
    "name": "Noren Jacket",
    "gender": "unisex",
    "description": "Short cotton jacket printed at the hem like a split noren curtain, cord-toggled front.",
    "tags": ["civilian", "jacket", "casual"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 36280, 2)
    cap(body, "P", seed=36280)
    body.front.vline(3, 0, 11, k("P", 1)), body.front.vline(4, 0, 11, k("P", 3))
    for y in (2, 5, 8):
        body.front.set(3, y, "S3"), body.front.set(4, y, "L3")
    body.front.hline(2, 5, 0, k("P", 0))
    # The noren hem: a band of curtain panels split at the seams, each with a pale circle.
    for face in body.sides:
        for y in range(7, 12):
            for x in range(face.w):
                face.set(x, y, k("A", 2))
        for x in range(0, face.w, 3 if face.w > 4 else 4):
            face.vline(x, 8, 11, k("A", 0))
        for x in range(1, face.w - 1, 3 if face.w > 4 else 4):
            face.set(x + (1 if face.w > 4 else 1), 9, "S3")
        face.hline(0, face.w - 1, 7, k("A", 3))
    sleeves(g, "P", "weave", 36281, rows=(0, 10), cuff=k("A", 2))
