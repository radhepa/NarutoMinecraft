"""Spiked Tail: a stiff crown of back-swept spikes over hair gathered into a short tail high at
the back, its end splaying into spikes like a broom; a rust tie holds it."""
from anime import bangs, lock, ring_shell, sidelocks, tie
from kit_hagane import crown
from paint import scalp

META = {"name": "Spiked Tail", "gender": "unisex",
        "description": "Back-swept crown spikes and a short high tail splaying into spikes, a rust tie."}

MID = ((3, 2), (2, 2), (1, 1))
SPIKES = [(-2.4, -2.8, MID, -20, -28), (0, -3.0, MID, -26, 0), (2.4, -2.8, MID, -20, 28),
          (-1.4, -.4, MID, -46, -12), (1.4, -.4, MID, -46, 12)]


def build(g):
    scalp(g, 21300, side_rows=5, back_rows=8, sideburn=2)
    ring_shell(g, 21301, side_rows=5, back_rows=7, ring_row=1)
    crown(g, "spike", SPIKES, 21302)
    pivot = (0, -5.4, 4.2)
    tie(g, "tie", pivot, (104, 0, 0), size=(3, 1, 3), key="A2")
    for i, (rz, rx) in enumerate(((-16, 108), (0, 118), (16, 108))):
        lock(g, f"tail_{i}", pivot, (rx, 0, rz), ((2, 3), (1, 2)), 2, 21320 + i * 3, ring=None, y0=1)
    bangs(g, "fringe", [(-2.6, ((2, 2), (1, 1)), 20), (-.6, ((2, 1), (1, 1)), 6), (1.6, ((2, 2), (1, 1)), -16)],
          seed=21340)
    sidelocks(g, "frame", 5, seed=21350, x=4.3, z=-3.0, flare=10, width=2)
