"""Rain Mane: long, unkempt red hair to the shoulder blades in ragged, separate locks, a parted
fringe of long points to the brows and locks spilling over the front of the shoulders."""
from anime import back_fan, bangs, ring_shell, sidelocks
from anime import lock
from paint import scalp

META = {"name": "Rain Mane", "gender": "unisex",
        "description": "Ragged locks to the shoulder blades, a long pointed parted fringe, shoulder locks."}

FAN = [(-3.4, ((2, 6), (2, 3), (1, 2)), 10, 4), (-1.7, ((2, 7), (2, 4), (1, 2)), 4, 2), (0, ((2, 8), (2, 3), (1, 2)), 0, 3),
       (1.7, ((2, 7), (2, 3), (1, 2)), -4, 2), (3.4, ((2, 6), (2, 4), (1, 2)), -10, 4)]


def build(g):
    scalp(g, 2140, side_rows=8, back_rows=8, sideburn=0)
    ring_shell(g, 2141, side_rows=7, back_rows=8, ring_row=1)
    back_fan(g, "mane", FAN, seed=2142, motion="sway")
    for side, sign in (("right", -1), ("left", 1)):
        for i, (z, n, rz) in enumerate(((-1.8, 9, 8), (.6, 10, 12), (2.8, 8, 16))):
            lock(g, f"side_{side}_{i}", (4.4 * sign, -7.4, z), (0, 0, -rz * sign), ((2, n - 3), (1, 3)), 1,
                 2143 + i * 3 + (sign > 0), ring=1)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 10), (-1.1, ((2, 2), (1, 1)), 22), (1.1, ((2, 2), (1, 1)), -22),
                        (2.8, ((2, 2), (1, 1)), -10)], seed=2152)
    sidelocks(g, "frame", 13, seed=2153, x=4.3, z=-3.4, flare=5, width=2)
