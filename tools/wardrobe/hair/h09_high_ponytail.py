"""High Ponytail: hair swept back from the face and tied high on the crown, a long tail arcing
out and down to the shoulder blades, side-swept bangs and two thin face-framing strands."""
from anime import bangs, cel_box, lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "High Ponytail", "gender": "unisex",
        "description": "Hair tied high on the crown in a long swinging tail, side-swept bangs, thin framing strands."}


def build(g):
    scalp(g, 901, side_rows=5, back_rows=7, sideburn=3)
    ring_shell(g, 902, side_rows=4, back_rows=6, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((3, 2), (2, 1), (1, 1)), 30), (-.8, ((3, 2), (2, 1)), 34),
                        (1.4, ((2, 1), (1, 1)), 22), (3.0, ((2, 2), (1, 1)), -14)], seed=930)
    sidelocks(g, "frame", 7, seed=940, x=4.3, z=-3.6, flare=2, width=1)
    tie = g.piece("tie", "HEAD", (-1.5, -1, -1.5), (3, 2, 3), pivot=(0, -7.2, 4.4))
    cel_box(tie, 950, base=0, top_delta=0)
    root = g.piece("tail_root", "HEAD", (-2, -2, 0), (4, 3, 3), pivot=(0, -7.4, 5.0), rotation=(20, 0, 0))
    cel_box(root, 955, base=2)
    lock(g, "ponytail", (0, -7.4, 6.2), (14, 0, 0), ((4, 3), (4, 4), (3, 4), (2, 3), (1, 2)), 3, 960, ring=None,
         motion="sway")
