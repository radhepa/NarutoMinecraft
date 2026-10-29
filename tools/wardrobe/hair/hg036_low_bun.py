"""Low Bun: hair parted in the middle and combed smoothly back over the ears into a round bun low at
the nape, a couple of short loose strands at the temples: the senior medic's working hair."""
from anime import lock, ring_shell
from kit_kurama import bun, part_line
from paint import scalp

META = {"name": "Low Bun", "gender": "unisex",
        "description": "Middle-parted hair combed back over the ears into a round bun at the nape."}


def build(g):
    scalp(g, 34880, side_rows=6, back_rows=8, sideburn=3, part=3)
    ring_shell(g, 34881, side_rows=5, back_rows=7, ring_row=1)
    part_line(g, 3)
    bun(g, "nape_bun", (0, -3.0, 5.3), size=4, seed=34882)
    for side, sign in (("right", -1), ("left", 1)):
        lock(g, f"temple_{side}", (4.3 * sign, -7.0, -3.3), (0, 0, -3 * sign), ((1, 3), (1, 1)), 1, 34885 + (sign > 0))
