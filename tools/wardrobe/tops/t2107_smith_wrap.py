"""Smith Wrap: the off-white wrap tunic the clan's smiths work the forge in, crossed at the chest
with gunmetal edging, sleeves rolled to the elbow, a broad leather belt hung with a hammer and steel
bracers to take the sparks."""
from kit import belt, roll, sleeves
from kit_hagane import bracers
from paint import cap, solid, strip_fabric

META = {
    "name": "Smith Wrap",
    "gender": "unisex",
    "description": "Off-white wrap tunic with gunmetal edging, rolled sleeves, a leather belt with a hammer, bracers.",
    "tags": ["shinobi"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 21940, 2)
    cap(body, "S", texture="weave", seed=21940)
    # The crossed collar, right over left, edged in gunmetal.
    for y in range(0, 8):
        x = min(7, 1 + y)
        body.front.set(x, y, "P2")
        if x + 1 <= 7:
            body.front.set(x + 1, y, "P1")
    body.front.set(1, 0, "P3"), body.front.set(6, 0, "P3")
    for arm in sleeves(g, "S", "weave", 21941, 2, rows=(0, 4)):
        arm.strip.hline(0, arm.strip.w - 1, 0, "S3")
    roll(g, "S", 4.0, base=3, accent="P2")
    belt(g, "belt", y=8.8, role="L", height=2, buckle="M", inflate=.1)
    head = g.piece("hammer_head", "TORSO", (-1, 0, -1), (2, 2, 3), pivot=(-3.6, 10.0, -1.0))
    solid(head, "M", "plain", 21942, 2, edge=False)
    haft = g.piece("hammer_haft", "TORSO", (-.5, 0, -.5), (1, 4, 1), pivot=(-3.6, 12.0, -1.0))
    solid(haft, "L", "leather", 21943, 2)
    bracers(g, top=6.5, height=4, seed=21944)
