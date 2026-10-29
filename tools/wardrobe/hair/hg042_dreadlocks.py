"""Dreadlocks: thick rope-like locks falling from the crown to the shoulders all round, the front
ones swept back off the face, a few bound with leather ties and metal rings partway down."""
from anime import ring_shell
from kit_rugged import dread
from paint import scalp

META = {"name": "Dreadlocks", "gender": "unisex",
        "description": "Thick rope-like locks to the shoulders all round, swept back off the face, a few bound with ties."}

# (x, y, z, rotation, length, tie)
LOCKS = [(-4.3, -6.8, -2.0, (14, 0, 18), 8, None), (4.3, -6.8, -2.0, (14, 0, -18), 8, "L2"),
         (-4.4, -6.6, .4, (18, 0, 16), 10, "M3"), (4.4, -6.6, .4, (18, 0, -16), 10, None),
         (-4.2, -6.6, 2.8, (24, 0, 12), 10, None), (4.2, -6.6, 2.8, (24, 0, -12), 10, "L2"),
         (-2.6, -7.2, 4.4, (20, 0, 6), 12, "L2"), (-.9, -7.4, 4.6, (16, 0, 2), 12, None),
         (.9, -7.4, 4.6, (16, 0, -2), 12, "M3"), (2.6, -7.2, 4.4, (20, 0, -6), 12, None),
         (-1.6, -5.0, 4.6, (8, 0, 4), 8, None), (1.6, -5.0, 4.6, (8, 0, -4), 8, None)]
# Locks swept back over the top of the head from the hairline.
CROWN = [(-2.4, -8.6, -2.6, (88, 0, 4), 8), (0, -8.8, -2.8, (90, 0, 0), 10), (2.4, -8.6, -2.6, (88, 0, -4), 8),
         (-1.2, -8.8, 0, (80, 0, 2), 8), (1.2, -8.8, 0, (80, 0, -2), 8)]


def build(g):
    scalp(g, 35640, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 35641, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, y, z, rot, n, tie) in enumerate(LOCKS):
        dread(g, f"dread_{i}", (x, y, z), rot, n, 2, 35642 + i, tie=tie, tie_at=1 if tie else None)
    for i, (x, y, z, rot, n) in enumerate(CROWN):
        dread(g, f"crown_dread_{i}", (x, y, z), rot, n, 2, 35654 + i, motion="none")
