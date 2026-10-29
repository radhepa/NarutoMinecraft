"""Open Field Vest: a jonin vest worn unzipped over a dark shirt and a mesh undershirt, a notched
collar folded flat, two pockets low at the belly and forearm guards: off duty but never unarmed."""
from kit_field import arm_guards, chain, collar, pocket, shirt, vest

META = {
    "name": "Open Field Vest",
    "gender": "unisex",
    "description": "Unzipped padded vest over a shirt and mesh undershirt, notched collar, forearm guards.",
    "tags": ["shinobi", "vest", "jonin"],
}


def build(g):
    body = shirt(g, "D", 32060)
    chain(body.front, 2, 0, 5, 11)
    vest(g, "P", 32064, closure="open", ribs=(3, 6, 9))
    collar(g, "collar", "P", 32065, style="notch")
    for i, x in enumerate((-2.6, 2.6)):
        pocket(g, f"belly_pocket_{i}", (x, 6.2, -2.3), (4, 4, 1), "P", 32066 + i, snap="M3")
    arm_guards(g, 32068, y=5.4, height=3)
