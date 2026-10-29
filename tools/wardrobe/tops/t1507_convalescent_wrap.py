"""Convalescent Wrap: a calm village look after Hayate's own: a soft pale kimono top wrapped left
over right, a slate over-collar, a loose knitted shawl round the shoulders against the cough, and a
narrow sash."""
from kit import belt
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Convalescent Wrap",
    "gender": "unisex",
    "description": "Pale wrapped kimono top with a slate over-collar, a knitted shawl round the shoulders, a narrow sash.",
    "tags": ["robe"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "S", "weave", 15770, 2)
    cap(body, "S", seed=15770)
    f = body.front
    for i in range(8):
        x = 1 + i
        if x <= 7:
            f.set(x, i, "P2")
            if x + 1 <= 7:
                f.set(x + 1, i, "S1")
    f.set(0, 0, "P2")
    belt(g, "sash", y=8.6, role="P", buckle=None, height=1, inflate=.12)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 15772 + (side == "left"), 2, 0, 10)
        fabric(arm.top, "S", "weave", 15772, 3)
        arm.strip.hline(0, arm.strip.w - 1, 10, "S1")
    # The shawl: a knitted ring over the shoulders, lower in front, ends falling on the chest.
    shawl = g.piece("shawl", "TORSO", (-4.5, -.4, -2.6), (9, 2, 5), inflate=.3)
    solid(shawl, "D", "knit", 15774, 3, edge=False)
    for face in shawl.sides:
        face.hline(0, face.w - 1, 1, "D2")
    for i, (x, rz) in enumerate(((-2.4, 4), (2.4, -4))):
        end = g.piece(f"shawl_end_{i}", "TORSO", (-1, 0, 0), (2, 5, 1), pivot=(x, 1.2, -3.0), rotation=(0, 0, rz))
        solid(end, "D", "knit", 15776 + i, 3)
        end.front.hline(0, 1, 4, "D1")
