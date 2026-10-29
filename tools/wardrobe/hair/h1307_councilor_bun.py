"""Councilor Bun: severe and tidy, parted in the centre and drawn back flat over the ears into a
low round bun at the nape, pinned with a single dark rod; two short locks are left at the temples."""
from anime import cel_box, ring_shell, sidelocks
from paint import scalp, solid

META = {"name": "Councilor Bun", "gender": "unisex",
        "description": "Centre parted, drawn flat into a low round bun at the nape, a dark hair rod, short temple locks."}


def build(g):
    scalp(g, 13198, side_rows=6, back_rows=8, sideburn=2, part=3)
    ring_shell(g, 13199, side_rows=6, back_rows=8, ring_row=1)
    bun = g.piece("bun", "HEAD", (-2, -2, 0), (4, 4, 3), pivot=(0, -2.6, 4.2))
    cel_box(bun, 13199, ring=1, clump=2)
    rod = g.piece("hair_rod", "HEAD", (-3.5, -.5, -.5), (7, 1, 1), pivot=(0, -3.2, 5.7), rotation=(0, 0, 18))
    solid(rod, "K", "smooth", 13200, 2, edge=False)
    rod.right.fill("A2"), rod.left.fill("A2")
    sidelocks(g, "temple", 5, seed=13204, x=4.3, z=-3.4, flare=2, width=1)
