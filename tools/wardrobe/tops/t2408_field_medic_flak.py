"""Field Medic Flak: the Konoha flak vest as the clan's medics wear it into battle, over a white
long-sleeved shirt with a white armband marked with a green sprig, herb pouches strapped to the
belt and short gloves."""
from kit import belt
from kit_shinobi import flak_vest
from kit_suzuran import armband, gloves, herb_pouch
from paint import fabric, strip_fabric

META = {
    "name": "Field Medic Flak",
    "gender": "unisex",
    "description": "Flak vest over a white shirt, medic armbands with a sprig, herb pouches on the belt, gloves.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 24581, 3)
    fabric(body.top, "S", "weave", 24581, 4)
    flak_vest(g, shoulder_swirls=False, seed=24582)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 24587 + (side == "left"), 3, 0, 9)
        fabric(arm.top, "S", "weave", 24587, 4)
    gloves(g, "K", top=10)
    armband(g, "armband", y=.8, role="D", mark="S4")
    belt(g, "belt", y=10.2, role="L", height=1, buckle="M")
    herb_pouch(g, "pouch_right", (-3.4, 10.6, -2.6), sprig=False)
    herb_pouch(g, "pouch_left", (3.4, 10.6, -2.6))
