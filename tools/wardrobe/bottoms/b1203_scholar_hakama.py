"""Scholar's Hakama: wide pleated hakama to the ankle, the pleats pressed sharp in front, a stiff
back panel at the waist, worn over cream tabi socks with straw zori."""
from kit import flaps, side_panels
from paint import fabric, k, solid, strip_fabric

META = {"name": "Scholar's Hakama", "gender": "unisex",
        "description": "Wide pleated hakama to the ankle, a stiff back panel, cream tabi and straw zori.",
        "tags": ["shinobi", "hakama"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 12890, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 12890, 1)
    for side, bone in (("right", "RIGHT_LEG"), ("left", "LEFT_LEG")):
        leg = g.part(f"{side}_leg")
        strip_fabric(leg, "D", "twill", 12891, 2, 0, 9)
        fabric(leg.top, "D", "twill", 12891, 2)
        for x in range(0, leg.strip.w, 2):
            leg.strip.vline(x, 0, 9, k("D", 1))
        strip_fabric(leg, "S", "plain", 12892, 3, 10, 11)
        leg.bottom.fill("L2")
        leg.front.vline(1, 10, 11, "S2")
        pants = g.part(f"{side}_pants")
        for face in pants.sides:
            face.hline(0, face.w - 1, 11, "L3")
        pants.bottom.fill("L1")
        flare = g.piece(f"{side}_flare", bone, (-2.6, 1.0, -2.6), (5, 9, 5), inflate=.15)
        solid(flare, "D", "twill", 12893 + (side == "left"), 2)
        for f in flare.sides:
            for x in range(0, f.w, 2):
                f.vline(x, 0, 8, k("D", 1))
            f.hline(0, f.w - 1, 8, k("D", 3))
        flare.bottom.fill(k("D", 0))
    for face in flaps(g, "hakama", 4, "D", "twill", 12895, width=9, top=10.8, front_z=-2.8, back_z=1.8):
        for x in range(1, 9, 2):
            face.vline(x, 1, 3, k("D", 1))
    koshi = g.piece("koshi_ita", "TORSO", (-2.5, 0, 0), (5, 3, 1), pivot=(0, 9.0, 2.05))
    solid(koshi, "D", "twill", 12896, 3)
    koshi.back.hline(0, 4, 0, k("D", 4))
    side_panels(g, "hakama_side", 3, "D", "twill", top=10.8)
