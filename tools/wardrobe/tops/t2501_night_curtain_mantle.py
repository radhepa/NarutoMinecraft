"""Night Curtain Mantle: the Tobari jonin's dress, a fitted charcoal shirt under a two-tier pleated
mantle that falls like a drawn curtain, the upper tier over the shoulders and arms, the hood worn
down, the night-curtain crest on the back, a dark sash and the amber paper lantern at the hip."""
from kit import sleeves
from kit_tobari import decal, lantern, mantle, plain_body, sash
from paint import fabric

META = {
    "name": "Night Curtain Mantle",
    "gender": "unisex",
    "description": "Two-tier pleated hooded mantle over a charcoal shirt, the curtain crest, a sash and a paper lantern.",
    "tags": ["shinobi", "mantle", "jonin"],
}


def build(g):
    plain_body(g, "D", "weave", 25300)
    for arm in sleeves(g, "D", "weave", 25301, rows=(0, 11)):
        for y in (8, 9, 10):
            arm.strip.hline(0, arm.strip.w - 1, y, "S3" if y % 2 else "S2")
        fabric(arm.bottom, "K", "plain", 25303, 1)
    mantle(g, "mantle", "P", "twill", 25304, length=9, tiers=2, trim=None)
    decal(g, "back_crest", "P2", (0, 2.7, 2.85))
    sash(g, "sash", "K", y=9.3, knot="right")
    lantern(g, "lantern", pivot=(2.4, 10.4, -2.9))
