"""Crow Mesh Shirt: a sleeveless dark high-collared shirt over a chain-mesh undershirt that runs down
both arms to the wrists, the crest on the back and a dark cord at the waist."""
from kit import belt
from kit_uchiha import back_crest, high_collar
from paint import cap, fabric, strip_fabric

META = {
    "name": "Crow Mesh Shirt",
    "gender": "unisex",
    "description": "Sleeveless dark high-collared shirt over chain mesh to the wrists, crest on the back.",
    "tags": ["shinobi", "uchiha"],
}


def fine_mesh(face, x0, y0, x1, y1):
    """Close-knit chain mesh: dark links in a diagonal check, read as a fine net at this scale."""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            face.set(x, y, "K2" if (x + y) % 2 else "K1")


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "weave", 3875, 2)
    cap(body, "P", seed=3875)
    f = body.front
    f.vline(2, 2, 9, "P1")
    # A short open neck showing the mesh.
    fine_mesh(f, 3, 0, 4, 1)
    for side in (body.right, body.left):
        side.vline(0, 0, 11, "P1"), side.vline(side.w - 1, 0, 11, "P1")
    back_crest(g, "P", seed=3876)
    high_collar(g, "P", seed=3877, height=3, flare=5)
    belt(g, "cord", y=9.6, role="K", height=1, buckle=None, inflate=.08)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        # The shirt's armhole edge, then mesh to the wrist.
        fabric(arm.top, "P", "weave", 3879, 2)
        arm.strip.hline(0, arm.strip.w - 1, 0, "P2")
        arm.strip.hline(0, arm.strip.w - 1, 1, "P1")
        fine_mesh(arm.strip, 0, 2, arm.strip.w - 1, 10)
        arm.strip.hline(0, arm.strip.w - 1, 10, "K2")
