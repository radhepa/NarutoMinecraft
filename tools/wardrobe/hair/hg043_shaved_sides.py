"""Shaved Sides: the sides and back clipped to stubble, a thick crest of hair left on top and swept
back into a row of tall spikes that ends at the crown: a fighter's cut that keeps the eyes clear."""
from anime import spike
from paint import hair_face, k, rnd

META = {"name": "Shaved Sides", "gender": "unisex",
        "description": "Sides and back clipped to stubble, a thick crest on top swept back into a row of tall spikes."}

# Crest spikes from the brow to the crown: (z, segments, lean back)
CREST = [(-3.0, ((4, 2), (3, 2), (2, 2), (1, 1)), 46), (-1.2, ((4, 3), (3, 2), (2, 2), (1, 1)), 56),
         (.8, ((4, 3), (3, 2), (2, 2), (1, 1)), 64), (2.6, ((4, 2), (3, 2), (2, 2), (1, 1)), 74)]


def stubble(face, seed, rows):
    for y in rows:
        for x in range(face.w):
            # Clipped stubble: a soft shadow over the skin with the odd darker root.
            face.set(x, y, "X1" if rnd(x, y, seed) < .75 else "X2")


def build(g):
    head, hat = g.part("head"), g.part("hat")
    hair_face(head.top, 35660, 2)
    for face in (head.right, head.left, head.back):
        stubble(face, 35661 + face.x0, range(0, 5 if face is not head.back else 7))
    head.front.hline(1, 6, 0, "H1")
    for x in range(8):
        for y in range(8):
            if 2 <= x <= 5:
                hat.top.set(x, y, k("H", 3 if 3 <= x <= 4 else 2))
    for i, (z, segs, rx) in enumerate(CREST):
        spike(g, f"crest_{i}", (0, -7.7, z), (-rx, 0, 0), segs, 3, 35664 + i * 2)
    for i, (x, rz) in enumerate(((-1.6, -12), (1.6, 12))):
        spike(g, f"crest_side_{i}", (x, -7.8, .4), (-60, 0, rz), ((2, 2), (1, 2)), 2, 35674 + i)
