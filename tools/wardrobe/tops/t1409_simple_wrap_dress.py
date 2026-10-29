"""Simple Wrap Dress: the soft, plain dress Kurenai wore while she waited for Mirai: long sleeves, a
crossed wrap neckline, a sash tied high under the bust with its ends hanging, and a full skirt
falling past the knee."""
from kit import belt, flaps
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Simple Wrap Dress",
    "gender": "female",
    "description": "Soft long-sleeved wrap dress, sash tied high with hanging ends, skirt past the knee.",
    "tags": ["dress", "wrap"],
    "rejects": ["skirt"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 14840, 2)
    cap(body, "P", texture="plain", seed=14840)
    f = body.front
    for i in range(4):
        f.set(1 + i, i, "P3"), f.set(6 - i, i, "P1")
    sash = belt(g, "sash", y=4.8, role="S", height=1, buckle=None, inflate=.1)
    for i, (x, rz) in enumerate(((-1.0, 6), (-.3, -6))):
        end = g.piece(f"sash_end_{i}", "TORSO", (-.5, 0, -.5), (1, 6 - i, 1), pivot=(x, 5.8, -2.75), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "S", "weave", 14841 + i, 3)
    for face in flaps(g, "skirt", 9, "P", "plain", 14843, width=9, top=10.4, front_z=-2.8, back_z=1.8):
        face.hline(0, face.w - 1, face.h - 1, "P1")
        face.vline(2, 2, face.h - 2, "P1"), face.vline(6, 3, face.h - 2, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "plain", 14844 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "plain", 14846, 3)
        arm.strip.hline(0, arm.strip.w - 1, 10, "S3")
