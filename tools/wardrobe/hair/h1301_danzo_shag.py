"""Danzo Shag: Danzo Shimura as an elder of the council: short, dark, shaggy hair that falls in
ragged points to the brows and over the ears, cut short and uneven at the nape."""
from anime import back_fan, bangs, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Danzo Shag", "gender": "unisex",
        "description": "Short shaggy dark hair, ragged points to the brows and over the ears, an uneven nape."}

TUFT = ((3, 1), (2, 1))
CROWN = [(-2.2, -1.6, -44, -44), (.4, -2.2, -50, 6), (2.6, -1.2, -44, 44), (0, 1.8, 50, 0)]


def build(g):
    scalp(g, 13000, side_rows=5, back_rows=7, sideburn=2)
    ring_shell(g, 13001, side_rows=5, back_rows=7, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(CROWN):
        spike(g, f"crown_tuft_{i}", (x, -7.9, z), (rx, 0, rz), TUFT, 2, 13006 + i)
    bangs(g, "fringe", [(-3.0, ((2, 3), (1, 1)), 10), (-1.4, ((2, 2), (1, 1)), 16), (.2, ((2, 2), (1, 1)), -8),
                        (1.8, ((2, 2), (1, 1)), -20), (3.1, ((2, 3), (1, 1)), -12)], seed=13012)
    sidelocks(g, "ear", 5, seed=13018, x=4.4, z=-2.0, flare=6, width=2)
    back_fan(g, "nape", [(-2.8, ((3, 2), (2, 1), (1, 1)), 14, 10), (0, ((3, 3), (2, 1), (1, 1)), 0, 8),
                         (2.8, ((3, 2), (2, 1), (1, 1)), -14, 10)], seed=13024, z=4.25)
