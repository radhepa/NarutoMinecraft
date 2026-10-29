"""Two-Tone Zip Jacket: an older heiress's fitted jacket, lavender over the shoulders and sleeves
and cream through the body, with a high zipped collar, a lavender cuff and a cream hem band."""
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Two-Tone Zip Jacket",
    "gender": "unisex",
    "description": "Fitted jacket, lavender shoulders and sleeves over a cream body, high zipped collar.",
    "tags": ["shinobi", "hyuga", "jacket"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "plain", 4741, 2)
    cap(body, "A", texture="plain", seed=4741)
    # The lavender yoke dips to a point at the zip.
    strip_fabric(body, "A", "plain", 4742, 2, 0, 3)
    for x, y in ((2, 4), (3, 4), (4, 4), (5, 4), (3, 5), (4, 5)):
        body.front.set(x, y, "A2")
    body.strip.hline(0, body.strip.w - 1, 4, "A1")
    for x in (2, 3, 4, 5):
        body.front.set(x, 4, "A2")
    body.front.set(3, 6, "A1"), body.front.set(4, 6, "A1")
    body.front.vline(4, 0, 11, "M3"), body.front.vline(3, 7, 11, "S1")
    body.front.vline(1, 7, 10, "S1")
    strip_fabric(jacket, "S", "plain", 4743, 2, 10, 11)
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "S1")
    jacket.front.set(4, 10, "M3"), jacket.front.set(4, 11, "M2")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "A", "plain", 4744 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "A", "plain", 4744, 3)
        arm.strip.hline(0, arm.strip.w - 1, 4, "S2")
        strip_fabric(sleeve, "A", "plain", 4746, 2, 8, 10)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 8, "A3"), sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "A1")
    neck = g.piece("collar", "TORSO", (-4.5, -2.0, -2.7), (9, 2, 5), inflate=.08)
    solid(neck, "A", "plain", 4747, 2)
    neck.front.vline(4, 0, 1, "M3")
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "A3")
