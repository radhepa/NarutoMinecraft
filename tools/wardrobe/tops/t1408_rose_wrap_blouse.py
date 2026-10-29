"""Rose Wrap Blouse: an elegant crimson blouse wrapped across the bust and tied at the side, a rose
pinned at the left shoulder, one long mesh sleeve on the right arm after Kurenai's dress, the left
arm bare to a bandaged wrist, and a short peplum over the hips."""
from kit import flaps
from kit_shinobi import mesh
from kit_yuhi import bandage_turns, rose, thorn_band
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Rose Wrap Blouse",
    "gender": "female",
    "description": "Crimson wrap blouse with a rose at the shoulder, one mesh sleeve, bandaged wrist, short peplum.",
    "tags": ["shinobi", "wrap"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "plain", 14810, 2)
    cap(body, "P", seed=14810)
    f = body.front
    for i in range(7):
        x = 6 - i
        if x >= 0:
            f.set(x, i, "P3"), f.set(max(0, x - 1), i, "P1")
    f.hline(0, 7, 8, "P1")
    for face in body.sides:
        thorn_band(face, 9, "A", ground="P2")
    tie = g.piece("side_tie", "TORSO", (-.5, 0, -.5), (1, 3, 1), pivot=(3.6, 8.4, -2.7), rotation=(0, 0, -8), motion="sway")
    solid(tie, "P", "plain", 14811, 3)
    for face in flaps(g, "peplum", 3, "P", "plain", 14812, width=9, top=10.4, front_z=-2.75, back_z=1.75):
        face.hline(0, face.w - 1, face.h - 1, "A2")
    rose(g, "brooch", (2.6, .6, -2.4), bone="TORSO", petal="A", base=2)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        fabric(arm.top, "P", "plain", 14813, 3)
        arm.strip.hline(0, arm.strip.w - 1, 0, "P2")
        if side == "right":
            mesh(arm.strip, 0, 1, arm.strip.w - 1, 10, "K1")
        bandage_turns(arm.strip, 0, 9 if side == "left" else 10, arm.strip.w - 1, 11, "S", 3)
