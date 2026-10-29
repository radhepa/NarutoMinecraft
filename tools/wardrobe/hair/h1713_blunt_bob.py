"""Blunt Bob: straight dark hair cut in one hard line at the jaw, a heavy blunt fringe at the brow
and the sides falling straight past the cheeks."""
from anime import lock, ring_shell
from paint import scalp

META = {"name": "Blunt Bob", "gender": "unisex",
        "description": "Straight hair cut in one hard line at the jaw, blunt brow fringe, straight sides."}


def build(g):
    scalp(g, 17141, side_rows=8, back_rows=8, sideburn=0)
    hat = ring_shell(g, 17142, side_rows=8, back_rows=8, ring_row=1)
    hat.front.hline(0, 7, 1, "H2"), hat.front.hline(0, 7, 2, "H1")
    for side, x in (("right", -4.3), ("left", 4.3)):
        lock(g, f"side_{side}", (x, -6.0, -2.6), (0, 0, 0), ((1, 6),), 3, 17143 + (x > 0), ring=None)
    hem = g.piece("nape_hem", "HEAD", (-4, 0, 0), (8, 2, 1), pivot=(0, -.6, 4.3))
    from anime import cel_box
    cel_box(hem, 17146, top_delta=0)
