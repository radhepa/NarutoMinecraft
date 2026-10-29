"""Fan Zip Jacket: a young Uchiha's long-sleeved zip jacket with the collar turned up, white trim at
the cuffs and collar, a crest on the back and another on the left shoulder."""
from kit import arm_bone, arm_x
from kit_uchiha import arm_crest, back_crest, high_collar
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Fan Zip Jacket",
    "gender": "unisex",
    "description": "Long-sleeved zip jacket, collar turned up, white trim, crests on the back and shoulder.",
    "tags": ["shinobi", "genin", "uchiha"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 3845, 2)
    cap(body, "P", texture="twill", seed=3845)
    f = body.front
    f.vline(3, 0, 11, "M2"), f.vline(4, 0, 11, "P1")
    f.set(3, 0, "M4"), f.set(3, 1, "M3")
    body.strip.hline(0, body.strip.w - 1, 11, "S2")
    body.strip.hline(0, body.strip.w - 1, 10, "P1")
    # Slash pockets on the hips.
    f.set(1, 7, "P0"), f.set(2, 8, "P0"), f.set(6, 7, "P0"), f.set(5, 8, "P0")
    back_crest(g, "P", texture="twill", seed=3846)
    high_collar(g, "P", seed=3847, height=2, flare=10, trim="S3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 3849 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "twill", 3849, 3)
        arm.strip.hline(0, arm.strip.w - 1, 4, "P1")
        cuff = g.piece(f"{side}_cuff", arm_bone(side), (arm_x(side) - .3, 8.8, -2.3), (4, 2, 4), inflate=.1)
        solid(cuff, "S", "rib", 3851, 3, edge=False)
        for face in cuff.sides:
            face.hline(0, face.w - 1, 1, "S2")
    arm_crest(g, "left", "P", seed=3852)
