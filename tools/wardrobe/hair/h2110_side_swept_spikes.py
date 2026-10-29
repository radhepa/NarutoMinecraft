"""Side-Swept Spikes: every spike leaning hard to one side as if the head had been out in a
gale, a long fringe point swept to the same side and a short spiky nape."""
from anime import bangs, lock, ring_shell
from kit_hagane import crown
from paint import scalp

META = {"name": "Side-Swept Spikes", "gender": "unisex",
        "description": "Spikes all leaning hard to one side, a fringe point swept the same way, a spiky nape."}

LONG = ((3, 3), (2, 2), (1, 2))
MID = ((3, 2), (2, 2), (1, 1))
SPIKES = [(-2.4, -2.6, MID, -6, 34), (0, -2.8, LONG, -10, 37), (2.4, -2.4, LONG, -6, 42),
          (-2.2, 0, LONG, -24, 33), (.6, .2, LONG, -26, 38), (2.8, .4, MID, -24, 46), (-1.0, 2.6, MID, -52, 29),
          (1.8, 2.6, MID, -52, 40)]


def build(g):
    scalp(g, 21530, side_rows=4, back_rows=7, sideburn=2)
    ring_shell(g, 21531, side_rows=4, back_rows=6, ring_row=1)
    crown(g, "spike", SPIKES, 21532)
    bangs(g, "fringe", [(-2.8, ((2, 2), (1, 1)), 34), (-.8, ((2, 1), (1, 1)), 30), (1.4, ((2, 2), (1, 1)), 40)],
          seed=21570)
    for i, (x, rz) in enumerate(((-2.0, 20), (1.0, -10))):
        lock(g, f"nape_{i}", (x, -3.2, 4.3), (46, 0, rz), ((2, 2), (1, 1)), 1, 21580 + i * 5)
