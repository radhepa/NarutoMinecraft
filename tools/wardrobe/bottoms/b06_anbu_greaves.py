"""ANBU Greaves: close black trousers, white shin guards strapped from knee to ankle with a steel
stud, and open-toe sandals."""
from kit_shinobi import sandals
from paint import fabric, strip_fabric

META = {"name": "ANBU Greaves", "gender": "unisex",
        "description": "Black trousers, white strapped shin guards, open-toe sandals.", "tags": ["shinobi", "armor"]}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "twill", 231, 2, 9, 11)
    fabric(body.bottom, "D", "twill", 231, 1)
    for side in ("right", "left"):
        leg, pants = g.part(f"{side}_leg"), g.part(f"{side}_pants")
        strip_fabric(leg, "D", "twill", 232 + (side == "left"), 2, 0, 9)
        fabric(leg.top, "D", "twill", 232, 2)
        # Shin guard on the front and sides of the pants layer, two black straps across it.
        for face in (pants.front, pants.right, pants.left):
            fabric(face, "S", "plain", 234, 2, 0, 5, face.w, 5)
            face.hline(0, face.w - 1, 5, "S4")
            face.hline(0, face.w - 1, 6, "K1"), face.hline(0, face.w - 1, 9, "K1")
        pants.front.set(1, 7, "M3"), pants.front.set(2, 7, "M3")
        fabric(pants.back, "K", "smooth", 235, 2, 0, 6, pants.back.w, 1)
        fabric(pants.back, "K", "smooth", 235, 2, 0, 9, pants.back.w, 1)
    sandals(g)
