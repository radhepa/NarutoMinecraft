"""Cherry Long: Sakura's Part I hair, straight cherry-pink to the waist and parted in the centre so
the broad forehead shows, two short brow locks at the temples and long front locks falling past the
cheeks to the chest."""
from anime import curtain, lock, ring_shell, sidelocks
from paint import scalp

META = {"name": "Cherry Long", "gender": "unisex",
        "description": "Straight waist-length hair, centre part, open forehead, long front locks to the chest."}


def build(g):
    scalp(g, 19001, side_rows=7, back_rows=8, sideburn=1, part=3)
    ring_shell(g, 19002, side_rows=7, back_rows=8, ring_row=1)
    for i, (x, rz) in enumerate(((-2.9, 34), (2.9, -34))):
        lock(g, f"brow_{i}", (x, -8.55, -4.35), (-10, 0, rz), ((2, 2), (1, 1)), 1, 19005 + i * 7, ring=0)
    sidelocks(g, "front", 11, seed=19010, x=4.35, flare=3, width=2)
    curtain(g, "back", (0, -7.4, 4.45), (6, 0, 0), 8, 13, hem=((0, 2, 2), (2, 2, 3), (4, 2, 3), (6, 2, 2)), seed=19015)
