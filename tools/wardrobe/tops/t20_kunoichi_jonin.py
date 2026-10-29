"""Kunoichi Jonin Vest: the jonin flak vest over a wine long-sleeved shirt, fingerless gloves, a red
sash at the waist and a wrap skirt split at the front over the shorts."""
from kit import belt, flaps
from kit_shinobi import flak_vest
from paint import fabric, strip_fabric

META = {
    "name": "Kunoichi Jonin Vest",
    "gender": "unisex",
    "description": "Flak vest over a wine shirt, fingerless gloves, red sash and a split wrap skirt.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 401, 2)
    fabric(body.top, "D", "weave", 401, 3), fabric(body.bottom, "D", "weave", 402, 1)
    flak_vest(g, seed=403)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 410 + (side == "left"), 2, 0, 9)
        fabric(arm.top, "D", "weave", 410, 3)
        arm.strip.hline(0, arm.strip.w - 1, 9, "D1")
        strip_fabric(arm, "K", "smooth", 412, 2, 10, 10)
    sash = belt(g, "sash", y=10.2, role="A", height=1, buckle=None, inflate=.15)
    sash.front.set(6, 0, "A3")
    for face in flaps(g, "wrap_skirt", 4, "D", "weave", 413, top=11.0, hem="D1", slit=True):
        face.hline(0, face.w - 1, 0, "D3")
