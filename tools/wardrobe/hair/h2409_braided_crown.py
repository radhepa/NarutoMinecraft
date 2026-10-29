"""Braided Crown: long hair braided and wound once round the head like a wreath, pinned above the
nape, a neat centre-parted fringe and a bell sprig tucked into the braid over the left ear."""
from anime import bangs, cel_box, ring_shell
from kit_suzuran import bell_charm
from paint import k, scalp

META = {"name": "Braided Crown", "gender": "unisex",
        "description": "A braid wound round the head like a wreath, centre-parted fringe, a bell sprig in the braid."}


def build(g):
    scalp(g, 24241, side_rows=5, back_rows=7, sideburn=1, part=3)
    ring_shell(g, 24242, side_rows=4, back_rows=7, ring_row=1)
    # The wreath: braided segments round the sides and back of the head above the ears, each crossed by diagonals.
    for name, origin, size in (("back", (-4.5, -7.2, 3.6), (9, 1, 1)), ("right", (-5.0, -7.2, -4.0), (1, 1, 8)),
                               ("left", (4.0, -7.2, -4.0), (1, 1, 8))):
        seg = g.piece(f"braid_{name}", "HEAD", origin, size, inflate=.35)
        cel_box(seg, 24245 + len(name), top_delta=1, clump=2)
        for f in seg.sides:
            for x in range(0, f.w, 2):
                f.set(x, 0, k("H", 1))
    bun = g.piece("braid_knot", "HEAD", (-1.5, -1.5, -1), (3, 3, 2), pivot=(0, -5.4, 4.8))
    cel_box(bun, 24250, top_delta=1, clump=2)
    bangs(g, "fringe", [(-2.7, ((2, 2), (1, 1)), 26), (-1.0, ((2, 2), (1, 1)), 32), (1.0, ((2, 2), (1, 1)), -32),
                        (2.7, ((2, 2), (1, 1)), -26)], seed=24255)
    bell_charm(g, "sprig", (5.3, -7.8, -.8), rotation=(0, -90, 24))
