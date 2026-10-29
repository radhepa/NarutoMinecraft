"""Rose Thorn Wrap: Kurenai Yuhi's dress, broad ivory bandage cloth wound around the body and printed
with crimson rose thorns, wrapped from the right shoulder across to the left hip. A single red mesh
sleeve covers the right arm, the left shoulder is bare, both hands are bandaged and the wraps fall
to a short skirt at mid-thigh."""
from kit import flaps
from kit_yuhi import bandage_turns, thorn_band, thorn_wrap
from paint import fabric, k, solid

META = {
    "name": "Rose Thorn Wrap",
    "gender": "female",
    "description": "Thorn-printed bandage wrap dress, one red mesh sleeve on the right arm, bandaged hands.",
    "tags": ["shinobi", "dress", "wrap"],
    "rejects": ["skirt"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    for f in body.sides:
        thorn_wrap(f, 0, 0, f.w - 1, f.h - 1, "P", "A", 2, 14600 + f.x0)
    fabric(body.top, "P", "plain", 14601, 3), fabric(body.bottom, "P", "plain", 14602, 1)
    f = body.front
    # The wrap's leading edge: a shaded fold from the right shoulder down to the left hip.
    for i in range(9):
        x = 1 + (i * 6) // 8
        f.set(x, i, "P0"), f.set(x + 1, i, "P3")
    # Bare left shoulder: the wrap starts at the collarbone on that side.
    body.left.hline(0, body.left.w - 1, 0, "P3")
    # A raised wrap band crossing the waist on the jacket layer.
    jacket = g.part("jacket")
    for face in jacket.sides:
        bandage_turns(face, 0, 7, face.w - 1, 8, "P", 2, lean=-1)
        thorn_band(face, 8, "A")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        if side == "right":
            # The red mesh armour sleeve from shoulder to wrist, the skin showing through.
            for y in range(9):
                for x in range(arm.strip.w):
                    arm.strip.set(x, y, "A1" if x % 2 == 0 and y % 2 == 0 else ("A3" if (x + y) % 4 == 1 else "A2"))
            fabric(arm.top, "A", "plain", 14603, 2)
            sleeve.strip.hline(0, sleeve.strip.w - 1, 0, "P3"), sleeve.strip.hline(0, sleeve.strip.w - 1, 1, "P2")
            fabric(sleeve.top, "P", "plain", 14604, 3)
        bandage_turns(arm.strip, 0, 9, arm.strip.w - 1, 11, "S", 3)
        fabric(arm.bottom, "S", "plain", 14605, 2)
    for face in flaps(g, "skirt", 5, "P", "plain", 14606, width=9, top=11.0, front_z=-2.75, back_z=1.75):
        thorn_wrap(face, 0, 1, face.w - 1, face.h - 1, "P", "A", 2, 14607)
        face.hline(0, face.w - 1, face.h - 1, "P1")
