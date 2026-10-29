"""Kennel Keeper Wrap: the clan vet's working clothes, a wrapped top with the sleeves rolled to the
elbow, a heavy leather apron belted at the waist with a pocket of tools, and a red cord tied at the
hip: for the kennels and the infirmary both."""
from kit import arm_x, belt, flaps
from kit_inuzuka import paw
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Kennel Keeper Wrap",
    "gender": "unisex",
    "description": "Wrapped top with rolled sleeves, a belted leather apron with a tool pocket, a red hip cord.",
    "tags": ["shinobi", "chunin"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 8540, 2)
    cap(body, "P", texture="weave", seed=8540)
    f = body.front
    for i in range(6):
        f.set(1 + i, i, "S3"), f.set(2 + i, i, "P1")
    # The leather apron: a bib over the chest and a skirt panel down the front.
    bib = g.piece("apron_bib", "TORSO", (-3, 0, 0), (6, 6, 1), pivot=(0, 3.4, -2.6))
    solid(bib, "L", "leather", 8541, 2)
    bib.front.hline(0, 5, 0, "L3")
    pocket = bib.front
    pocket.hline(1, 4, 3, "L3"), pocket.vline(1, 3, 5, "L1"), pocket.vline(4, 3, 5, "L1")
    pocket.set(2, 2, "M3"), pocket.set(3, 2, "M2")
    for i, x in enumerate((-1.6, 1.6)):
        strap = g.piece(f"apron_strap_{i}", "TORSO", (-.5, 0, 0), (1, 4, 1), pivot=(x * 1.5, -.2, -2.6))
        solid(strap, "L", "leather", 8542 + i, 2, edge=False)
    belt(g, "apron_belt", y=9.2, role="L", buckle="M", inflate=.12)
    front, back = flaps(g, "apron", 6, "L", "leather", 8544, width=8, hem="L1", top=11.0, front_z=-2.9, back_z=1.9)
    paw(front, 2, 1, "L3")
    # Rolled sleeves: cloth to the elbow and a thick roll.
    for side, bone in (("right", "RIGHT_ARM"), ("left", "LEFT_ARM")):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "weave", 8546 + (side == "left"), 2, 0, 4)
        fabric(arm.top, "P", "weave", 8546, 3)
        roll = g.piece(f"{side}_roll", bone, (arm_x(side) - .45, 4.2, -2.45), (5, 2, 5))
        solid(roll, "S", "weave", 8548, 3)
        for face in roll.sides:
            face.hline(0, face.w - 1, 0, "S4")
    cord = g.piece("hip_cord", "TORSO", (0, 0, 0), (1, 4, 1), pivot=(3.2, 10.0, -2.9), rotation=(0, 0, -8), motion="flap_front")
    solid(cord, "A", "weave", 8549, 2)
