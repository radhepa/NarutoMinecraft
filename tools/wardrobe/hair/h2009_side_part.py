"""Side Part: a neat short cut parted on the left, the long side swept across the brow and over in
one smooth wave, tidy above the ears and at the nape."""
from anime import ring_shell
from kit_namiashi import wave_lock
from paint import scalp

META = {"name": "Side Part", "gender": "unisex",
        "description": "Neat short cut parted on the left, the long side swept across the brow in one smooth wave."}


def build(g):
    scalp(g, 20231, side_rows=5, back_rows=7, sideburn=2, part=5)
    hat = ring_shell(g, 20232, side_rows=5, back_rows=7, ring_row=1)
    hat.top.vline(5, 0, 7, "H0")
    sweep = g.piece("sweep", "HEAD", (-.5, -1, 0), (6, 2, 4), pivot=(-2.2, -8.1, -4.4), rotation=(0, 0, -6))
    from anime import cel_box
    cel_box(sweep, 20233, ring=0)
    wave_lock(g, "wave", (-3.6, -8.6, -4.35), (-10, 0, 20), [(((2, 2),), 0, 0), (((1, 2),), 0, 40)], seed=20235)
    wave_lock(g, "tip", (1.9, -8.6, -4.35), (-10, 0, -28), [(((1, 2),), 0, 0)], seed=20240)
