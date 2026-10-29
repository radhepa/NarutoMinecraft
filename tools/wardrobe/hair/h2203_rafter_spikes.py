"""Rafter Spikes: short stiff spikes combed straight back from the brow in neat rows like rafters on
a roof frame, a few lifting at the crown, the sides cut short and the hairline left bare."""
from anime import ring_shell, spike
from paint import k, scalp

META = {"name": "Rafter Spikes", "gender": "unisex",
        "description": "Stiff spikes combed straight back in neat rows like rafters, short sides, bare brow."}


def build(g):
    scalp(g, 22041, side_rows=4, back_rows=7, sideburn=3)
    hat = ring_shell(g, 22042, side_rows=4, back_rows=6, ring_row=1)
    for x in (0, 2, 5, 7):
        hat.top.vline(x, 0, 7, k("H", 1))
    for row, (z, rx, segs) in enumerate(((-3.0, -62, ((2, 2), (1, 2))), (-.6, -58, ((2, 3), (1, 2))),
                                         (1.8, -46, ((2, 3), (1, 2))))):
        for i, x in enumerate((-2.4, 0, 2.4)):
            spike(g, f"rafter_{row}_{i}", (x, -7.8, z), (rx, 0, (x * -3)), segs, 2, 22044 + row * 3 + i)
    for i, x in enumerate((-2.2, 0, 2.2)):
        spike(g, f"nape_{i}", (x, -5.6, 4.1), (-110, 0, x * -6), ((2, 2), (1, 1)), 1, 22054 + i)
