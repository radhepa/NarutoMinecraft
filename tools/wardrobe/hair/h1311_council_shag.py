"""Council Shag: Danzo in his prime as Root's founder: dark hair worn shaggy and full, a ragged
fringe parted off-centre to the brows, locks over the ears and a longer nape of points to the collar."""
from anime import back_fan, bangs, ring_shell, sidelocks
from paint import scalp

META = {"name": "Council Shag", "gender": "unisex",
        "description": "Full shaggy hair, an off-centre ragged fringe, locks over the ears, a pointed nape to the collar."}


def build(g):
    scalp(g, 13330, side_rows=6, back_rows=8, sideburn=3)
    ring_shell(g, 13331, side_rows=6, back_rows=8, ring_row=1)
    bangs(g, "fringe", [(-3.3, ((2, 3), (1, 1)), 6), (-.9, ((3, 2), (1, 1)), 22), (1.4, ((2, 2), (1, 1)), -10),
                        (3.3, ((2, 3), (1, 1)), -6)], seed=13331)
    sidelocks(g, "ear", 6, seed=13332, x=4.45, z=-1.6, flare=7, width=2)
    sidelocks(g, "frame", 6, seed=13333, x=4.3, z=-3.5, flare=4, width=1)
    back_fan(g, "nape", [(-3.0, ((3, 4), (2, 1), (1, 1)), 12, 4), (-1.0, ((2, 5), (1, 1)), 4, 3),
                         (1.0, ((3, 5), (2, 1), (1, 1)), -4, 3), (3.0, ((2, 4), (1, 1)), -12, 4)], seed=13333, z=4.3)
