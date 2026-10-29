"""Prototype 16px item sprites for the Shinobi Modpack (ITEMS.md, "Item art").

The catalogue marks each item's art: sprite (authored here), tint:<base> (a palette swap of an authored sprite),
icon (a simple sprite still to draw), model, block, wardrobe, vanilla or vf. This tool authors the first sprites
as small programs instead of pixel strings: each shape is rasterised on the 16 x 16 grid (no antialiasing), then
shaded like VF's tools/item_sprites.py and vanilla items: light from the top left, a darker lower-right edge and a
dark outline, three tones per material.

    python tools/items/sprites.py            # write docs/renders/items/16px/*.png and the preview sheets
    python tools/items/sprites.py --check    # verify the committed renders match the programs
    python tools/items/sprites.py --list     # sprites and tints still to author, from the catalogue

Phase 0 copies the 16px files into Shinobi Life's and Shinobi Combat's textures.
"""
import io
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'docs/renders/items'
ITEMS = ROOT / 'data/items/items.json'

sys.path.insert(0, str(ROOT / 'tools'))
from output_checks import matches  # noqa: E402

# Three tones (light, mid, dark) and an outline per material.
MATERIALS = {
    'steel': ('d7dde3', 'a3adb8', '6e7886', '2b3038'),
    'steel_dark': ('8e98a4', '66707d', '474f5a', '22262c'),
    'wrap': ('d9c3a0', 'b49870', '7f6646', '3a2c1d'),
    'wrap_dark': ('6d5a44', '544434', '3c3024', '1e1812'),
    'paper': ('f6efd9', 'e4d8b6', 'c2b28a', '6b5f45'),
    'ink': ('3b3a46', '2a2933', '1b1a22', '0e0d12'),
    'red': ('e8705f', 'c8463a', '8f2c25', '45140f'),
    'bomb': ('6b6f78', '4d5059', '33353d', '16171b'),
    'fuse': ('e3c79a', 'c49a5c', '8a6a3e', '3e2e1a'),
    'spark': ('fff2b0', 'ffd257', 'f29a2e', '8a4a10'),
    'smoke': ('eef0f2', 'c9cdd2', 'a0a6ad', '6f757d'),
    'pill': ('a9b86a', '7f8f45', '58652e', '262c14'),
    'glass': ('d9edf0', 'a7c8d5', '749cae', '466779'),
    'cork': ('d9a274', 'bc7850', '7c4930', '3b2116'),
    'green_liquid': ('9ad08a', '5fa55a', '3e7848', '1f3d25'),
    'rice': ('ffffff', 'eeeae0', 'cfc9b8', '7d786b'),
    'nori': ('3d5a40', '2b4230', '1d2d21', '0d150f'),
    'pink': ('ffc4d6', 'f19ab6', 'c96a8c', '6e3247'),
    'white': ('ffffff', 'f2eee6', 'd5cfc2', '7e776a'),
    'matcha': ('b9d98a', '8dbb5a', '5f8a3a', '2d421b'),
    'stick': ('e3c99b', 'c9a46a', '93733f', '45351d'),
    'lacquer': ('d85a46', 'b23a2c', '7a2219', '3a0f0b'),
    'lacquer_black': ('4a3d3d', '332a2a', '221b1b', '0f0b0b'),
    'noodle': ('fbe6a2', 'f0cf6c', 'c9a33f', '6b551c'),
    'broth': ('e0a86a', 'c98a4a', '9a6430', '4a2e14'),
    'ceramic': ('f1ece0', 'd9d1bf', 'aea48e', '5e574a'),
    'tea': ('c4dc7c', '9ebd52', '6f8f34', '33441a'),
    'note': ('efe3c0', 'dccb98', 'b3a06c', '5c5034'),
    'note_ink': ('9a7a4a', '7a5a32', '5a4024', '2a1e10'),
    'scroll_paper': ('f8f0d8', 'eadbb4', 'c7b384', '6c5e40'),
    'scroll_rod': ('a15c3c', '7e4029', '58291a', '2a130c'),
    'string': ('e86a5a', 'c84a3a', '8e3026', '3e140f'),
    'navy': ('5a6a9a', '3e4c78', '2a3456', '12172a'),
    'plate': ('e9eef2', 'c3ccd5', '8e99a6', '3a414b'),
    'canvas': ('b8a27a', '96805a', '6c5a3e', '30281a'),
    'buckle': ('e6d38a', 'c9b25a', '8e7a34', '3e3414'),
    'chakra_paper': ('f4f1e8', 'e2ddcc', 'c4bda5', '6b6553'),
    'fiber': ('d8cdb0', 'c2b48e', 'a3946c', '5a4f36'),
    'cup': ('f4f0e6', 'e4dccb', 'bdb29a', '5f574a'),
    'label_red': ('f07a5e', 'd5523a', '9a3424', '44160f'),
    'fish': ('fde3e9', 'f7c9d3', 'd99aab', '6e3b48'),
    'fish_skin': ('9fb4c4', '6f8799', '4b5f70', '1f2a33'),
    'herb': ('9bc96a', '6fa047', '4b7430', '22361a'),
    'ladle': ('c9a46a', 'a8834c', '7a5c32', '3a2a14'),
    'frame': ('8e5a3a', '6e4229', '4e2d1b', '22130a'),
}


def hexrgb(h):
    return tuple(bytes.fromhex(h)) + (255,)


class Canvas:
    """A 16 x 16 grid of material labels; shapes paint labels, render() shades them."""

    def __init__(self):
        self.px = {}

    def put(self, x, y, mat):
        if 0 <= x < 16 and 0 <= y < 16:
            self.px[(x, y)] = mat

    def fill(self, test, mat):
        for y in range(16):
            for x in range(16):
                if test(x + 0.5, y + 0.5):
                    self.put(x, y, mat)

    def rect(self, x0, y0, x1, y1, mat):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                self.put(x, y, mat)

    def disc(self, cx, cy, r, mat):
        self.fill(lambda x, y: (x - cx) ** 2 + (y - cy) ** 2 <= r * r, mat)

    def line(self, x0, y0, x1, y1, mat, width=0.5):
        def near(x, y):
            dx, dy = x1 - x0, y1 - y0
            t = max(0, min(1, ((x - x0) * dx + (y - y0) * dy) / (dx * dx + dy * dy)))
            return math.hypot(x - (x0 + t * dx), y - (y0 + t * dy)) <= width
        self.fill(near, mat)

    def poly(self, points, mat):
        def inside(x, y):
            n, hit = len(points), False
            for i in range(n):
                (ax, ay), (bx, by) = points[i], points[(i + 1) % n]
                if (ay > y) != (by > y) and x < (bx - ax) * (y - ay) / (by - ay) + ax:
                    hit = not hit
            return hit
        self.fill(inside, mat)

    def render(self, outline=True):
        img = Image.new('RGBA', (16, 16))
        for (x, y), mat in self.px.items():
            light, mid, dark, _ = MATERIALS[mat]
            up = self.px.get((x, y - 1)) == mat and self.px.get((x - 1, y)) == mat
            down = self.px.get((x, y + 1)) == mat and self.px.get((x + 1, y)) == mat
            tone = mid if up and down else (light if not up and down else dark if not down else mid)
            img.putpixel((x, y), hexrgb(tone))
        if outline:
            for y in range(16):
                for x in range(16):
                    if (x, y) in self.px:
                        continue
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        m = self.px.get((x + dx, y + dy))
                        if m:
                            img.putpixel((x, y), hexrgb(MATERIALS[m][3]))
                            break
        return img


def along(x0, y0, x1, y1):
    """Coordinates (t, s) along the axis from (x0, y0) to (x1, y1): t in blocks along it, s across it."""
    length = math.hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / length, (y1 - y0) / length

    def f(x, y):
        dx, dy = x - x0, y - y0
        return dx * ux + dy * uy, -dx * uy + dy * ux
    return f, length


# -- the sprites ---------------------------------------------------------------------------------------------------

def kunai(steel='steel', wrap='wrap'):
    c = Canvas()
    f, length = along(3.4, 12.6, 14.6, 1.4)

    def blade(x, y):
        t, s = f(x, y)
        if not 6.6 <= t <= length:
            return False
        w = 0.9 + 2.3 * (t - 6.6) / 3.0 if t < 9.6 else 3.2 * (length - t) / (length - 9.6)
        return abs(s) <= max(w, 0.5)
    c.fill(lambda x, y: (lambda t, s: 2.2 <= t <= 6.4 and abs(s) <= 0.8)(*f(x, y)), wrap)
    c.fill(lambda x, y: (lambda t, s: 2.2 <= t <= 6.4 and abs(s) <= 0.8 and int(t * 1.4) % 2 == 0)(*f(x, y)), 'wrap_dark')
    c.fill(lambda x, y: (lambda t, s: 6.0 <= t <= 7.0 and abs(s) <= 1.9)(*f(x, y)), 'steel_dark')
    c.fill(blade, steel)
    c.fill(lambda x, y: (lambda t, s: 0.8 <= math.hypot(t + 0.2, s) <= 2.0)(*f(x, y)), 'steel_dark')
    return c.render()


def shuriken(steel='steel'):
    """A four-point star: points up, down and to the sides, straight edges to a small waist, a hole."""
    c = Canvas()
    points = []
    for k in range(8):
        a = math.pi / 4 * k
        r = 7.6 if k % 2 == 0 else 2.9
        points.append((8 + r * math.cos(a), 8 + r * math.sin(a)))
    c.poly(points, steel)
    c.fill(lambda x, y: math.hypot(x - 8, y - 8) <= 1.9, 'steel_dark')
    for x, y in ((7, 7), (8, 7), (7, 8), (8, 8)):
        c.px.pop((x, y), None)
    return c.render()


def senbon():
    c = Canvas()
    for off in (-2.2, 0, 2.2):
        c.line(3 + off, 13 - 0.0 + off * 0.2, 13 + off, 3 + off * 0.2, 'steel', 0.42)
    return c.render()


def smoke_bomb(body='bomb'):
    c = Canvas()
    c.disc(7.5, 9.5, 4.9, body)
    c.rect(7, 3, 8, 4, 'fuse')
    c.put(9, 2, 'fuse')
    c.put(10, 1, 'spark')
    c.disc(12.6, 3.2, 1.6, 'smoke')
    return c.render()


def tag(marks='red', paper='paper'):
    c = Canvas()
    c.rect(5, 1, 10, 14, paper)
    for y in range(3, 13):
        if y % 3 != 1:
            c.put(7, y, marks)
            c.put(8, y, marks)
    c.rect(6, 6, 9, 6, marks)
    c.rect(6, 10, 9, 10, marks)
    return c.render()


def pill(mat='pill'):
    c = Canvas()
    c.disc(4.8, 10.8, 2.7, mat)
    c.disc(11.0, 10.8, 2.7, mat)
    c.disc(8.0, 5.0, 2.7, mat)
    return c.render()


def vial(liquid='green_liquid'):
    c = Canvas()
    c.rect(6, 2, 9, 3, 'cork')
    c.rect(6, 4, 9, 5, 'glass')
    c.fill(lambda x, y: (x - 8) ** 2 / 4.6 ** 2 + (y - 10.5) ** 2 / 4.2 ** 2 <= 1, 'glass')
    c.fill(lambda x, y: (x - 8) ** 2 / 3.6 ** 2 + (y - 11.2) ** 2 / 3.2 ** 2 <= 1 and y > 9.2, liquid)
    return c.render()


def onigiri(filling=None):
    c = Canvas()
    c.poly([(8, 1.5), (14.6, 13.2), (1.4, 13.2)], 'rice')
    c.rect(4, 10, 11, 13, 'nori')
    if filling:
        c.rect(7, 6, 8, 7, filling)
    return c.render()


def dango(colours=('pink', 'white', 'matcha')):
    c = Canvas()
    c.line(2, 14, 14, 2, 'stick', 0.5)
    for (cx, cy), mat in zip(((5.2, 10.8), (8, 8), (10.8, 5.2)), colours):
        c.disc(cx, cy, 2.4, mat)
    return c.render()


def ramen(broth='broth', bowl='lacquer'):
    c = Canvas()
    c.fill(lambda x, y: y >= 8 and (x - 8) ** 2 / 7.2 ** 2 + (y - 8) ** 2 / 6.2 ** 2 <= 1, bowl)
    c.rect(1, 6, 14, 8, broth)
    for x in range(2, 14, 3):
        c.rect(x, 6, x + 1, 7, 'noodle')
    c.disc(10.5, 6.0, 1.5, 'fish')
    c.put(10, 6, 'pink')
    c.rect(3, 4, 4, 6, 'nori')
    c.rect(4, 13, 11, 14, 'lacquer_black')
    return c.render()


def teacup(tea='tea'):
    c = Canvas()
    c.fill(lambda x, y: 5 <= y <= 13 and abs(x - 8) <= 5.2 - (y - 5) * 0.12, 'ceramic')
    c.rect(3, 5, 12, 6, tea)
    c.rect(4, 14, 11, 14, 'ceramic')
    return c.render()


def ryo_note(ink='note_ink', paper='note'):
    c = Canvas()
    c.rect(1, 4, 14, 11, paper)
    c.rect(2, 5, 13, 5, ink)
    c.rect(2, 10, 13, 10, ink)
    c.disc(7.5, 7.5, 1.6, ink)
    c.rect(11, 7, 12, 8, ink)
    c.rect(3, 7, 4, 8, ink)
    return c.render()


def scroll(paper='scroll_paper', rod='scroll_rod', string='string'):
    c = Canvas()
    c.rect(3, 4, 12, 11, paper)
    c.rect(1, 3, 2, 12, rod)
    c.rect(13, 3, 14, 12, rod)
    c.rect(7, 4, 8, 11, string)
    return c.render()


def forehead_protector():
    c = Canvas()
    c.rect(0, 6, 15, 10, 'navy')
    c.rect(3, 4, 12, 12, 'plate')
    for x, y in ((6, 9), (7, 9), (8, 8), (8, 7), (7, 6), (6, 7), (9, 9), (10, 8)):
        c.put(x, y, 'steel_dark')
    return c.render()


def ingot(mat='steel'):
    c = Canvas()
    c.poly([(3, 6.5), (13, 6.5), (15, 11.5), (1, 11.5)], mat)
    return c.render()


def chakra_paper():
    c = Canvas()
    c.rect(2, 2, 13, 13, 'chakra_paper')
    for x, y in ((4, 4), (9, 3), (6, 7), (11, 9), (4, 11), (8, 12), (12, 5)):
        c.put(x, y, 'fiber')
    return c.render()


def pouch(mat='canvas'):
    c = Canvas()
    c.fill(lambda x, y: 4 <= y <= 14 and (abs(x - 8) <= 5.5 if y < 12 else (x - 8) ** 2 / 5.5 ** 2 + (y - 11.5) ** 2 / 3 ** 2 <= 1), mat)
    c.rect(3, 4, 12, 7, 'wrap_dark')
    c.rect(7, 7, 8, 8, 'buckle')
    c.rect(5, 2, 10, 3, 'wrap_dark')
    return c.render()


def instant_ramen():
    c = Canvas()
    c.fill(lambda x, y: 3 <= y <= 14 and abs(x - 8) <= 4.2 + (y - 3) * 0.12 * -1 + 1.2, 'cup')
    c.rect(3, 6, 12, 9, 'label_red')
    c.rect(2, 2, 13, 3, 'white')
    return c.render()


def grilled_fish():
    c = Canvas()
    c.fill(lambda x, y: (x - 7.5) ** 2 / 5.6 ** 2 + (y - 8) ** 2 / 2.6 ** 2 <= 1, 'fish_skin')
    c.poly([(12, 8), (15, 5), (15, 11)], 'fish_skin')
    for x in (5, 8, 11):
        c.rect(x, 7, x, 9, 'steel_dark')
    c.put(3, 7, 'ink')
    c.line(1, 12, 13, 12, 'stick', 0.45)
    return c.render()


def charm(mat='red'):
    c = Canvas()
    c.rect(5, 4, 10, 13, mat)
    c.rect(6, 6, 9, 9, 'buckle')
    c.rect(7, 1, 8, 3, 'string')
    return c.render()


def headband():
    c = Canvas()
    c.rect(0, 6, 15, 9, 'white')
    c.rect(11, 10, 12, 14, 'white')
    c.rect(13, 10, 14, 13, 'white')
    return c.render()


def flak_vest():
    c = Canvas()
    c.poly([(3, 2), (6, 2), (8, 5), (10, 2), (13, 2), (14, 14), (2, 14)], 'herb')
    c.rect(4, 9, 6, 11, 'matcha')
    c.rect(10, 9, 12, 11, 'matcha')
    c.rect(7, 6, 8, 14, 'nori')
    return c.render()


def framed_ladle():
    c = Canvas()
    c.rect(1, 1, 14, 14, 'frame')
    c.rect(3, 3, 12, 12, 'paper')
    c.line(5, 4, 9, 9, 'ladle', 0.5)
    c.disc(10, 10, 1.8, 'ladle')
    return c.render()


def rice():
    c = Canvas()
    c.fill(lambda x, y: y >= 6 and (x - 8) ** 2 / 6 ** 2 + (y - 9) ** 2 / 5 ** 2 <= 1, 'fiber')
    c.fill(lambda x, y: (x - 8) ** 2 / 4.5 ** 2 + (y - 5.5) ** 2 / 2.5 ** 2 <= 1, 'rice')
    c.rect(6, 12, 9, 12, 'string')
    return c.render()


SPRITES = {
    'kunai': kunai, 'shuriken': shuriken, 'senbon': senbon, 'smoke_bomb': smoke_bomb,
    'paper_bomb': lambda: tag('red'), 'sealing_tag': lambda: tag('ink'), 'ninja_wire': None,
    'soldier_pill': pill, 'antidote': vial, 'onigiri': onigiri, 'dango': dango, 'miso_ramen': ramen,
    'green_tea': teacup, 'ryo_1': ryo_note, 'technique_scroll': scroll,
    'sealing_scroll': lambda: scroll('scroll_paper', 'lacquer_black', 'navy'),
    'forehead_protector': forehead_protector, 'steel_ingot': ingot, 'chakra_paper': chakra_paper,
    'tool_pouch': pouch, 'instant_ramen': instant_ramen, 'grilled_fish': grilled_fish, 'luck_charm': charm,
    'training_headband': headband, 'flak_vest': flak_vest, 'keepsake_framed_ladle': framed_ladle, 'rice': rice,
}
# Palette swaps of authored sprites (the catalogue's tint:<base> art), as the base's program with other materials.
TINTS = {
    'practice_kunai': lambda: kunai('stick', 'wrap'),
    'rusty_kunai': lambda: kunai('cork', 'wrap_dark'),
    'chakra_metal_kunai': lambda: kunai('glass', 'navy'),
    'practice_shuriken': lambda: shuriken('stick'),
    'manji_shuriken': lambda: shuriken('steel_dark'),
    'flash_bomb': lambda: smoke_bomb('white'),
    'stink_bomb': lambda: smoke_bomb('herb'),
    'food_pill': lambda: pill('rice'),
    'blood_pill': lambda: pill('red'),
    'eye_drops': lambda: vial('glass'),
    'coating_venom': lambda: vial('matcha'),
    'onigiri_umeboshi': lambda: onigiri('red'),
    'onigiri_salmon': lambda: onigiri('fish'),
    'shoyu_ramen': lambda: ramen('scroll_rod'),
    'tonkotsu_ramen': lambda: ramen('ceramic'),
    'mitarashi_dango': lambda: dango(('broth', 'broth', 'broth')),
    'matcha': lambda: teacup('matcha'),
    'ryo_10': lambda: ryo_note('matcha', 'note'),
    'ryo_100': lambda: ryo_note('navy', 'note'),
    'ryo_1000': lambda: ryo_note('lacquer', 'buckle'),
    'blank_scroll': lambda: scroll('scroll_paper', 'stick', 'stick'),
    'study_charm': lambda: charm('navy'),
    'safety_charm': lambda: charm('herb'),
    'refined_steel': lambda: ingot('glass'),
    'scrap_steel': lambda: ingot('steel_dark'),
    'tool_pouch_large': lambda: pouch('wrap'),
}


def build():
    out = {}
    for name, program in list(SPRITES.items()) + list(TINTS.items()):
        if program:
            out[name] = program()
    return out


def sheet(images, title_scale=8, columns=8):
    names = list(images)
    cell = 16 * title_scale
    rows = (len(names) + columns - 1) // columns
    img = Image.new('RGBA', (columns * (cell + 16) + 16, rows * (cell + 40) + 16), (36, 38, 46, 255))
    draw = ImageDraw.Draw(img)
    for i, name in enumerate(names):
        x, y = 16 + (i % columns) * (cell + 16), 16 + (i // columns) * (cell + 40)
        draw.rectangle([x - 2, y - 2, x + cell + 1, y + cell + 1], fill=(52, 55, 66, 255))
        img.alpha_composite(images[name].resize((cell, cell), Image.NEAREST), (x, y))
        draw.text((x, y + cell + 6), name, fill=(225, 225, 230, 255))
    return img


def png_bytes(img):
    buf = io.BytesIO()
    img.save(buf, 'PNG', optimize=False)
    return buf.getvalue()


def main(argv):
    images = build()
    files = {f'16px/{name}.png': png_bytes(img) for name, img in images.items()}
    files['sprites.png'] = png_bytes(sheet({k: v for k, v in images.items() if k in SPRITES}))
    files['tints.png'] = png_bytes(sheet({k: v for k, v in images.items() if k in TINTS}))
    if '--list' in argv:
        items = json.loads(ITEMS.read_text(encoding='utf-8'))['items']
        todo = [i['id'] for i in items if i['art'] in ('sprite',) and i['id'] not in images]
        tints = [i['id'] for i in items if i['art'].startswith('tint:') and i['id'] not in images]
        icons = [i['id'] for i in items if i['art'] == 'icon']
        print(f'{len(images)} authored ({len(SPRITES) - list(SPRITES.values()).count(None)} sprites, {len(TINTS)} tints)')
        print(f'sprites to author: {len(todo)}: ' + ', '.join(todo))
        print(f'tints to author: {len(tints)}')
        print(f'icons to draw: {len(icons)}')
        return 0
    if '--check' in argv:
        stale = [p for p, data in files.items() if not matches(OUT / p, data)]
        if stale:
            print('stale (rerun python tools/items/sprites.py): ' + ', '.join(stale))
            return 1
        print(f'ok: {len(images)} sprites')
        return 0
    (OUT / '16px').mkdir(parents=True, exist_ok=True)
    for path, data in files.items():
        (OUT / path).write_bytes(data)
    print(f'wrote {len(images)} sprites and 2 sheets to {OUT.relative_to(ROOT)}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
