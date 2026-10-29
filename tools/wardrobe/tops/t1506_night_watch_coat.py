"""Night Watch Coat: a long slate coat to the knee for the night patrol, a high collar, a belt
with a steel buckle, silver piping down the front edge and the katana slung on the back over it."""
from kit import belt, collar, flaps
from kit_gekko import katana
from paint import cap, fabric, strip_fabric

META = {
    "name": "Night Watch Coat",
    "gender": "unisex",
    "description": "Long slate coat to the knee, high collar, buckled belt, silver piping, a katana on the back.",
    "tags": ["shinobi", "jonin", "coat"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "D", "weave", 15760, 2)
    cap(body, "D", seed=15760)
    strip_fabric(jacket, "P", "twill", 15761, 2)
    cap(jacket, "P", texture="twill", seed=15761)
    jacket.front.vline(3, 0, 11, "S3"), jacket.front.vline(4, 0, 11, "P1")
    for y in (2, 5):
        jacket.front.set(2, y, "M3"), jacket.front.set(5, y, "M3")
    belt(g, "belt", y=8.8, role="L", buckle="M", inflate=.3)
    collar(g, "collar", "P", texture="twill", height=2, y=-1.5, inflate=.3)
    for face in flaps(g, "coat", 7, "P", "twill", 15763, width=9, hem="P1", top=11.0, front_z=-2.8, back_z=1.8, slit=True):
        face.vline(4, 1, 6, "S3")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "twill", 15765 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "P", "twill", 15765, 3)
        strip_fabric(sleeve, "P", "twill", 15767, 2, 0, 10)
        fabric(sleeve.top, "P", "twill", 15767, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "P1")
    katana(g, pivot=(-1.4, 2.2, 3.15))
