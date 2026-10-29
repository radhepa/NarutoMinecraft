"""Slit Tunic: a steel-grey tunic with a stand collar falling to mid-thigh, slit at the sides so the
legs move freely, a dusky sash with a needle case at the hip and close dusky sleeves."""
from kit import collar, flaps, pouch
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Slit Tunic",
    "gender": "unisex",
    "description": "Steel tunic to mid-thigh slit at the sides, stand collar, dusky sash with a needle case.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 16830, 2)
    cap(body, "P", seed=16830)
    body.front.vline(5, 0, 11, "P1"), body.front.set(5, 2, "M3"), body.front.set(5, 5, "M3")
    collar(g, "collar", "P", height=1, y=-.9)
    sash = g.piece("sash", "TORSO", (-4.6, 8.6, -2.6), (9, 2, 5), inflate=.1)
    solid(sash, "D", "weave", 16831, 2, edge=False)
    for face in flaps(g, "tunic", 4, "P", "weave", 16832, width=8, hem="P1", top=10.8, front_z=-2.7, back_z=1.7):
        face.vline(0, 0, 3, "P1")
    pouch(g, "needle_case", (3.0, 9.0, -2.4), size=(1, 4, 1), role="L")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "D", "weave", 16834 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "P", "weave", 16834, 3)
        arm.strip.hline(0, arm.strip.w - 1, 0, "P2"), arm.strip.hline(0, arm.strip.w - 1, 1, "P1")
