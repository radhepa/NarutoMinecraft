"""Close Buzz: hair clipped short all over for the heat of the roof beams, a little longer and
spiky along the top in a short brush, the hairline crisp and the nape clean."""
from anime import ring_shell, spike
from paint import scalp

META = {"name": "Close Buzz", "gender": "unisex",
        "description": "Clipped short all over, a short spiky brush along the top, crisp hairline."}


def build(g):
    scalp(g, 22121, side_rows=3, back_rows=5, sideburn=1)
    ring_shell(g, 22122, side_rows=2, back_rows=4, ring_row=1)
    for i, (x, z) in enumerate(((-1.2, -2.6), (1.2, -2.6), (-1.2, -.2), (1.2, -.2), (0, 2.2))):
        spike(g, f"brush_{i}", (x, -7.8, z), (-6, 0, x * -8), ((2, 1), (1, 1)), 2, 22124 + i)
