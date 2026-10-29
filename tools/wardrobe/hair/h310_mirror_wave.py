"""Mirror Wave: Kagami's soft wavy hair, swept over to one side in loose waves that curl down past
the ears to the nape, the parting high on the left."""
from anime import bangs, lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "Mirror Wave", "gender": "unisex", "description": "Loose waves swept to one side, curling past the ears to the nape."}

# Waved locks: each is two pieces bending opposite ways. (x, y, z, rx, rz)
WAVES = [(-4.5, -7.4, -1.2, 0, 12), (-4.5, -7.4, 1.6, 6, 16), (4.5, -7.4, 1.6, 6, -14),
         (-2.6, -7.0, 4.4, 18, 14), (0, -7.2, 4.5, 16, 2), (2.6, -7.0, 4.4, 18, -12)]


def build(g):
    scalp(g, 3441, side_rows=6, back_rows=8, sideburn=2, part=5)
    ring_shell(g, 3442, side_rows=6, back_rows=8, ring_row=1)
    for i, (x, y, z, rx, rz) in enumerate(WAVES):
        lock(g, f"wave_{i}", (x, y, z), (rx, 0, rz), ((3, 4),), 2, 3450 + i * 5, motion="sway")
        lock(g, f"wave_{i}_curl", (x, y, z), (rx, 0, -rz * 1.4), ((2, 2), (1, 2)), 2, 3452 + i * 5, y0=4,
             ring=None, motion="sway")
    bangs(g, "fringe", [(-3.0, ((3, 2), (2, 1)), 42), (-.8, ((3, 2), (2, 1)), 46), (1.4, ((3, 2), (1, 1)), 40),
                        (3.1, ((2, 2), (1, 1)), 8)], seed=3485)
    sidelocks(g, "frame", 8, seed=3490, x=4.35, z=-3.4, flare=5, width=2)
