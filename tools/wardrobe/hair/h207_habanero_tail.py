"""Habanero Tail: the long hair tied up high in a cloth wrap for work or a fight, a thick tail
swinging down past the shoulder blades, a side-swept fringe with a dark clip and long face locks."""
from anime import bangs, cel_box, lock, ring_shell, sidelocks
from kit_uzumaki import clip, wrap_tie
from paint import scalp

META = {"name": "Habanero Tail", "gender": "unisex",
        "description": "High tail in a cloth wrap swinging past the shoulder blades, swept fringe, side clip."}


def build(g):
    scalp(g, 2110, side_rows=5, back_rows=7, sideburn=3)
    ring_shell(g, 2111, side_rows=5, back_rows=6, ring_row=1)
    root = g.piece("tail_root", "HEAD", (-2, -2, 0), (4, 3, 3), pivot=(0, -7.2, 4.8), rotation=(20, 0, 0))
    cel_box(root, 2112, base=2)
    wrap_tie(g, "wrap", (0, -7.6, 6.2), (14, 0, 0), (4, 2, 4), y=-.5, key="A")
    lock(g, "tail", (0, -7.0, 6.4), (16, 0, 0), ((4, 4), (4, 4), (3, 4), (3, 3), (2, 2), (1, 2)), 3, 2113, ring=None,
         motion="sway")
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 30), (-1.2, ((2, 2), (1, 1)), 30), (.4, ((2, 2), (1, 1)), 26),
                        (2.0, ((2, 1), (1, 1)), 14), (3.2, ((2, 2), (1, 1)), -10)], seed=2114)
    sidelocks(g, "frame", 11, seed=2115, x=4.3, z=-3.4, flare=3, width=2)
    clip(g, "clip", (3.1, -7.9, -4.75), (-10, 0, -40))
