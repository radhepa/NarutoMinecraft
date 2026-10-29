"""Close Crop: hair cut to a soldier's short nap all over, only a faint ridge at the crown, nothing
for a bandana or a blade to catch."""
from paint import k, scalp, shell

META = {"name": "Close Crop", "gender": "unisex",
        "description": "Hair cut to a short soldier's nap all over, a faint ridge at the crown."}


def build(g):
    scalp(g, 20351, side_rows=3, back_rows=6, sideburn=2)
    shell(g, 20352, side_rows=2, back_rows=4, sheen=None)
    hat = g.part("hat")
    hat.top.vline(3, 0, 7, k("H", 4)), hat.top.vline(4, 0, 7, k("H", 3))
    ridge = g.piece("ridge", "HEAD", (-1, 0, -3), (2, 1, 6), pivot=(0, -8.8, .5))
    from anime import cel_box
    cel_box(ridge, 20353, base=2, top_delta=1)
