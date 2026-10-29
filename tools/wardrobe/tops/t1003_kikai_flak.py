"""Kikai Flak: the war-era Aburame jonin, the olive flak vest over a dark full bodysuit, a pair of
kikaichu emblems on the collar and the bodysuit's own collar turned up behind the neck."""
from kit_aburame import BEETLE, glyph, high_collar
from kit_shinobi import flak_vest
from paint import cap, fabric, strip_fabric

META = {
    "name": "Kikai Flak",
    "gender": "unisex",
    "description": "Olive flak vest over a dark bodysuit, kikaichu emblems on the collar.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "K", "plain", 10561, 2)
    cap(body, "K", seed=10561)
    flak_vest(g, seed=10562)
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "K", "plain", 10570, 2, 0, 11)
        fabric(arm.top, "K", "plain", 10570, 3)
        (arm.right if side == "right" else arm.left).vline(1, 1, 10, "K3")   # the suit's outer seam
        strip_fabric(sleeve, "K", "plain", 10571, 2, 9, 11)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "K3")
    high_collar(g, "K", "plain", 10575, cover_mouth=False, back_top=-3.0, flare=2)
    # Below the collar points, where the head does not hide them.
    for side, x in (("right", -3.7), ("left", 1.3)):
        badge = g.piece(f"collar_beetle_{side}", "TORSO", (0, 0, 0), (8, 8, 1), pivot=(x, .5, -2.95),
                        scale=(.22, .22, .22))
        for face in badge.faces:
            fabric(face, "P", "plain", 10580, 2)
        glyph(badge.front, BEETLE, 0, 0, {"#": "K2", "+": "A3"})
