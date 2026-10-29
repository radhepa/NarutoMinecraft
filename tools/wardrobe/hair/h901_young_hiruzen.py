"""Young Hiruzen: the Third Hokage as a young man under Tobirama, short dark hair standing up in
blunt spikes over the crown and swept back, a few short points at the brow and trimmed sideburns."""
from anime import bangs, ring_shell, spike
from paint import scalp

META = {"name": "Young Hiruzen", "gender": "unisex",
        "description": "Short spikes standing up over the crown and swept back, short brow points."}

# (x, y, z, segments, rx, rz)
CROWN = [(-2.4, -7.9, -1.4, ((3, 2), (2, 2), (1, 1)), -14, -22),
         (0.0, -8.0, -1.8, ((3, 3), (2, 2), (1, 1)), -10, 0),
         (2.4, -7.9, -1.4, ((3, 2), (2, 2), (1, 1)), -14, 22),
         (-1.4, -8.0, 1.0, ((3, 3), (2, 2), (1, 1)), -38, -12),
         (1.4, -8.0, 1.0, ((3, 3), (2, 2), (1, 1)), -38, 12),
         (-2.8, -7.0, 3.0, ((3, 2), (2, 2), (1, 1)), -70, -30),
         (0.0, -7.2, 3.2, ((3, 3), (2, 2), (1, 1)), -66, 0),
         (2.8, -7.0, 3.0, ((3, 2), (2, 2), (1, 1)), -70, 30)]


def build(g):
    scalp(g, 9011, side_rows=4, back_rows=6, sideburn=3)
    ring_shell(g, 9012, side_rows=4, back_rows=6, ring_row=1)
    for i, (x, y, z, segs, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_{i}", (x, y, z), (rx, 0, rz), segs, 2, 9020 + i * 3)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 20), (-.6, ((2, 1), (1, 1)), 6), (1.6, ((2, 2), (1, 1)), -16),
                        (3.0, ((1, 2),), -22)], seed=9050)
