"""Clip Bob: a straight bob to the jaw, cut in soft points all round, with a blunt fringe to the
brows and the left side tucked back behind a dark clip: a practical cut for a young sealer."""
from anime import bangs, cel_box, lock, ring_shell
from kit_uzumaki import clip
from paint import scalp

META = {"name": "Clip Bob", "gender": "unisex",
        "description": "Jaw-length straight bob, blunt fringe, one side tucked back behind a clip."}


def build(g):
    scalp(g, 2130, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 2131, side_rows=7, back_rows=8, ring_row=1)
    back = g.piece("back", "HEAD", (-4.5, 0, -.5), (9, 8, 1), pivot=(0, -7.4, 4.6), rotation=(-6, 0, 0))
    cel_box(back, 2132, ring=1)
    for i, x in enumerate((-3, 0, 3)):
        lock(g, f"back_tip_{i}", (x, .6, 4.55), (-6, 0, 0), ((3, 1), (1, 1)), 1, 2133 + i, ring=None)
    right = g.piece("side_right", "HEAD", (-.5, 0, -3.6), (1, 8, 8), pivot=(-4.6, -7.6, .2), rotation=(0, 0, 4))
    cel_box(right, 2136, ring=1)
    lock(g, "point_right", (-4.4, .2, -3.0), (0, 0, 6), ((2, 1), (1, 1)), 1, 2137, ring=None)
    # The tucked side: shorter, swept back behind the ear under the clip.
    left = g.piece("side_left", "HEAD", (-.5, 0, -2), (1, 7, 6), pivot=(4.6, -7.6, 1.0), rotation=(0, 0, -4))
    cel_box(left, 2138, ring=1)
    bangs(g, "fringe", [(-2.9, ((2, 2), (1, 1)), 8), (-1.4, ((2, 2), (1, 1)), 4), (0, ((2, 2), (1, 1)), 0),
                        (1.4, ((2, 2), (1, 1)), -4), (2.9, ((2, 2), (1, 1)), -8)], seed=2139)
    clip(g, "clip", (4.85, -6.8, -2.4), (0, 90, 70), length=3, key="M")
    clip(g, "clip_2", (4.85, -5.9, -2.0), (0, 90, 70), length=3, key="M")
