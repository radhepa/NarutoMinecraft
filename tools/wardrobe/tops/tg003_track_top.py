"""Track Top: a zip tracksuit top with two stripes down each sleeve, a stand-up collar edged in the
stripe color and elastic cuffs: the genin who runs laps before breakfast."""
from kit import collar
from kit_academy import ribbed, shirt, side_stripe, zip_front, zip_pull

META = {
    "name": "Track Top",
    "gender": "unisex",
    "description": "Zip tracksuit top, two stripes down each sleeve, a stand-up collar and elastic cuffs.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body, arms = shirt(g, "P", "plain", 31030, sleeve=10)
    zip_front(body.front, 0, 10, "S3", "P1")
    ribbed(body, (11,), "K")
    # A contrast panel down each side seam.
    for face in (body.right, body.left):
        face.vline(1, 1, 10, "S2"), face.vline(2, 1, 10, "A2")
    for side, arm in zip(("right", "left"), arms):
        side_stripe(arm, side, (0, 9), "S3", double="A2")
        ribbed(arm, (10,), "K")
        arm.front.vline(1, 3, 8, "P1")
    neck = collar(g, "collar", "P", "plain", height=2, y=-1.6)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "S3")
    neck.front.vline(4, 0, 1, "S3")
    zip_pull(g, 31032, 1.0)
