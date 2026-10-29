"""Scroll Rack Vest: a jonin vest with two tall scroll sleeves either side of the zip, the scroll caps
showing at the top, sleeves rolled to the elbow and fingerless gloves: a long-range summoner's kit."""
from kit import roll
from kit_field import collar, gloves, pocket, shirt, vest
from paint import solid

META = {
    "name": "Scroll Rack Vest",
    "gender": "unisex",
    "description": "Padded vest with two tall scroll sleeves, rolled sleeves and fingerless gloves.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    shirt(g, "D", 32040, sleeve=5)
    roll(g, "D", 3.8)
    gloves(g, "K", 32044)
    vest(g, "P", 32046, ribs=(3, 7))
    collar(g, "collar", "P", 32047)
    for i, x in enumerate((-2.0, 2.0)):
        rack = pocket(g, f"scroll_sleeve_{i}", (x, 3.0, -2.3), (4, 10, 1), "P", 32048 + i)
        rack.front.vline(1, 2, 9, "P1")
        for j, dx in enumerate((-.6, .6)):
            cap = g.piece(f"scroll_cap_{i}_{j}", "TORSO", (-.5, -1, -.5), (1, 1, 1), pivot=(x + dx, 3.1, -2.55))
            solid(cap, "S", "plain", 32050 + i * 2 + j, 3, edge=False)
            cap.top.fill("A2")
