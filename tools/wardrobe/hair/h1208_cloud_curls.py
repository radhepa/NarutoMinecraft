"""Cloud Curls: short, soft curls piled up like the clouds in a Kurama scroll painting, fuller on the
crown and over the ears, tapering at the nape, with a few curls tumbling onto the brow."""
from paint import curls_box, scalp

META = {"name": "Cloud Curls", "gender": "unisex",
        "description": "Short soft curls piled like painted clouds, full crown, curls on the brow."}


def build(g):
    scalp(g, 12280, side_rows=5, back_rows=7, sideburn=2)
    hat = g.part("hat")
    curls_box(hat, 12281)
    for face in (hat.front, hat.right, hat.left, hat.back):
        for y in range(face.h):
            for x in range(face.w):
                keep = {"front": y < 1, "right": y < 5 - (x < 2), "left": y < 5 - (x > 5), "back": y < 7}[face.name]
                if not keep:
                    face.clear(x, y)
    hat.bottom.fill(None)
    crown = g.piece("crown", "HEAD", (-4, 0, -4), (8, 2, 8), pivot=(0, -9.6, .2))
    curls_box(crown, 12284)
    for i, (x, z, w) in enumerate(((-2.6, -1.6, 3), (.6, -2.2, 4), (2.8, 1.6, 3), (-1.2, 2.4, 3))):
        puff = g.piece(f"puff_{i}", "HEAD", (-w / 2, -1, -w / 2), (w, 2, w), pivot=(x, -10.2, z))
        curls_box(puff, 12288 + i)
    for side, sign in (("right", -1), ("left", 1)):
        ear = g.piece(f"ear_{side}", "HEAD", (-1, 0, -3), (2, 4, 6), pivot=(4.4 * sign, -7.8, .6))
        curls_box(ear, 12294 + (sign > 0))
    back = g.piece("nape", "HEAD", (-4, 0, -1), (8, 6, 2), pivot=(0, -7.8, 4.3))
    curls_box(back, 12297)
    for i, x in enumerate((-2.4, -.4, 1.8)):
        curl = g.piece(f"brow_curl_{i}", "HEAD", (-1, 0, -1), (2, 2, 1), pivot=(x, -8.6, -4.4))
        curls_box(curl, 12300 + i)
