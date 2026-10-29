"""Practice Gi: the dojo jacket every Gekko child learns the sword in: a heavy white gi wrapped
over with an indigo collar band, sleeves to the elbow, an indigo belt and a wooden practice sword
slung on the back."""
from kit import belt
from kit_gekko import katana
from paint import cap, fabric, strip_fabric

META = {
    "name": "Practice Gi",
    "gender": "unisex",
    "description": "White wrapped gi with an indigo collar band, elbow sleeves, indigo belt, a wooden sword on the back.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 15780, 2)
    cap(body, "S", texture="weave", seed=15780)
    f = body.front
    for i in range(8):
        x = 1 + i
        if x <= 7:
            f.set(x, i, "D2")
            if x + 1 <= 7:
                f.set(x + 1, i, "D1")
    f.set(0, 0, "D2"), f.set(0, 1, "D2")
    belt(g, "belt", y=8.8, role="D", buckle=None, height=1, inflate=.12)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 15782 + (side == "left"), 2, 0, 5)
        fabric(arm.top, "S", "weave", 15782, 3)
        arm.strip.hline(0, arm.strip.w - 1, 5, "S1")
    # A bokken: the same sword shape in plain wood, no guard cord.
    hilt, guard, blade = katana(g, "bokken", pivot=(-1.4, 2.4, 2.75), cord=None, wrap="L3")
    for box in (hilt, blade):
        for face in box.faces:
            face.recolor(lambda key, x, y: "L" + key[1] if key[0] in "KM" else key)
    for face in guard.faces:
        face.fill("L1")
