"""Clan Flak Vest: the jonin's flak vest as the clan head wears it, over a dark long-sleeved shirt,
with a rough fur mantle at the collar and a red fang painted on each shoulder."""
from kit import sleeves
from kit_inuzuka import fang, fur_box
from kit_shinobi import flak_vest
from paint import cap, strip_fabric

META = {
    "name": "Clan Flak Vest",
    "gender": "unisex",
    "description": "The jonin flak vest with a fur mantle at the collar, red fangs on the shoulders, dark sleeves.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 8570, 2)
    cap(body, "D", seed=8570)
    flak_vest(g, shoulder_swirls=False, seed=8571)
    for arm in sleeves(g, "D", "weave", 8580, 2, rows=(0, 10)):
        arm.strip.hline(0, arm.strip.w - 1, 10, "D1")
    for side in ("right", "left"):
        sleeve = g.part(f"{side}_sleeve")
        outer = sleeve.right if side == "right" else sleeve.left
        fang(outer, 2 if side == "right" else 1, 1, "A3", h=3)
    mantle = g.piece("fur_mantle", "TORSO", (-5.5, -1.9, -3.2), (11, 3, 7))
    fur_box(mantle, "S", 8582, 2)
