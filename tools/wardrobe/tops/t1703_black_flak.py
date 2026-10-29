"""Black Flak: the Konoha flak vest dyed black for the Interrogation Force, worn over the slate
long-sleeved uniform with the oxblood force band round the left arm."""
from kit_morino import armband
from kit_shinobi import flak_vest
from paint import cap, fabric, strip_fabric

META = {
    "name": "Black Flak",
    "gender": "unisex",
    "description": "Black flak vest over the slate long-sleeved uniform, the oxblood force band on the left arm.",
    "tags": ["shinobi", "vest"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 17241, 2)
    cap(body, "S", seed=17241)
    flak_vest(g, seed=17242)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 17244 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "S", "weave", 17244, 3)
        arm.strip.hline(0, arm.strip.w - 1, 11, "S1")
    armband(g, "left", y=2.2)
