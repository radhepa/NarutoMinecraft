"""High Collar Sleeveless: a fitted sleeveless top zipped to a tall collar that hides the chin's
line, a contrast panel down the front and long arm warmers banded at the elbow."""
from kit_kunoichi import arm_warmers
from paint import cap, solid, strip_fabric

META = {
    "name": "High Collar Sleeveless",
    "gender": "unisex",
    "description": "Fitted sleeveless top zipped to a tall collar, a front panel, long arm warmers.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 33040, 2)
    cap(body, "P", seed=33040)
    f = body.front
    for y in range(12):
        f.set(3, y, "S2"), f.set(4, y, "S3")
    f.vline(4, 0, 8, "M3")
    for face in (body.right, body.left):
        face.vline(1, 0, 11, "P1")
    body.strip.hline(0, body.strip.w - 1, 11, "P1")
    arm_warmers(g, "P", 33041, rows=(5, 10), band="A2")
    for side in ("right", "left"):
        g.part(f"{side}_arm").strip.hline(0, 15, 0, "P2")
    neck = g.piece("collar", "TORSO", (-4.5, -2.4, -2.6), (9, 3, 5), inflate=.06)
    solid(neck, "P", "plain", 33044, 2)
    neck.front.vline(4, 0, 2, "M3")
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "A2")
