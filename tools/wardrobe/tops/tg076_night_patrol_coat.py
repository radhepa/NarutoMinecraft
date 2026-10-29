"""Night Patrol Coat: the village watch's hip-length coat, closed and belted, with a short rain
cape over the shoulders, the collar turned up and a small paper lantern hung from the belt for the
rounds of the sleeping streets."""
from kit import belt
from kit_aburame import high_collar
from paint import cap, k, solid, strip_fabric

META = {
    "name": "Night Patrol Coat",
    "gender": "unisex",
    "description": "Belted hip-length coat, short rain cape, turned-up collar, paper lantern on the belt.",
    "tags": ["shinobi", "coat", "chunin"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 34300, 2)
    cap(body, "P", texture="twill", seed=34300)
    body.front.vline(3, 0, 11, "P0"), body.front.vline(4, 0, 11, "P3")
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        strip_fabric(arm, "P", "twill", 34301 + (side == "left"), 2)
        arm.strip.hline(0, arm.strip.w - 1, 11, "P0")
    belt(g, "coat_belt", y=8.6, height=2)
    cape = g.piece("rain_cape", "TORSO", (-8.4, -.4, -2.8), (17, 3, 6), inflate=.12)
    solid(cape, "S", "smooth", 34303, 1)
    cape.top.fill("S2")
    for face in cape.sides:
        face.hline(0, face.w - 1, 0, "S2"), face.hline(0, face.w - 1, face.h - 1, "S0")
    cape.bottom.fill(k("S", 0))
    high_collar(g, "P", "twill", 34304, cover_mouth=False, front_top=-1.6, back_top=-3.0, flare=8)
    hook = g.piece("lantern_cord", "TORSO", (-.5, 0, -.5), (1, 1, 1), pivot=(3.0, 10.4, -2.9))
    solid(hook, "K", "plain", 34308, 2, edge=False)
    lantern = g.piece("lantern", "TORSO", (-1, 0, -1), (2, 3, 2), pivot=(3.0, 11.4, -3.1), motion="sway")
    solid(lantern, "A", "plain", 34309, 3, edge=False)
    for face in lantern.sides:
        face.hline(0, 1, 0, "K1"), face.hline(0, 1, 2, "K1"), face.set(0, 1, "A4")
