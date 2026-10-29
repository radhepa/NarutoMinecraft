"""Wild Tail: a spiky mane pulled back and tied at the nape into a thick, bristling tail that flares
out in spikes to the shoulder blades, with spiky locks left free in front of the ears."""
from anime import bangs, cel_box, lock, ring_shell, sidelocks, spike
from kit_akimichi import flick
from paint import scalp

META = {"name": "Wild Tail", "gender": "unisex",
        "description": "Spiky hair tied at the nape into a thick bristling tail, spiky locks before the ears."}


def build(g):
    scalp(g, 6181, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 6181, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.4, -2.0, -30, -26), (0, -2.4, -34, 0), (2.4, -2.0, -30, 26),
                                        (-1.6, 1.0, -50, -18), (1.6, 1.0, -50, 18))):
        spike(g, f"crown_{i}", (x, -7.8, z), (rx, 0, rz), ((3, 2), (2, 2), (1, 1)), 2, 6187 + i)
    tie = g.piece("tie", "HEAD", (-1.5, -.5, -1), (3, 1, 2), pivot=(0, -3.6, 4.9))
    cel_box(tie, 6194, base=0, top_delta=0)
    lock(g, "tail", (0, -3.4, 5.2), (16, 0, 0), ((5, 3), (4, 4), (3, 3), (1, 2)), 3, 6201, ring=None, motion="sway")
    for i, (rz, rx) in enumerate(((34, 30), (-34, 30), (20, 50), (-20, 50))):
        flick(g, f"tail_spike_{i}", (0, -2.0, 5.6), (rx, 0, rz), ((2, 3), (1, 2)), 2, 6208 + i, motion="sway")
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 24), (-.2, ((2, 2), (1, 1)), 6), (2.2, ((2, 2), (1, 1)), -20)], seed=6215)
    sidelocks(g, "ear", 7, seed=6222, x=4.35, z=-3.2, flare=12, width=2)
