"""Field Coat: a dusky-brown coat to the knee with a steel-grey collar and cuffs, a needle bandolier
slung over it from the right shoulder and a buckled belt: for long watches out of the village."""
from kit import belt, collar, flaps
from kit_shiranui import bandolier
from paint import cap, fabric, strip_fabric

META = {
    "name": "Field Coat",
    "gender": "unisex",
    "description": "Dusky knee coat, steel collar and cuffs, a senbon bandolier over the shoulder, buckled belt.",
    "tags": ["shinobi", "jonin", "coat"],
    "covers_waist": True,
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "weave", 16820, 2)
    cap(body, "P", seed=16820)
    strip_fabric(jacket, "D", "twill", 16821, 2)
    cap(jacket, "D", texture="twill", seed=16821)
    jacket.front.vline(4, 0, 11, "D0"), jacket.front.vline(5, 0, 11, "D3")
    bandolier(jacket.front, "L", rows=9)
    bandolier(jacket.back, "L", rows=9, mirror=True)
    belt(g, "belt", y=8.8, role="L", buckle="M", inflate=.3)
    collar(g, "collar", "P", height=2, y=-1.5, inflate=.3)
    for face in flaps(g, "coat", 7, "D", "twill", 16823, width=9, hem="D1", top=11.0, front_z=-2.8, back_z=1.8, slit=True):
        face.vline(5, 1, 6, "D3")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "D", "twill", 16825 + (side == "left"), 2, 0, 11)
        fabric(arm.top, "D", "twill", 16825, 3)
        strip_fabric(sleeve, "D", "twill", 16827, 2, 0, 11)
        fabric(sleeve.top, "D", "twill", 16827, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 10, "P2"), sleeve.strip.hline(0, sleeve.strip.w - 1, 11, "P1")
