"""Worker's Topknot: all the hair drawn up off the neck and the brow into a tight bun on the crown,
bound with a strip of cloth, the way the cooks and smiths keep it out of the work."""
from anime import cel_box, ring_shell, tie
from paint import scalp

META = {"name": "Worker's Topknot", "gender": "unisex",
        "description": "Hair drawn up off the neck and brow into a tight crown bun bound with cloth."}


def build(g):
    scalp(g, 36961, side_rows=5, back_rows=7, sideburn=1)
    ring_shell(g, 36962, side_rows=4, back_rows=6, ring_row=1)
    bun = g.piece("bun", "HEAD", (-2, -2, -2), (4, 3, 4), pivot=(0, -8.1, 1.4), rotation=(-12, 0, 0))
    cel_box(bun, 36963, ring=0, clump=2)
    knob = g.piece("bun_top", "HEAD", (-1.5, -1, -1.5), (3, 1, 3), pivot=(0, -10.3, 1.2), rotation=(-12, 0, 0))
    cel_box(knob, 36964, top_delta=1)
    tie(g, "bun_wrap", (0, -8.1, 1.4), (-12, 0, 0), (5, 1, 5), y=.2, key="S3")
