"""Elder Mane: the clan elders' long hair worn loose and swept straight back from a high forehead,
falling past the shoulders, gathered once low on the back with a white cord, with long sweeping
locks at the temples."""
from anime import curtain, lock, ring_shell, tie
from paint import scalp

META = {"name": "Elder Mane", "gender": "unisex",
        "description": "Long hair swept straight back from the forehead, tied once low on the back, long temple locks."}


def build(g):
    scalp(g, 24411, side_rows=6, back_rows=8, sideburn=2)
    ring_shell(g, 24412, side_rows=5, back_rows=8, ring_row=1)
    for i, x in enumerate((-2.4, 0, 2.4)):
        lock(g, f"sweep_{i}", (x, -8.3, -3.8), (86, 0, 0), ((3, 3), (3, 3), (2, 2)), 1, 24415 + i * 5, ring=0)
    curtain(g, "mane", (0, -7.4, 4.6), (8, 0, 0), 8, 9, hem=((1, 2, 2), (3, 2, 3), (5, 2, 2)), seed=24430)
    tie(g, "cord", (0, -7.4, 4.6), (8, 0, 0), (5, 1, 2), y=5.5, key="S4", motion="sway")
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"temple_{side}", (4.4 * sign, -7.4, -2.4), (0, 0, -4 * sign), ((2, 5), (1, 3)), 1, 24440 + (sign > 0))
