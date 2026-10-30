#!/usr/bin/env python3
"""Hokage Residence: the round red building at the head of Main Street, under the Rock.

Drawn from the anime's establishing shots: red drums stepping in, each ringed by a wide skirt of orange
tiles; the top drum carries a white rim with curved white fins rising from it and, on its street face,
the white disc with the red fire kanji. A white tower with teal skirts and a spire stands to the west,
a small red drum to the east. Dark pilasters and small windows run round every drum.

Inside: the entrance hall (a red runner to the reception desk, benches, lanterns), the Hokage's office
on the middle floor with the big window over the village behind the desk, the scroll archive above.
The owner finishes the rooms by hand (KONOHA_BUILD.md, landmarks); the Mission Desk moves in at Beta 2.
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from kit import NS, ROOFS, Plan  # noqa: E402

W, H, D = 49, 36, 40
CX, CZ = 24, 18
WALL, PILASTER, PANE, RIM = "red_concrete", "red_nether_bricks", "gray_stained_glass_pane", "smooth_quartz"


def dist(x, z, cx=CX, cz=CZ):
    return math.hypot(x - cx, z - cz)


def disc(r, cx=CX, cz=CZ):
    k = int(r) + 1
    return {(x, z) for x in range(cx - k, cx + k + 1) for z in range(cz - k, cz + k + 1) if dist(x, z, cx, cz) <= r + .5}


def ring(r, cx=CX, cz=CZ):
    return disc(r, cx, cz) - disc(r - 1, cx, cz)


def sector(x, z, n=32, cx=CX, cz=CZ):
    return int((math.atan2(z - cz, x - cx) + math.pi) / (2 * math.pi) * n) % n


def drum(p, r, y0, y1, rows, wall=WALL, pilaster=PILASTER, cx=CX, cz=CZ):
    """A drum's wall from y0 to y1: a pilaster every eighth of the way round, small windows between them on the rows given."""
    for x, z in ring(r, cx, cz):
        s = sector(x, z, cx=cx, cz=cz)
        for y in range(y0, y1 + 1):
            if s % 4 == 0:
                p.set(x, y, z, pilaster)
            elif y in rows and s % 2 == 1:
                p.set(x, y, z, PANE)
            else:
                p.set(x, y, z, wall)


def skirt(p, r_in, r_out, y, style="orange", cx=CX, cz=CZ):
    """A ring of tile from r_out down at y, climbing half a block per block inwards to r_in: the anime's wide eaves."""
    r = ROOFS[style]
    for x, z in disc(r_out, cx, cz) - disc(r_in, cx, cz):
        k = max(0, int(r_out + .5 - dist(x, z, cx, cz)))
        p.set(x, y + k // 2, z, f"{r['slab']}[type={'bottom' if k % 2 == 0 else 'top'}]")
        if k > 1:
            for yy in range(y, y + k // 2):
                if p.get(x, yy, z) is None:
                    p.set(x, yy, z, r["full"])


def floor(p, r, y, block="spruce_planks"):
    for x, z in disc(r):
        p.set(x, y, z, block)


def fins(p, r, y):
    """The white fins on the top drum's rim: eight curved horns leaning out, between the pilasters."""
    for i in range(8):
        a = (i + .5) / 8 * 2 * math.pi
        for j, (dr, dy) in enumerate(((0, 0), (0, 1), (0, 2), (1, 3), (1, 4), (2, 5))):
            x, z = CX + round((r + dr) * math.cos(a)), CZ + round((r + dr) * math.sin(a))
            p.set(x, y + dy, z, RIM if j < 5 else "quartz_slab[type=bottom]")


def tower(p, cx, cz):
    """The white tower beside the drums: teal tile skirts at each stage and a spire."""
    for r, y0, y1, sk in ((4, 1, 9, 10), (3, 11, 17, 18), (2, 19, 23, 24)):
        drum(p, r, y0, y1, (3, 6, 13, 15, 21), wall="smooth_quartz", pilaster="calcite", cx=cx, cz=cz)
        skirt(p, r, r + 2, sk, "green", cx=cx, cz=cz)
    p.fill(cx, 25, cz, cx, 27, cz, "waxed_oxidized_cut_copper")
    p.set(cx, 28, cz, "lightning_rod")
    for x, z in disc(3, cx, cz):
        p.set(x, 1, z, "smooth_stone")


def build() -> Plan:
    p = Plan("hokage_residence", "Hokage Residence", (W, H, D), "landmark",
             "Exterior, hall, office and archive (Beta 1); the owner finishes the rooms; the Mission Desk at Beta 2")
    # the plaza
    p.fill(0, 0, 0, W - 1, 0, D - 1, "polished_andesite")
    for x in range(W):
        for z in range(D):
            if (x + z) % 2 and abs(x - CX) > 2:
                p.set(x, 0, z, "smooth_stone")
    p.fill(CX - 1, 0, CZ + 14, CX + 1, 0, D - 1, "stone_bricks")

    # the drums: base r14 (the hall, two storeys), middle r11 (the office), top r8 (the archive)
    for x, z in disc(14):
        p.set(x, 1, z, "polished_andesite")
    drum(p, 14, 1, 9, (3, 4, 7, 8))
    floor(p, 13, 6)
    skirt(p, 12, 17, 10)
    drum(p, 11, 10, 16, (12, 13, 14))
    floor(p, 10, 10)
    skirt(p, 9, 14, 17)
    drum(p, 8, 17, 25, (20, 21))
    floor(p, 7, 17)
    for x, z in disc(8):
        p.set(x, 26, z, "smooth_stone")
    for x, z in ring(8):
        p.set(x, 26, z, RIM)
        p.set(x, 27, z, "quartz_slab[type=bottom]")
    fins(p, 8, 27)
    p.water_tank(CX - 3, 27, CZ - 2)
    p.set(CX + 2, 27, CZ - 3, "lightning_rod")
    p.fire_sign(CX, 22, CZ + 9)

    # the wings: the white tower to the west, a small red drum with its own skirt to the east
    tower(p, 6, 9)
    for x, z in disc(4, 42, 9):
        p.set(x, 1, z, "polished_andesite")
    drum(p, 4, 1, 6, (3, 4), cx=42, cz=9)
    skirt(p, 0, 6, 7, cx=42, cz=9)

    # the entrance: a three-wide arch, lanterns, the name board above
    zf = CZ + 14
    p.clear(CX - 1, 2, zf, CX + 1, 4, zf)
    p.clear(CX - 1, 2, zf - 1, CX + 1, 4, zf - 1)
    for x in (CX - 2, CX + 2):
        p.fill(x, 2, zf + 1, x, 5, zf + 1, "stripped_dark_oak_log[axis=y]")
    p.fill(CX - 2, 6, zf + 1, CX + 2, 6, zf + 1, "dark_oak_planks")
    p.fill(CX - 1, 7, zf + 1, CX + 1, 7, zf + 1, "dark_oak_planks")
    for x in (CX - 4, CX + 4):
        p.set(x, 1, zf + 3, f"{NS}:stone_lantern[facing=south,half=lower]")
        p.set(x, 2, zf + 3, f"{NS}:stone_lantern[facing=south,half=upper]")
    for x in (4, W - 5):
        p.set(x, 1, D - 3, f"{NS}:mossy_stone_lantern[facing=south,half=lower]")
        p.set(x, 2, D - 3, f"{NS}:mossy_stone_lantern[facing=south,half=upper]")

    # the hall: a red runner to the reception desk, benches either side, lanterns, the stairs up the west side
    for z in range(CZ - 1, zf):
        p.set(CX, 2, z, "red_carpet")
    for x in range(CX - 5, CX + 6):
        p.set(x, 2, CZ - 3, "stripped_spruce_log[axis=x]")
        p.set(x, 3, CZ - 3, "spruce_slab[type=bottom]")
    p.set(CX, 3, CZ - 3, "lectern[facing=south]")
    for x in (CX - 6, CX - 5, CX + 5, CX + 6):
        for z in (CZ + 4, CZ + 8):
            p.set(x, 2, z, "spruce_stairs[facing=" + ("east" if x < CX else "west") + ",half=bottom]")
    for x, z in ((CX - 8, CZ), (CX + 8, CZ), (CX, CZ + 8), (CX - 8, CZ + 8), (CX + 8, CZ + 8), (CX, CZ - 8)):
        p.set(x, 5, z, f"{NS}:white_paper_lantern")
    for x, z in ((CX - 11, CZ + 6), (CX + 11, CZ + 6), (CX - 11, CZ - 6), (CX + 11, CZ - 6)):
        p.set(x, 2, z, "potted_azalea_bush")
    for i in range(4):
        p.set(CX - 10, 2 + i, CZ + 3 - i, "spruce_stairs[facing=north,half=bottom]")
        p.clear(CX - 10, 6, CZ + 3 - i, CX - 10, 6, CZ + 3 - i)
    for i in range(4):
        p.set(CX - 6, 7 + i, CZ - 4 + i, "spruce_stairs[facing=south,half=bottom]")
        p.clear(CX - 6, 10, CZ - 4 + i, CX - 6, 10, CZ - 4 + i)

    # the Hokage's office: the desk with its back to the big window over the village, shelves of paperwork
    for x in range(CX - 3, CX + 4):
        p.fill(x, 11, CZ + 11, x, 15, CZ + 11, PANE)
    p.fill(CX - 2, 11, CZ + 7, CX + 2, 11, CZ + 7, "dark_oak_planks")
    p.set(CX, 11, CZ + 8, "dark_oak_stairs[facing=south,half=bottom]")
    for x in (CX - 7, CX + 7):
        p.fill(x, 11, CZ - 3, x, 13, CZ + 3, "bookshelf")
    for x in (CX - 2, CX + 2):
        p.set(x, 12, CZ + 7, "white_carpet")
    p.set(CX, 15, CZ, f"{NS}:white_paper_lantern")
    for i in range(7):
        p.set(CX + 6, 11 + i, CZ + 3 - i, "spruce_stairs[facing=north,half=bottom]")
        p.clear(CX + 6, 17, CZ + 3 - i, CX + 6, 17, CZ + 3 - i)

    # the archive: shelves of scrolls round the top drum
    for x, z in ring(6):
        if sector(x, z) % 8 != 6:
            p.fill(x, 18, z, x, 20, z, "bookshelf")
    p.set(CX, 18, CZ, "lectern[facing=south]")
    p.set(CX, 23, CZ, f"{NS}:white_paper_lantern")

    p.marker("door_anchor", (CX, 1, D - 2))
    p.marker("anchor:hokage_office", (CX, 11, CZ + 4))
    p.cutaway = [9, 16]
    return p


if __name__ == "__main__":
    build().write()
