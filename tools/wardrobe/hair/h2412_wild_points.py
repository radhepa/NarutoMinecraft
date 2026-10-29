"""Wild Points: short hair that dries into stiff points from a day over the steaming pots, swept up
and back from the forehead, the sides cut short and a single lock left down at the centre of the
brow."""
from anime import lock, ring_shell, spike
from paint import scalp

META = {"name": "Wild Points", "gender": "unisex",
        "description": "Short stiff points swept up and back from the forehead, short sides, one centre lock."}

TUFT = ((3, 2), (2, 2), (1, 1))


def build(g):
    scalp(g, 24301, side_rows=3, back_rows=6, sideburn=2)
    ring_shell(g, 24302, side_rows=3, back_rows=6, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.4, -2.6, -40, 20), (0, -2.8, -44, 0), (2.4, -2.6, -40, -20),
                                        (-1.4, .6, -64, 10), (1.4, .6, -64, -10))):
        spike(g, f"point_{i}", (x, -7.9, z), (rx, 0, rz), TUFT, 3, 24305 + i * 5)
    lock(g, "centre", (.4, -8.55, -4.35), (-10, 0, 10), ((2, 2), (1, 1)), 1, 24345, ring=0)
