"""Ward Tunic: the trainee medic's short-sleeved tunic, fastened across the chest at the side with a
band of the corps colour round the neck and hem, worn over bandaged forearms with the cross on the
left sleeve."""
from kit_shinobi import bandage
from kit_specialist import cross_armband
from paint import cap, fabric, strip_fabric

META = {
    "name": "Ward Tunic",
    "gender": "unisex",
    "description": "Short-sleeved tunic fastened at the side, corps-colour trim, bandaged forearms, cross armband.",
    "tags": ["shinobi", "tunic", "genin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 34040, 2)
    cap(body, "P", texture="weave", seed=34040)
    f = body.front
    f.hline(1, 6, 0, "A2")
    for y in range(1, 9):
        f.set(min(7, 2 + y // 2 + 1), y, "A2")
    for y in (2, 5):
        f.set(min(7, 2 + y // 2), y, "M3")
    body.strip.hline(0, body.strip.w - 1, 11, "A2"), body.strip.hline(0, body.strip.w - 1, 10, "P1")
    body.back.hline(1, 6, 0, "A2")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 34041 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "P", "weave", 34041, 3)
        arm.strip.hline(0, arm.strip.w - 1, 4, "A2")
        bandage(arm.strip, 0, 7, arm.strip.w - 1, 10)
    cross_armband(g, "left", y=-.8, seed=34045)
