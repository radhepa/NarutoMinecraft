"""Fan Jonin Vest: the Konoha flak vest as the clan's jonin wear it, over a dark high-necked shirt,
the fan crest on both shoulders in place of the swirl and white warmers on the forearms."""
from kit_shinobi import flak_vest
from kit_uchiha import arm_crest, arm_warmers, back_crest
from paint import cap, fabric, strip_fabric

META = {
    "name": "Fan Jonin Vest",
    "gender": "unisex",
    "description": "Flak vest over a dark shirt, fan crests on both shoulders, white forearm warmers.",
    "tags": ["shinobi", "vest", "jonin", "uchiha"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 3885, 2)
    cap(body, "D", seed=3885)
    flak_vest(g, shoulder_swirls=False, seed=3886)
    # The clan's own vests carry the crest over the swirl on the back.
    back_crest(g, "P", pivot=(0, 1.9, 2.85), texture="plain", seed=3887, width=13, height=16)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 3895 + (side == "left"), 2, 0, 5)
        fabric(arm.top, "D", "weave", 3895, 3)
        arm_crest(g, side, "D", seed=3897)
    arm_warmers(g, rows=(6, 10), role="S", seed=3898)
