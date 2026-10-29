"""Half Coat: a hip-length black coat with a standing collar and a hidden fly, oxblood piping down
the front and round the cuffs, two flapped pockets: the field interrogator's working coat."""
from kit import collar
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Half Coat",
    "gender": "unisex",
    "description": "Hip-length black coat with a standing collar, oxblood piping, two flapped pockets.",
    "tags": ["shinobi", "jacket"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "twill", 17301, 2)
    cap(body, "P", texture="twill", seed=17301)
    strip_fabric(jacket, "P", "twill", 17302, 2)
    cap(jacket, "P", texture="twill", seed=17302)
    jacket.front.vline(4, 0, 11, "A2")
    jacket.strip.hline(0, jacket.strip.w - 1, 11, "A1")
    for x0 in (0, 5):
        jacket.front.hline(x0, x0 + 2, 7, "P0"), jacket.front.hline(x0, x0 + 2, 6, "P3")
    neck = collar(g, "collar", "P", "twill", height=2, y=-1.6, inflate=.1)
    for face in neck.sides:
        face.hline(0, face.w - 1, 0, "A2")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "twill", 17303 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "P", "twill", 17303, 3)
        strip_fabric(sleeve, "P", "twill", 17305, 2, 0, 10)
        fabric(sleeve.top, "P", "twill", 17305, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "A2")
    hem = g.piece("coat_hem", "TORSO", (-4.5, 11, -2.6), (9, 2, 5), inflate=.12)
    solid(hem, "P", "twill", 17306, 2)
    for face in hem.sides:
        face.hline(0, face.w - 1, 1, "A1")
    hem.front.vline(4, 0, 1, "A2")
