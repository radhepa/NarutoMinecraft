"""Mountain Wrap: a long cloth thrown over the left shoulder and wound across the body to the right
hip, the way the mountain monks wear it, over a chain-mesh shirt; a broad sash at the waist and the
bare right arm wound in bandages to the shoulder."""
from kit import belt
from kit_shinobi import bandage, mesh
from paint import fabric, k, solid, strip_fabric

META = {
    "name": "Mountain Wrap",
    "gender": "unisex",
    "description": "Long cloth draped over the left shoulder across a mesh shirt, a broad sash, a bandaged right arm.",
    "tags": ["shinobi", "wrap", "jonin"],
}


def drape(face, cols, seed, base=2):
    """Paint the diagonal band of cloth: cols(y) gives the band's (x0, x1) on each row."""
    for y in range(face.h):
        span = cols(y)
        if span is None:
            continue
        x0, x1 = span
        for x in range(max(0, x0), min(face.w, x1 + 1)):
            s = base - (1 if (x + y) % 4 == 0 else 0)
            face.set(x, y, k("P", s))
        if 0 <= x0 < face.w:
            face.set(x0, y, k("P", base + 1))
        if 0 <= x1 < face.w:
            face.set(x1, y, k("P", base - 1))


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    mesh(body.strip, 0, 0, body.strip.w - 1, 9)
    mesh(body.top, 0, 0, body.top.w - 1, body.top.h - 1)
    body.front.hline(2, 5, 0, "K1")
    # Over the left shoulder and down to the right hip, front and back; the left side is covered.
    drape(jacket.front, lambda y: (6 - y // 2 * 1 - 2, 8) if y < 9 else None, 35140)
    drape(jacket.back, lambda y: (-1, 2 + y // 2) if y < 9 else None, 35141)
    drape(jacket.left, lambda y: (0, 3) if y < 9 else None, 35142)
    drape(jacket.top, lambda y: (5, 7), 35143, 3)
    for side in ("right", "left"):
        arm = g.part(f"{side}_arm")
        mesh(arm.strip, 0, 0, arm.strip.w - 1, 2)
        mesh(arm.top, 0, 0, arm.top.w - 1, arm.top.h - 1)
    right = g.part("right_arm")
    bandage(right.strip, 0, 3, right.strip.w - 1, 10)
    left = g.part("left_arm")
    bandage(left.strip, 0, 8, left.strip.w - 1, 10)
    shoulder = g.piece("shoulder_drape", "LEFT_ARM", (-1.4, -2.6, -2.6), (5, 4, 5), inflate=.05)
    solid(shoulder, "P", "weave", 35144, 2)
    for face in shoulder.sides:
        face.hline(0, face.w - 1, 0, "P3")
        for x in range(0, face.w, 2):
            face.set(x, 3, "P1")
    sash = belt(g, "broad_sash", y=8.8, role="A", height=2, buckle=None)
    sash.front.hline(0, sash.front.w - 1, 1, "A1")
    end = g.piece("sash_end", "TORSO", (-1, 0, 0), (2, 4, 1), pivot=(-2.4, 10.4, -2.9), rotation=(0, 0, 6), motion="flap_front")
    solid(end, "A", "weave", 35145, 2)
