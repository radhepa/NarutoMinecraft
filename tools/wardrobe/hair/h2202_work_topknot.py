"""Work Topknot: everything swept up off the neck and the brow into a short stubby knot on the crown,
bound with a cedar cord, the ends fanned out above it like a brush, and short sideburns."""
from anime import cel_box, ring_shell, spike, tie
from paint import k, scalp

META = {"name": "Work Topknot", "gender": "unisex",
        "description": "Hair swept up into a stubby crown knot bound in cedar cord, the ends fanned like a brush."}


def build(g):
    scalp(g, 22021, side_rows=4, back_rows=8, sideburn=2)
    hat = ring_shell(g, 22022, side_rows=4, back_rows=8, ring_row=1)
    for x in (1, 3, 5, 6):
        hat.top.vline(x, 0, 7, k("H", 3 if x % 2 else 1))
    root = g.piece("knot_root", "HEAD", (-1.5, -2, -1.5), (3, 2, 3), pivot=(0, -8, .4))
    cel_box(root, 22023, top_delta=1)
    tie(g, "knot_cord", (0, -9.6, .4), size=(3, 1, 3), key="A2")
    for i, (rx, rz) in enumerate(((-12, -34), (-6, 0), (-12, 34), (16, -14), (16, 14))):
        spike(g, f"brush_{i}", (0, -10.4, .4), (rx, 0, rz), ((2, 2), (1, 1)), 2, 22026 + i)
