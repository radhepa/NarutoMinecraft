"""Gatepost Spikes: the clan's signature dark hair, after the gate guard who keeps the Leaf's front
door: stiff spikes rising off the hairline and sweeping up and back over the crown like a breaking
wave, a short pointed fringe and a bristling nape."""
from anime import bangs, lock, ring_shell
from kit_hagane import crown
from paint import scalp

META = {"name": "Gatepost Spikes", "gender": "unisex",
        "description": "Stiff spikes sweeping up and back from the hairline, a short pointed fringe, a bristling nape."}

TALL = ((3, 3), (2, 2), (1, 2))
MID = ((3, 2), (2, 2), (1, 1))
SPIKES = [(-2.6, -3.0, MID, -18, -30), (0, -3.4, TALL, -26, 0), (2.6, -3.0, MID, -18, 30),
          (-1.4, -1.0, TALL, -40, -14), (1.4, -1.0, TALL, -40, 14), (-3.0, 1.0, MID, -56, -40),
          (3.0, 1.0, MID, -56, 40), (0, 1.2, TALL, -58, 0), (-1.6, 3.0, MID, -76, -18), (1.6, 3.0, MID, -76, 18)]


def build(g):
    scalp(g, 21100, side_rows=3, back_rows=6, sideburn=2)
    ring_shell(g, 21101, side_rows=3, back_rows=6, ring_row=1)
    crown(g, "spike", SPIKES, 21102)
    bangs(g, "fringe", [(-2.4, ((2, 2), (1, 1)), 22), (0, ((2, 1), (1, 1)), 0), (2.4, ((2, 2), (1, 1)), -22)], seed=21140)
    for i, (x, rz) in enumerate(((-2.6, 30), (0, 0), (2.6, -30))):
        lock(g, f"nape_{i}", (x, -3.0, 4.3), (44, 0, rz), ((2, 2), (1, 1)), 1, 21150 + i * 5)
