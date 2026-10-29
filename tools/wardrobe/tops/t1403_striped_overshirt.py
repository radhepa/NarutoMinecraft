"""Striped Overshirt: Kurenai's dress after the war, a black long-sleeved shirt under a sleeveless
overshirt with three bright stripes across the front, belted loosely at the hips."""
from paint import fabric, strip_fabric

META = {
    "name": "Striped Overshirt",
    "gender": "unisex",
    "description": "Sleeveless overshirt with three stripes over a black long-sleeved shirt.",
    "tags": ["shinobi", "casual"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "K", "weave", 14660, 2)
    fabric(body.top, "K", "weave", 14661, 3), fabric(body.bottom, "K", "weave", 14661, 1)
    strip_fabric(jacket, "P", "twill", 14662, 2, 0, 10)
    fabric(jacket.top, "P", "twill", 14663, 3)
    # The overshirt is sleeveless: its armholes leave the black shirt's shoulders showing at the sides.
    for face in (jacket.right, jacket.left):
        for y in range(0, 3):
            for x in range(face.w):
                face.clear(x, y)
        face.vline(1, 3, 10, "P1")
    jacket.front.hline(3, 4, 0, None), jacket.front.set(3, 1, None), jacket.front.set(4, 1, None)
    jacket.front.set(2, 0, "P3"), jacket.front.set(5, 0, "P1")
    # The three stripes run right round the overshirt below the armholes.
    for y in (4, 6, 8):
        for face in jacket.sides:
            face.hline(0, face.w - 1, y, "A2")
    jacket.strip.hline(0, jacket.strip.w - 1, 10, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "K", "weave", 14664 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "K", "weave", 14666, 3), fabric(arm.bottom, "K", "weave", 14666, 1)
        arm.strip.hline(0, arm.strip.w - 1, 10, "K3"), arm.strip.hline(0, arm.strip.w - 1, 11, "K1")
