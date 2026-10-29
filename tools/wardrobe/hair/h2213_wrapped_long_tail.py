"""Wrapped Long Tail: long hair swept back off the face and tied high at the back of the head, the
tail wound in a band of cream cloth for a hand's length and then let fall to the middle of the back."""
from anime import cel_box, lock, ring_shell, sidelocks
from paint import k, scalp, solid

META = {"name": "Wrapped Long Tail", "gender": "unisex",
        "description": "Long hair swept back into a high tail wrapped in cream cloth, then falling to mid-back."}


def build(g):
    scalp(g, 22261, side_rows=5, back_rows=8, sideburn=2)
    hat = ring_shell(g, 22262, side_rows=5, back_rows=8, ring_row=1)
    for x in (2, 5):
        hat.top.vline(x, 0, 7, k("H", 1))
    root = g.piece("tail_root", "HEAD", (-1.5, -1.5, -1), (3, 3, 2), pivot=(0, -6.4, 4.6), rotation=(-20, 0, 0))
    cel_box(root, 22263)
    wrap = g.piece("tail_wrap", "HEAD", (-1.5, 0, -1.5), (3, 4, 3), pivot=(0, -5.4, 5.6), rotation=(24, 0, 0),
                   inflate=.05, motion="sway")
    solid(wrap, "S", "weave", 22264, 3, edge=False)
    for face in wrap.sides:
        for y in range(4):
            face.set((y * 2) % face.w, y, "S1")
    lock(g, "tail", (0, -5.4, 5.6), (24, 0, 0), ((3, 4), (3, 4), (2, 3), (1, 2)), 2, 22266, ring=None,
         motion="sway", y0=4.0)
    sidelocks(g, "temple", 5, seed=22272, x=4.2, z=-3.0, flare=4, width=1)
