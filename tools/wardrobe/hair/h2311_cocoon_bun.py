"""Cocoon Bun: hair wound into a tall oval bun at the back of the head, wrapped round and round with
pale thread like a silk cocoon, short wisps loose at the temples."""
from anime import cel_box, ring_shell, sidelocks
from paint import scalp

META = {"name": "Cocoon Bun", "gender": "unisex",
        "description": "A tall oval bun at the back of the head wound with pale thread like a cocoon."}

PIVOT, TILT = (0, -5.6, 4.3), (-10, 0, 0)


def build(g):
    scalp(g, 23221, side_rows=5, back_rows=8, sideburn=2)
    hat = ring_shell(g, 23222, side_rows=4, back_rows=8, ring_row=1)
    for x in (1, 3, 4, 6):
        hat.back.vline(x, 0, 7, "H1")
    bun = g.piece("bun_cocoon", "HEAD", (-2, -3, 0), (4, 6, 3), pivot=PIVOT, rotation=TILT)
    cel_box(bun, 23225, ring=None)
    for f in bun.sides:   # pale thread wound round and round the cocoon
        for y in (1, 3, 4):
            f.hline(0, f.w - 1, y, "S3" if y != 4 else "S2")
    for i, (w, y) in enumerate(((2, -4), (2, 3))):
        cap = g.piece(f"bun_tip_{i}", "HEAD", (-w / 2, y, .5), (w, 1, 2), pivot=PIVOT, rotation=TILT)
        cel_box(cap, 23228 + i, top_delta=1)
    sidelocks(g, "wisp", 5, seed=23230, x=4.3, z=-3.4, flare=4, width=1)
