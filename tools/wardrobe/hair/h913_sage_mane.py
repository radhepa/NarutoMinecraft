"""Sage Mane: an invention after the Monkey King Enma's white mane. Shaggy hair to the shoulders,
layered in pointed locks round the back and sides, a heavy fringe and thick sideburns."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Sage Mane", "gender": "unisex",
        "description": "Shaggy shoulder-length mane in layered pointed locks, heavy fringe, thick sides."}


def build(g):
    scalp(g, 9711, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 9712, side_rows=8, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-2.8, ((2, 3), (1, 1)), 18), (-1.0, ((2, 2), (1, 1)), 8), (1.0, ((2, 2), (1, 1)), -8),
                        (2.8, ((2, 3), (1, 1)), -18)], seed=9720)
    sidelocks(g, "frame", 9, seed=9730, x=4.4, z=-3.2, flare=8, width=2)
    sidelocks(g, "frame_back", 10, seed=9735, x=4.5, z=0.0, flare=14, width=3)
    back_fan(g, "back", [(-3.0, ((3, 6), (2, 2), (1, 1)), 18, 14), (-1.0, ((3, 7), (2, 2), (1, 1)), 6, 16),
                         (1.0, ((3, 7), (2, 2), (1, 1)), -6, 16), (3.0, ((3, 6), (2, 2), (1, 1)), -18, 14)],
             seed=9740, motion="sway")
    for i, (x, rz) in enumerate(((-2.0, -20), (0.0, 0), (2.0, 20))):
        spike(g, f"crown_{i}", (x, -8.0, 0.0), (-30, 0, rz), ((3, 2), (2, 1), (1, 1)), 2, 9760 + i * 3)
