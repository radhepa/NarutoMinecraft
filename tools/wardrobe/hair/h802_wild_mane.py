"""Wild Mane: a huge untamed mane like the clan head's, thick spikes bursting off the crown, the
length tumbling past the shoulders in jagged hanks that flare outward, and long rough bangs at
the sides of the face."""
from anime import back_fan, bangs, lock, ring_shell, sidelocks
from kit_inuzuka import burst
from paint import scalp

META = {"name": "Wild Mane", "gender": "unisex",
        "description": "A huge untamed mane: thick crown spikes, jagged hanks past the shoulders flaring out."}

BIG = ((4, 3), (3, 2), (2, 2), (1, 1))
MID = ((3, 3), (2, 2), (1, 1))
CROWN = [(-2.4, -2.4, MID, 18, -30), (0, -2.8, BIG, 20, 0), (2.4, -2.4, MID, 18, 30), (-3.2, .4, BIG, -14, -52),
         (3.2, .4, BIG, -14, 52), (-1.4, 1.4, BIG, -30, -16), (1.4, 1.4, BIG, -30, 16), (0, 3.0, BIG, -58, 0)]
# Hanks down the back: (x, segments, splay, lean back)
HANKS = [(-3.4, ((3, 4), (3, 3), (2, 3), (1, 2)), 30, 20), (-1.8, ((3, 5), (2, 4), (2, 3), (1, 2)), 14, 16),
         (0, ((3, 5), (3, 4), (2, 3), (1, 2)), 0, 14), (1.8, ((3, 5), (2, 4), (2, 3), (1, 2)), -14, 16),
         (3.4, ((3, 4), (3, 3), (2, 3), (1, 2)), -30, 20)]


def build(g):
    scalp(g, 8031, side_rows=7, back_rows=8, sideburn=1)
    ring_shell(g, 8032, side_rows=7, back_rows=8, ring_row=1)
    burst(g, "crown_spike", CROWN, 8033, depth=3)
    back_fan(g, "mane", HANKS, seed=8039, motion="sway")
    bangs(g, "fringe", [(-2.6, ((3, 2), (2, 1), (1, 1)), 24), (-.4, ((2, 2), (1, 1)), 6), (1.8, ((3, 2), (1, 1)), -20)],
          seed=8046)
    sidelocks(g, "bang", 9, seed=8049, x=4.4, z=-3.4, flare=8, width=2)
    sidelocks(g, "sidelock", 8, seed=8052, x=4.5, z=-.4, flare=26, width=3)
    for i, (x, rz) in enumerate(((-4.4, 40), (4.4, -40))):
        lock(g, f"flare_{i}", (x, -5.0, 2.2), (14, 0, rz), ((2, 3), (1, 2)), 2, 8055 + i)
