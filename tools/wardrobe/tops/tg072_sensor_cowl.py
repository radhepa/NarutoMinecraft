"""Sensor Cowl: a young sensor's sleeveless tunic with a loose cowl of cloth gathered round the
neck and shoulders, its hood hanging behind, and wrapped forearms for the hand signs."""
from kit_aburame import hood_down
from kit_yamanaka import wrapped
from paint import cap, k, solid, strip_fabric

META = {
    "name": "Sensor Cowl",
    "gender": "unisex",
    "description": "Sleeveless tunic with a loose cowl round the neck, hood hanging behind, wrapped forearms.",
    "tags": ["shinobi", "tunic", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 34220, 2)
    cap(body, "P", texture="weave", seed=34220)
    body.strip.hline(0, body.strip.w - 1, 9, "L2"), body.strip.hline(0, body.strip.w - 1, 10, "L1")
    body.front.set(3, 9, "M3")
    body.front.vline(4, 3, 8, "P1")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 34221, 1, 0, 1)
        wrapped(arm.strip, 0, 6, arm.strip.w - 1, 10, "S")
    cowl = g.piece("cowl", "TORSO", (-5, -1.6, -3.0), (10, 3, 6), inflate=.15)
    solid(cowl, "S", "weave", 34222, 2)
    cowl.top.fill(k("S", 0))
    for face in cowl.sides:
        face.hline(0, face.w - 1, 0, "S3")
        for x in range(0, face.w, 3):
            face.vline(x, 1, 2, "S1")
    drape = g.piece("cowl_drape", "TORSO", (-3, 0, 0), (6, 3, 1), pivot=(0, 1.2, -3.1), rotation=(-6, 0, 0))
    solid(drape, "S", "weave", 34223, 2)
    drape.front.hline(1, 4, 2, "S1"), drape.front.set(0, 2, "S1"), drape.front.set(5, 2, "S1")
    hood_down(g, "S", "weave", 34224)
