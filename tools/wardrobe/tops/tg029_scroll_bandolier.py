"""Scroll Bandolier: a long-sleeved shirt crossed from the right shoulder to the left hip by a leather
bandolier carrying four sealing scrolls, accent-capped, with a pouch at its foot."""
from kit import belt
from kit_field import pocket, shirt, strap
from paint import solid

META = {
    "name": "Scroll Bandolier",
    "gender": "unisex",
    "description": "Long-sleeved shirt with a diagonal bandolier of four capped scrolls and a belt.",
    "tags": ["shinobi", "chunin"],
}

TILT = (0, 0, -36)


def build(g):
    shirt(g, "P", 32160, texture="twill")
    strap(g, "bandolier", (0, 5.0, -2.75), TILT, length=15, width=2, seed=32163)
    strap(g, "bandolier_back", (0, 5.0, 2.75), (0, 0, 36), length=15, width=2, seed=32164)
    # Scrolls along the strap, at t * (sin 36, cos 36) from its centre.
    for i, t in enumerate((-4.4, -1.6, 1.2)):
        x, y = .588 * t, 5.0 + .809 * t
        scroll = g.piece(f"scroll_{i}", "TORSO", (-1.5, -.5, -1), (3, 1, 1), pivot=(x, y, -3.2), rotation=TILT)
        solid(scroll, "S", "plain", 32165 + i, 3, edge=False)
        for face in (scroll.front, scroll.back):
            face.set(0, 0, "A2"), face.set(2, 0, "A2")
        scroll.right.fill("A1"), scroll.left.fill("A1")
    pocket(g, "bandolier_pouch", (2.6, 8.0, -3.0), (3, 3, 2), "L", 32169, rotation=TILT, snap="M3")
    belt(g, "belt", y=9.6, role="K", buckle="M")
