"""Scholar's Robe: Unkai Kurama's teaching dress. A long, sober robe to the knee, the cream inner
collar showing at the throat, broad kimono sleeves edged in the clan accent, a dark sash knotted at
the side and the Kurama crest across the back."""
from kit import belt, flaps, side_panels
from kit_kurama import back_crest, kimono_sleeves, wrap_front
from paint import cap, solid, strip_fabric

META = {
    "name": "Scholar's Robe",
    "gender": "unisex",
    "description": "Long robe to the knee, cream inner collar, broad accent-edged sleeves, dark side-knotted sash, crest.",
    "tags": ["robe"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 12650, 2)
    cap(body, "P", texture="twill", seed=12650)
    f = body.front
    wrap_front(f, "S3", "S2", rows=8, start=1)
    f.set(0, 0, "S3")
    for face in (body.right, body.left):
        face.vline(1, 0, 11, "P1")
    sash = belt(g, "sash", y=7.6, role="D", height=2, buckle=None, inflate=.14)
    for face in sash.sides:
        face.hline(0, face.w - 1, 0, "D3")
    for i, (x, rz) in enumerate(((-3.4, -4), (-2.8, 8))):
        end = g.piece(f"sash_end_{i}", "TORSO", (-.5, 0, -.5), (1, 5 - i, 1), pivot=(x, 9.2, -2.8), rotation=(0, 0, rz),
                      motion="sway")
        solid(end, "D", "weave", 12651 + i, 2)
    for face in flaps(g, "robe", 8, "P", "twill", 12653, width=9, hem="A2", top=10.6, front_z=-2.8, back_z=1.8):
        face.vline(5, 1, 7, "S3")
    side_panels(g, "robe_side", 7, "P", "twill", hem="A2", top=10.6)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "S", "weave", 12655, 3, 9, 10)
    kimono_sleeves(g, "P", "twill", 12656, length=9, trim="A2")
    back_crest(g, role="P", ink="A2", texture="twill")
