"""Torune Suit: Torune's Root bodysuit, black from the collar to the wrists, chain mesh on the
forearms, bandaged hands, a short jacket over the shoulders hung with red cords and a red sash."""
from kit import belt
from kit_aburame import high_collar
from kit_shinobi import bandage, mesh
from paint import cap, fabric, k, solid, strip_fabric

META = {
    "name": "Torune Suit",
    "gender": "unisex",
    "description": "Black high-collared bodysuit, mesh forearms, bandaged hands, red-corded shoulder jacket, red sash.",
    "tags": ["shinobi", "aburame"],
}


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "P", "rib", 10641, 2)
    cap(body, "P", seed=10641)
    # The short jacket: shoulders and chest to the ribs.
    strip_fabric(jacket, "P", "plain", 10642, 3, 0, 5)
    fabric(jacket.top, "P", "plain", 10642, 3)
    jacket.strip.hline(0, jacket.strip.w - 1, 5, "P1")
    jacket.front.vline(4, 0, 5, "P0")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "P", "rib", 10643, 2, 0, 8)
        fabric(arm.top, "P", "rib", 10643, 3)
        for face in arm.sides:
            mesh(face, 0, 5, face.w - 1, 8, "P0")
            bandage(face, 0, 9, face.w - 1, 11)
        strip_fabric(sleeve, "P", "plain", 10644 + (side == "left"), 3, 0, 3)
        fabric(sleeve.top, "P", "plain", 10644, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 3, "P1")
        # Red cords hanging from the shoulder seam.
        x = -5.4 if side == "right" else 5.4
        for i, z in enumerate((-1.4, 0, 1.4)):
            cord = g.piece(f"{side}_cord_{i}", "TORSO", (-.5, 0, -.5), (1, 3 + (i == 1), 1), pivot=(x, 1.0, z),
                           rotation=(0, 0, 6 if side == "right" else -6), scale=(.5, 1, .5))
            solid(cord, "A", "plain", 10646 + i, 2, edge=False)
    high_collar(g, "P", "rib", 10650, front_top=-2.4)
    sash = belt(g, "sash", y=9.4, role="A", height=2, buckle=None)
    tail = g.piece("sash_tail", "TORSO", (-1, 0, 0), (2, 4, 1), pivot=(2.6, 10.6, -2.75), rotation=(0, 0, -8),
                   motion="flap_front")
    solid(tail, "A", "weave", 10655, 2)
    sash.front.set(6, 0, "A3")
