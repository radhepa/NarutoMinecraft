"""Kanzashi Pins: two lacquered hairpins pushed crosswise through the hair at the back of the head
on the left, a short string of metal drops hanging from one: they double as throwing needles."""
from paint import solid

META = {"name": "Kanzashi Pins", "gender": "unisex",
        "description": "Two crossed lacquered hairpins at the back left of the head, a string of metal drops."}


def build(g):
    for i, rz in enumerate((38, -30)):
        pin = g.piece(f"pin_{i}", "HEAD", (-.5, -3, -.5), (1, 6, 1), pivot=(2.6, -5.0, 5.0), rotation=(0, 0, rz),
                      scale=(.5, 1, .5))
        solid(pin, "K", "smooth", 33993 + i, 2, edge=False)
        pin.top.fill("A3"), pin.bottom.fill("A3")
        for face in pin.sides:
            face.set(0, 0, "A3")
    for j in range(3):
        drop = g.piece(f"drop_{j}", "HEAD", (-.5, j * 1.2, -.5), (1, 1, 1), pivot=(4.0, -7.6, 5.2), motion="sway",
                       scale=(.6, .6, .6))
        solid(drop, "M", "plain", 33995, 3 if j < 2 else 4, edge=False)
