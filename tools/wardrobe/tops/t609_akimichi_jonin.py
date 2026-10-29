"""Akimichi Jonin: the Konoha flak vest over the clan's deep red shirt, red lacquered sode on the
shoulders, a red belly lame below the vest and red forearm guards: how Akimichi jonin wear the
village's uniform."""
from kit import arm_bone, arm_x
from kit_akimichi import lames, sode
from kit_shinobi import flak_vest
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Akimichi Jonin",
    "gender": "unisex",
    "description": "Flak vest over a deep red shirt, red lacquered sode, a belly lame and forearm guards.",
    "tags": ["shinobi", "vest", "jonin", "akimichi"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 6881, 2)
    cap(body, "D", seed=6881)
    flak_vest(g, shoulder_swirls=False, seed=6882)
    lames(g, "belly_lame", [(8.6, 2, .45)], role="A", seed=6890, lacing="M3")
    sode(g, "sode", role="A", seed=6892, lacing="M3", stud="M3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 6895 + (side == "left"), 2)
        fabric(arm.top, "D", "weave", 6895, 3)
        fabric(arm.bottom, "D", "weave", 6895, 1)
        guard = g.piece(f"{side}_guard", arm_bone(side), (arm_x(side) - .3, 5.6, -2.3), (4, 4, 4), inflate=.12)
        solid(guard, "A", "smooth", 6897 + (side == "left"), 2, edge=False)
        for face in guard.sides:
            face.hline(0, face.w - 1, 0, "A3"), face.hline(0, face.w - 1, 3, "A1"), face.set(1, 1, "M3")
