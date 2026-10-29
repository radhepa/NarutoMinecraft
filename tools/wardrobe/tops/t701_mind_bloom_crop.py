"""Mind Bloom Crop: the Yamanaka kunoichi's sleek purple top, sleeveless and cut short above a
chain-mesh midriff, with a small stand collar, a blossom at the throat, bandaged elbows and long
purple arm warmers from the elbow to the knuckles."""
from kit import arm_x, collar
from kit_shinobi import mesh
from kit_yamanaka import flower, wrapped
from paint import fabric, solid, strip_fabric

META = {
    "name": "Mind Bloom Crop",
    "gender": "unisex",
    "description": "Sleeveless purple crop top over a mesh midriff, bandaged elbows, long purple arm warmers.",
    "tags": ["shinobi", "yamanaka"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "plain", 7150, 2, 0, 5)
    fabric(body.top, "P", "plain", 7150, 3)
    mesh(body.strip, 0, 6, body.strip.w - 1, 8, "K3")
    # A snug fitted hem one texel proud of the mesh, and the shaping darts.
    strip_fabric(jacket, "P", "plain", 7151, 2, 5, 5)
    jacket.strip.hline(0, jacket.strip.w - 1, 5, "P1")
    f = body.front
    f.vline(2, 2, 4, "P1"), f.vline(5, 2, 4, "P3"), f.hline(3, 4, 0, "P0")
    for face in (body.right, body.left):
        face.vline(1, 0, 5, "P1")
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        arm.strip.hline(0, arm.strip.w - 1, 0, "P2"), fabric(arm.top, "P", "plain", 7152, 3)
        wrapped(arm.strip, 0, 4, arm.strip.w - 1, 5)
        strip_fabric(arm, "P", "plain", 7153 + (side == "left"), 2, 6, 10)
        strip_fabric(sleeve, "P", "plain", 7155, 2, 6, 10)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 6, "P3"), sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "P1")
        band = g.piece(f"{side}_warmer_band", bone, (arm_x(side) - .3, 5.7, -2.3), (4, 1, 4), inflate=.12)
        solid(band, "A", "plain", 7156, 2)
    neck = collar(g, "collar", "P", "plain", height=1, y=-.9)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "P3")
    flower(g, "brooch", (0, .4, -2.75), bone="TORSO")
