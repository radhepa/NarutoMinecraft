"""Swept Dusk: hair swept straight back off the face in low, flat spikes, as if combed by a night
wind, the points lifting a little over the crown and fanning out at the nape."""
from anime import back_fan, ring_shell, sidelocks, spike
from paint import scalp

META = {"name": "Swept Dusk", "gender": "unisex",
        "description": "Hair swept straight back in low flat spikes, lifting over the crown, fanned at the nape."}

LONG = ((3, 3), (2, 2), (1, 2))


def build(g):
    scalp(g, 25120, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 25121, side_rows=5, back_rows=8, ring_row=1)
    for i, (x, z, rx, rz) in enumerate(((-2.6, -2.6, -62, -6), (0, -2.8, -58, 0), (2.6, -2.6, -62, 6),
                                        (-1.4, .2, -68, -4), (1.4, .2, -68, 4))):
        spike(g, f"sweep_{i}", (x, -7.8, z), (rx, 0, rz), LONG, 2, 25122 + i)
    sidelocks(g, "temple", 4, seed=25128, x=4.4, z=-2.0, flare=-6, width=1)
    back_fan(g, "nape", [(-2.8, ((3, 3), (2, 1), (1, 1)), 20, 30), (0, ((3, 3), (2, 2), (1, 1)), 0, 26),
                         (2.8, ((3, 3), (2, 1), (1, 1)), -20, 30)], seed=25131)
