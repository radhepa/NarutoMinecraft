"""Gambler Haori: Tsunade's look. A long green haori to the knee with full sleeves, worn open over a
grey wrapped blouse and a dark blue obi, with 賭 ("gamble") in a red circle on the back."""
from kit import belt
from paint import cap, fabric, solid, strip_fabric

META = {
    "name": "Gambler Haori",
    "gender": "unisex",
    "description": "Long open green haori with full sleeves over a grey wrapped blouse and dark blue obi, 賭 in a red circle on the back.",
    "tags": ["shinobi", "senju", "robe"],
    "covers_waist": True,
}

# 賭 ("gamble") in a red circle, drawn at double resolution: the 貝 radical on the left, 者 on the right.
GAMBLE = ["....######....",
          "..##......##..",
          ".#..........#.",
          ".#.###.#....#.",
          "#..#.#.####..#",
          "#..###..#.#..#",
          "#..#.#.#####.#",
          "#..###...#...#",
          "#..#.#..####.#",
          "#..###..#..#.#",
          ".#.#.#..#####.",
          ".##...#.#..##.",
          "..##......##..",
          "....######...."]


def build(g):
    body, jacket = g.part("body"), g.part("jacket")
    strip_fabric(body, "S", "weave", 1570, 2)
    cap(body, "S", seed=1570)
    f = body.front
    for i in range(7):
        f.set(2 + i * 4 // 7, i, "S1")
    belt(g, "obi", y=7.8, role="D", height=2, buckle=None, inflate=.1)
    strip_fabric(jacket, "P", "weave", 1571, 2)
    cap(jacket, "P", seed=1571)
    for y in range(12):
        for x in range(2, 6):
            jacket.front.clear(x, y)
        jacket.front.set(1, y, "P3"), jacket.front.set(6, y, "P1")
    for name, x in (("right", -3.6), ("left", 2.6)):
        lapel = g.piece(f"lapel_{name}", "TORSO", (0, 0, 0), (1, 12, 1), pivot=(x, -.6, -2.75))
        solid(lapel, "P", "weave", 1572, 2)
    back = g.piece("back_mark", "TORSO", (-7, 0, 0), (14, 14, 1), pivot=(0, 1.2, 2.3), scale=(.5, .5, .5))
    for face in back.faces:
        fabric(face, "P", "weave", 1573, 2)
    ring = {(x, y) for y, row in enumerate(GAMBLE) for x, ch in enumerate(row) if ch == "#" and
            ((x - 6.5) ** 2 + (y - 6.5) ** 2) ** .5 > 5.2}
    for y, row in enumerate(GAMBLE):
        for x, ch in enumerate(row):
            if ch == "#":
                back.back.set(13 - x, y, "A2" if (x, y) in ring else "K2")
    for side in ("right", "left"):
        arm, sleeve = g.part(f"{side}_arm"), g.part(f"{side}_sleeve")
        strip_fabric(arm, "S", "weave", 1574, 2, 0, 10)
        fabric(arm.top, "S", "weave", 1574, 3)
        strip_fabric(sleeve, "P", "weave", 1575 + (side == "left"), 2, 0, 9)
        fabric(sleeve.top, "P", "weave", 1575, 3)
        sleeve.strip.hline(0, sleeve.strip.w - 1, 9, "P1")
    for name, x0, w, z, motion in (("skirt_front_right", -4.6, 3, -2.95, "flap_front"),
                                   ("skirt_front_left", 1.6, 3, -2.95, "flap_front"),
                                   ("skirt_back", -4.6, 9, 1.95, "flap_back")):
        skirt = g.piece(name, "TORSO", (0, 0, 0), (w, 9, 1), pivot=(x0, 11.4, z), motion=motion)
        solid(skirt, "P", "weave", 1577 + len(name) % 3, 2)
    for name, x in (("skirt_right", -5.05), ("skirt_left", 4.05)):
        panel = g.piece(name, "TORSO", (0, 0, -2), (1, 8, 4), pivot=(x, 11.4, 0))
        solid(panel, "P", "weave", 1580, 2)
