"""Swept Part: a deep side part, one long lock swept right across the brow and down past the cheek,
the other side tucked short behind the ear, the back cut neat at the collar."""
from anime import curtain, lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "Swept Part", "gender": "unisex",
        "description": "Deep side part, a long lock swept across the brow and down past one cheek, collar-length back."}


def build(g):
    scalp(g, 16360, side_rows=6, back_rows=8, sideburn=2, part=6)
    ring_shell(g, 16361, side_rows=5, back_rows=8, ring_row=1)
    for i, (x, segs, rz) in enumerate(((3.0, ((2, 3), (2, 2), (1, 2)), 72), (1.6, ((2, 3), (2, 2), (1, 1)), 76),
                                       (0.2, ((2, 2), (1, 2)), 80))):
        lock(g, f"fringe_{i}", (x, -8.55, -4.35), (-10, 0, rz), segs, 1, 16362 + i * 7, ring=0)
    lock(g, "frame_long", (-4.3, -7.4, -3.2), (0, 0, 5), ((2, 5), (2, 2), (1, 2)), 1, 16380, ring=1)
    lock(g, "frame_short", (4.3, -7.4, -2.6), (0, 0, -4), ((1, 3), (1, 1)), 1, 16384, ring=1)
    sidelocks(g, "ear", 4, seed=16388, x=4.35, z=-.6, flare=2, width=2, taper=False)
    curtain(g, "fall", (0, -6.6, 4.6), (-4, 0, 0), 9, 5, hem=[(1, 2, 1), (4, 2, 1), (6, 2, 1)], seed=16392)
