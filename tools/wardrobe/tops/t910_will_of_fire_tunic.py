"""Will of Fire Tunic: an invention for the clan's kunoichi and medics. A long sleeveless tunic to
mid-thigh, split at the sides, flame tongues rising from its hem, a high collar, mesh sleeves
beneath and the Sarutobi crest on the back, belted with a dark sash."""
from kit import belt, flaps
from kit_sarutobi import crest_patch, flame_hem
from kit_shinobi import mesh
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Will of Fire Tunic",
    "gender": "unisex",
    "description": "Long sleeveless tunic with flames at the hem, high collar, mesh sleeves, the crest on the back.",
    "tags": ["shinobi", "robe"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 9850, 2)
    cap(body, "P", seed=9850)
    body.front.vline(4, 1, 8, "P1")
    for y in (2, 4, 6):
        body.front.set(3, y, "S3")
    belt(g, "sash", y=8.6, role="K", height=2, buckle=None, inflate=.12)
    for face in flaps(g, "tunic", 5, "P", "weave", 9851, width=9, hem=None, top=10.8, front_z=-2.8, back_z=1.8):
        flame_hem(face, 0, k("A", 2), k("A", 4))
    collar = g.piece("collar", "TORSO", (-4.5, -1.6, -2.7), (9, 2, 5), inflate=.08)
    solid(collar, "P", "weave", 9852, 2)
    for f in collar.sides:
        f.hline(0, f.w - 1, 0, "A2")
    collar.front.vline(4, 0, 1, "P0")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "K", "plain", 9853, 2, 0, 9)
        for f in arm.sides:
            mesh(f, 0, 0, f.w - 1, 9, "K1")
        fabric(arm.top, "P", "weave", 9854, 3)
        arm.strip.hline(0, arm.strip.w - 1, 0, "P2")
    crest_patch(g, "back_crest", "TORSO", (0, 1.4, 2.08), "P", "A2", 9855)
