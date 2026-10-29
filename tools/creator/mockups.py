"""Mock-ups of the creator's screens (CHARACTER_CREATION.md, "Screens"), drawn with PIL around real wardrobe renders:
the character preview, the hair and outfit thumbnails and the clan looks are the actual pieces, rendered the way
preview.py draws the player. Layout only: the game draws these with Minecraft's GUI widgets at any GUI scale.

    python3 tools/creator/creator.py --mockups    # docs/renders/creator/screen_*.png
"""
from __future__ import annotations

import numpy as np
from PIL import Image, ImageDraw

import creator as C
import preview as P
import render as R
import wardrobe as W

OUT = P.OUT
SS = R.SS
SW, SH = 1600, 900
INK, SOFT, FAINT = (52, 34, 26), (112, 86, 66), (170, 146, 120)
PAPER, PANEL, PANEL2 = (246, 236, 216), (236, 222, 196), (226, 208, 178)
ACCENT, ACCENT_SOFT = (178, 58, 44), (232, 190, 160)
LOCK = (120, 104, 96)
STEPS = ["Name", "Body", "Hair", "Face", "Outfit", "Roots", "Review"]


def font(size, bold=False):
    return R.font(size, bold)


class Screen:
    def __init__(self, title: str, step: int | None, mode: str = "Varied"):
        self.img = Image.new("RGB", (SW, SH), PAPER)
        self.d = ImageDraw.Draw(self.img)
        self.mode = mode
        d = self.d
        # Header: the opening's framing card, neutral.
        d.rectangle((0, 0, SW, 64), fill=(44, 30, 24))
        d.text((28, 16), "Shinobi Modpack", font=font(26, True), fill=(240, 222, 190))
        d.text((300, 22), title, font=font(20), fill=(214, 190, 160))
        badge = f"{mode} world"
        tw = d.textlength(badge, font=font(16))
        d.rounded_rectangle((SW - tw - 56, 18, SW - 24, 46), 12, fill=(92, 64, 48))
        d.text((SW - tw - 40, 22), badge, font=font(16), fill=(240, 222, 190))
        if step is not None:
            self.rail(step)

    def rail(self, current: int):
        d = self.d
        d.rectangle((0, 64, 220, SH), fill=PANEL)
        for i, s in enumerate(STEPS):
            y = 96 + i * 62
            on = i == current
            done = i < current
            if on:
                d.rounded_rectangle((12, y - 10, 208, y + 38), 10, fill=PAPER, outline=ACCENT, width=2)
            d.ellipse((24, y, 52, y + 28), fill=ACCENT if on else (INK if done else PANEL2))
            d.text((38 - d.textlength(str(i + 1), font=font(15, True)) / 2, y + 5), str(i + 1), font=font(15, True),
                   fill=PAPER if (on or done) else SOFT)
            d.text((64, y + 3), s, font=font(20, on), fill=INK if on or done else SOFT)
        d.text((24, SH - 70), "Esc: back to world options", font=font(13), fill=SOFT)

    def footer(self, next_label="Next", dice=True, back=True):
        d = self.d
        d.rectangle((220, SH - 72, SW, SH), fill=PANEL)
        if back:
            self.button((244, SH - 56, 384, SH - 16), "Back")
        if dice and self.mode == "Varied":
            self.button((404, SH - 56, 640, SH - 16), "Roll a life", icon="dice")
        self.button((SW - 220, SH - 56, SW - 24, SH - 16), next_label, primary=True)

    def button(self, box, label, primary=False, icon=None, small=False):
        d = self.d
        d.rounded_rectangle(box, 8, fill=ACCENT if primary else PAPER, outline=INK if not primary else ACCENT, width=2)
        f = font(15 if small else 18, True)
        x0, y0, x1, y1 = box
        tw = d.textlength(label, font=f) + (26 if icon else 0)
        x = (x0 + x1 - tw) / 2
        if icon == "dice":
            die(d, x, (y0 + y1) / 2 - 9, 18)
            x += 26
        d.text((x, (y0 + y1) / 2 - (9 if small else 11)), label, font=f, fill=PAPER if primary else INK)

    def heading(self, x, y, text, sub=None, size=22):
        self.d.text((x, y), text, font=font(size, True), fill=INK)
        if sub:
            self.d.text((x, y + size + 8), sub, font=font(15), fill=SOFT)

    def lock(self, x, y, label="locked after creation"):
        d = self.d
        d.rounded_rectangle((x, y + 6, x + 12, y + 16), 2, fill=LOCK)
        d.arc((x + 2, y, x + 10, y + 10), 180, 360, fill=LOCK, width=2)
        d.text((x + 18, y + 1), label, font=font(13), fill=LOCK)

    def changeable(self, x, y, label):
        d = self.d
        d.ellipse((x, y + 3, x + 12, y + 15), outline=(80, 128, 80), width=2)
        d.text((x + 18, y + 1), label, font=font(13), fill=(70, 110, 70))

    def save(self, name: str):
        out = OUT / f"screen_{name}.png"
        self.img.save(out)
        print(out)


def die(d, x, y, s):
    d.rounded_rectangle((x, y, x + s, y + s), 4, fill=PAPER, outline=INK, width=2)
    for px, py in ((.3, .3), (.7, .7), (.5, .5), (.7, .3), (.3, .7)):
        d.ellipse((x + px * s - 2, y + py * s - 2, x + px * s + 2, y + py * s + 2), fill=INK)


def wrap(d, text, f, width):
    words, lines, line = text.split(), [], ""
    for w in words:
        t = (line + " " + w).strip()
        if d.textlength(t, font=f) > width and line:
            lines.append(line)
            line = w
        else:
            line = t
    if line:
        lines.append(line)
    return lines


def paragraph(d, x, y, text, width, size=16, fill=INK, gap=6, bold=False):
    f = font(size, bold)
    for line in wrap(d, text, f, width):
        d.text((x, y), line, font=f, fill=fill)
        y += size + gap
    return y


# -- real renders ------------------------------------------------------------------------------------------------
def character_image(world, spec, w, h, stage="child", yaw=-24, unit=None, heads=False, bg=(240, 228, 204), bg2=(222, 202, 166)):
    """A rendered player (or head) on its own backdrop, as a PIL image of w x h."""
    ww, hh = w * SS, h * SS
    back = R.backdrop(ww, hh, bg, bg2)
    ch = R.Character(spec, world.garments)
    s, head = P.stage_scale(world.data, stage)
    if heads:
        unit = unit or min(h / 15.5, w / 15.5)
        canvas = R.Canvas(ww, hh, back)
        P.render_player(canvas, ch, ww / 2, hh * .97, unit * SS, yaw, 8, head=1.0)
    else:
        unit = unit or min(h / 38, w / 17.5)
        feet = hh * .93
        R.ground_shadow(back, ww / 2, feet + 2 * SS, unit * 6 * SS, unit * SS)
        canvas = R.Canvas(ww, hh, back)
        P.draw_player(canvas, ch, ww / 2, feet, unit * SS, world.data, stage, yaw)
    img = Image.fromarray(canvas.img.clip(0, 255).astype(np.uint8)).resize((w, h), Image.LANCZOS)
    return img


def preview_panel(scr, world, spec, box, stage="child", caption=True):
    x0, y0, x1, y1 = box
    d = scr.d
    d.rounded_rectangle(box, 14, fill=PANEL2)
    img = character_image(world, spec, x1 - x0 - 24, y1 - y0 - 96, stage)
    scr.img.paste(img, (x0 + 12, y0 + 12))
    # Rotate arrows and the stage toggle.
    cy = y1 - 64
    for x, t in ((x0 + 22, "<"), (x1 - 62, ">")):
        d.rounded_rectangle((x, cy, x + 40, cy + 40), 8, fill=PAPER, outline=INK, width=2)
        d.text((x + 13, cy + 7), t, font=font(20, True), fill=INK)
    mid = (x0 + x1) / 2
    for i, (label, on) in enumerate((("Now", stage == "child"), ("Grown", stage != "child"))):
        bx = mid - 100 + i * 100
        d.rounded_rectangle((bx, cy + 4, bx + 96, cy + 36), 8, fill=INK if on else PAPER, outline=INK, width=2)
        d.text((bx + 48 - d.textlength(label, font=font(15, True)) / 2, cy + 11), label, font=font(15, True), fill=PAPER if on else INK)
    if caption:
        d.text((x0 + 16, y0 + 14), "drag to turn", font=font(13), fill=SOFT)


def swatch_row(scr, x, y, colors, selected, size=36, gap=10, per_row=10, labels=None):
    d = scr.d
    for i, c in enumerate(colors):
        cx, cy = x + (i % per_row) * (size + gap), y + (i // per_row) * (size + gap + (16 if labels else 0))
        d.rounded_rectangle((cx, cy, cx + size, cy + size), 8, fill=c, outline=INK if i == selected else FAINT, width=3 if i == selected else 1)
        if labels:
            t = labels[i]
            d.text((cx + size / 2 - d.textlength(t, font=font(11)) / 2, cy + size + 2), t, font=font(11), fill=SOFT)
    rows = (len(colors) + per_row - 1) // per_row
    return y + rows * (size + gap + (16 if labels else 0))


def hair_rgb(world, cid):
    return W.hex_rgb(world.hair_colors[cid]["ramp"][2])


def eye_rgb(world, cid):
    return W.hex_rgb(world.eye_colors[cid]["ramp"][2])


def palette_chip(scr, x, y, world, pid, selected, size=36):
    d = scr.d
    ramps = world.palettes[pid]["ramps"]
    d.rounded_rectangle((x - 3, y - 3, x + size + 3, y + size + 3), 8, outline=INK if selected else PANEL, width=3)
    d.rectangle((x, y, x + size, y + size * .6), fill=W.hex_rgb(ramps["P"][2]))
    d.rectangle((x, y + size * .6, x + size * .7, y + size), fill=W.hex_rgb(ramps["S"][2]))
    d.rectangle((x + size * .7, y + size * .6, x + size, y + size), fill=W.hex_rgb(ramps["A"][2]))


# -- the screens ------------------------------------------------------------------------------------------------
def world_screen(world, data):
    scr = Screen("New world: Shinobi options", None, "Varied")
    d = scr.d
    scr.heading(60, 96, "How should this Leaf be?", "Chosen once, at world creation. The main story is the same in both.")
    cards = [("Classic", "A curated village: the same squad, sensei, rival and families, in the same order, every time. "
                         "Names are still rolled per save.", False),
             ("Varied", "The save's seed rolls the squad, sensei and rival, the families, which side stories appear and in what "
                        "order, shop stock and your apartment. Same seed, same village.", True)]
    for i, (name, text, on) in enumerate(cards):
        x = 60 + i * 520
        d.rounded_rectangle((x, 170, x + 490, 400), 16, fill=PAPER if not on else (250, 242, 226), outline=ACCENT if on else FAINT, width=4 if on else 2)
        d.ellipse((x + 24, 194, x + 50, 220), outline=INK, width=3)
        if on:
            d.ellipse((x + 31, 201, x + 43, 213), fill=ACCENT)
        d.text((x + 64, 190), name, font=font(28, True), fill=INK)
        paragraph(d, x + 28, 244, text, 430, 17)
    # Seed.
    y = 440
    scr.heading(60, y, "Save seed", "64-bit; taken from the world seed unless you type one. It also seeds Roll a life in the creator.")
    d.rounded_rectangle((60, y + 70, 560, y + 116), 8, fill=(255, 250, 240), outline=INK, width=2)
    d.text((76, y + 81), "20261029", font=font(20), fill=INK)
    scr.button((580, y + 70, 760, y + 116), "New seed", icon="dice")
    # Difficulty.
    y = 600
    scr.heading(60, y, "Difficulty", "Changeable any time in the settings.")
    for i, (name, sub) in enumerate((("Story", "forgiving, cinematic"), ("Shinobi", "normal windows"), ("Hard", "short telegraphs"))):
        x = 60 + i * 240
        on = i == 0
        d.rounded_rectangle((x, y + 70, x + 224, y + 140), 10, fill=INK if on else PAPER, outline=INK, width=2)
        d.text((x + 16, y + 80), name, font=font(20, True), fill=PAPER if on else INK)
        d.text((x + 16, y + 108), sub, font=font(14), fill=PANEL if on else SOFT)
    # Right column: rules and controls.
    x = 1140
    d.rounded_rectangle((x - 20, 170, SW - 40, 760), 16, fill=PANEL)
    scr.heading(x, 190, "Adventure rules")
    paragraph(d, x, 230, "On: no breaking or placing blocks anywhere. Doors, chests, stations, sitting and sleeping still work, "
                         "and furniture places in your own home.", 400, 15)
    toggle(d, x, 330, True, "Adventure rules (on in the Leaf map)")
    paragraph(d, x, 370, "Off only in builder mode, for making the map.", 400, 14, SOFT)
    scr.heading(x, 430, "Hand signs")
    toggle(d, x, 470, True, "Typed (a key per sign)")
    toggle(d, x, 506, False, "Radial wheel")
    paragraph(d, x, 546, "Also in the settings later.", 400, 14, SOFT)
    scr.heading(x, 600, "What this sets")
    for i, t in enumerate(("mode: varied", "seed: 20261029", "difficulty: story", "adventure rules: on")):
        d.text((x, 640 + i * 24), "· " + t, font=font(15), fill=SOFT)
    scr.button((SW - 300, SH - 64, SW - 40, SH - 20), "Create world", primary=True)
    scr.button((60, SH - 64, 240, SH - 20), "Cancel")
    scr.save("0_world")


def toggle(d, x, y, on, label):
    d.rounded_rectangle((x, y, x + 46, y + 24), 12, fill=(96, 140, 96) if on else PANEL2, outline=INK, width=2)
    d.ellipse((x + (24 if on else 2), y + 2, x + (44 if on else 22), y + 22), fill=PAPER, outline=INK)
    d.text((x + 58, y + 2), label, font=font(16), fill=INK)


def name_screen(world, data):
    scr = Screen("Who are you?", 0)
    d = scr.d
    o = data["origins"]["clanless"]
    look = o["defaults"]["female"]
    preview_panel(scr, world, C.spec(data, "clanless", look), (1140, 86, SW - 24, SH - 90))
    scr.heading(250, 96, "First name", "Residents, the journal and every line of dialogue use it.")
    d.rounded_rectangle((250, 170, 750, 218), 8, fill=(255, 250, 240), outline=INK, width=2)
    d.text((266, 181), "Kaede", font=font(22), fill=INK)
    cx = 270 + d.textlength("Kaede", font=font(22))
    d.line((cx, 180, cx, 208), fill=INK, width=2)
    d.text((250, 226), "2 to 16 letters, any script; spaces, apostrophes and hyphens are fine.", font=font(14), fill=SOFT)
    scr.lock(250, 250, "first name: locked after creation")
    scr.heading(250, 296, "Last name", "The family name you remember: an ordinary one. Pick one or roll.")
    d.rounded_rectangle((250, 366, 750, 414), 8, fill=(255, 250, 240), outline=INK, width=2)
    d.text((266, 377), "Tanaka", font=font(22), fill=INK)
    d.text((712, 375), "v", font=font(22, True), fill=INK)
    scr.button((770, 366, 920, 414), "Roll", icon="dice")
    d.rounded_rectangle((940, 372, 1090, 408), 18, fill=PANEL2, outline=FAINT)
    d.text((965, 380), "no clan", font=font(16, True), fill=SOFT)
    fam = o["family_names"]
    for i, n in enumerate(fam[:18]):
        x, y = 250 + (i % 6) * 118, 430 + (i // 6) * 32
        on = n == "Tanaka"
        d.rounded_rectangle((x, y, x + 110, y + 26), 6, fill=INK if on else PAPER, outline=FAINT)
        d.text((x + 8, y + 4), n, font=font(14), fill=PAPER if on else INK)
    d.text((250, 530), f"... {len(fam)} ordinary family names in all; never a clan's", font=font(13), fill=SOFT)
    scr.heading(250, 566, "Pronouns", "How text refers to you when someone talks about you. Changeable any time in the settings.")
    for i, (label, on) in enumerate((("they / them", False), ("she / her", True), ("he / him", False))):
        x = 250 + i * 170
        d.rounded_rectangle((x, 630, x + 156, 668), 10, fill=INK if on else PAPER, outline=INK, width=2)
        d.text((x + 78 - d.textlength(label, font=font(16, True)) / 2, 639), label, font=font(16, True), fill=PAPER if on else INK)
    d.rounded_rectangle((250, 690, 1100, 800), 12, fill=PANEL)
    d.text((270, 702), "How you will appear", font=font(15, True), fill=INK)
    rows = [("{player}", "Kaede", "friends, squad, most lines"), ("{player_full}", "Kaede Tanaka", "papers, the Hokage, the journal"),
            ("{player_family}", "Tanaka", "formal greetings")]
    for i, (tok, val, use) in enumerate(rows):
        y = 728 + i * 22
        d.text((270, y), tok, font=font(14, True), fill=ACCENT)
        d.text((450, y), val, font=font(14), fill=INK)
        d.text((640, y), use, font=font(13), fill=SOFT)
    scr.footer()
    scr.save("1_name")


def roots_screen(world, data):
    scr = Screen("Who are you?", 5)
    d = scr.d
    look = data["origins"]["clanless"]["defaults"]["male"]
    preview_panel(scr, world, C.spec(data, "clanless", look), (1140, 86, SW - 24, SH - 90))
    scr.heading(250, 86, "Roots", "Small things about you. None of them changes the story.")
    blurbs = {
        "temperament": ("Temperament", "How you carry yourself. Some lines notice it; friendships do not depend on it.",
                        {"bold": "Bold", "steady": "Steady", "cheerful": "Cheerful", "quiet": "Quiet", "curious": "Curious", "stubborn": "Stubborn"}, "curious"),
        "knack": ("Knack", "What comes easily at the Academy: +5% to it, and a practice item to start.",
                  {"balanced": "Balanced", "taijutsu": "Taijutsu", "weapons": "Weapons", "ninjutsu": "Ninjutsu"}, "taijutsu"),
        "affinity": ("Affinity", "The nature you lean toward. The Genin ceremony offers every nature; choosing this one there gives a bonus.",
                     {"undecided": "Undecided", "fire": "Fire", "wind": "Wind", "water": "Water", "earth": "Earth", "lightning": "Lightning"}, "wind"),
    }
    colors = {"fire": (196, 74, 44), "wind": (110, 168, 120), "water": (70, 120, 190), "earth": (150, 112, 70), "lightning": (214, 180, 60)}
    y = 160
    for key, (title, sub, labels, sel) in blurbs.items():
        d.text((250, y), title, font=font(20, True), fill=INK)
        paragraph(d, 250, y + 30, sub, 840, 14, SOFT, 4)
        for i, opt in enumerate(data["roots"][key]["options"]):
            x = 250 + i * 142
            on = opt == sel
            d.rounded_rectangle((x, y + 66, x + 132, y + 108), 10, fill=INK if on else PAPER, outline=INK, width=2)
            if opt in colors:
                d.ellipse((x + 10, y + 79, x + 26, y + 95), fill=colors[opt], outline=INK)
            lab = labels[opt]
            tx = x + (36 if opt in colors else 66 - d.textlength(lab, font=font(15, True)) / 2)
            d.text((tx, y + 77), lab, font=font(15, True), fill=PAPER if on else INK)
        y += 150
    scr.lock(250, 620, "roots: locked after creation (the ceremony still offers every nature)")
    d.text((250, 650), "Starting numbers are the same for every player: 10 hearts, chakra 53, control 35, stamina 110, poise 20.",
           font=font(14), fill=SOFT)
    scr.footer()
    scr.save("6_roots")


def body_screen(world, data):
    scr = Screen("Who are you?", 1)
    d = scr.d
    look = dict(data["origins"]["clanless"]["defaults"]["female"], complexion=3, eye_color="JADE", eye_style="soft_glint")
    preview_panel(scr, world, C.spec(data, "clanless", look), (1140, 86, SW - 24, SH - 90))
    scr.heading(250, 96, "Body")
    for i, (label, on) in enumerate((("Body A", False), ("Body B", True))):
        x = 250 + i * 190
        d.rounded_rectangle((x, 136, x + 176, 182), 10, fill=INK if on else PAPER, outline=INK, width=2)
        d.text((x + 88 - d.textlength(label, font=font(18, True)) / 2, 148), label, font=font(18, True), fill=PAPER if on else INK)
    paragraph(d, 640, 140, "Sets which tops and bottoms fit, and the face's lashes and lips. Every hairstyle fits both.", 460, 14, SOFT, 4)
    scr.lock(250, 192, "body: locked after creation")
    scr.heading(250, 236, "Complexion")
    cols = [W.hex_rgb(c["swatch"]) for c in world.rules["complexions"]]
    labels = [c["label"].split(".")[-1].title() for c in world.rules["complexions"]]
    swatch_row(scr, 250, 276, cols, 3, size=52, gap=18, labels=labels)
    scr.lock(250, 362, "complexion: locked after creation")
    scr.heading(250, 404, "Eye shape")
    for i, (label, on) in enumerate((("Starlit", False), ("Soft glint", True))):
        x = 250 + i * 190
        d.rounded_rectangle((x, 444, x + 176, 486), 10, fill=INK if on else PAPER, outline=INK, width=2)
        d.text((x + 88 - d.textlength(label, font=font(17, True)) / 2, 454), label, font=font(17, True), fill=PAPER if on else INK)
    scr.heading(650, 404, "Brows")
    for i, (label, on) in enumerate((("Fine", True), ("Bold", False))):
        x = 650 + i * 150
        d.rounded_rectangle((x, 444, x + 136, 486), 10, fill=INK if on else PAPER, outline=INK, width=2)
        d.text((x + 68 - d.textlength(label, font=font(17, True)) / 2, 454), label, font=font(17, True), fill=PAPER if on else INK)
    scr.changeable(650, 494, "brows: the barber")
    scr.heading(250, 536, "Eyes", "Dark, sky blue, jade, hazel or grey.")
    eyes = data["origins"]["clanless"]["eye_colors"]
    swatch_row(scr, 250, 606, [eye_rgb(world, e) for e in eyes], eyes.index("JADE"), size=44, gap=16,
               labels=[world.eye_colors[e]["name"].replace("Kunoichi ", "") for e in eyes])
    scr.lock(250, 684, "eyes: locked after creation")
    die(d, 250, 730, 22)
    d.text((282, 731), "Each row has its own dice, within what you are allowed. Roll a life (Varied) rolls everything.", font=font(14), fill=SOFT)
    scr.footer()
    scr.save("2_body")


def hair_screen(world, data, origin="clanless"):
    scr = Screen("Who are you?", 2)
    d = scr.d
    o = data["origins"][origin]
    look = dict(o["defaults"]["female"])
    v = C.view(data, origin, "child")
    hair = v["hair"]
    look["hair"] = "hg007_side_swept_bob"
    look["hair_color"] = "AUBURN"
    preview_panel(scr, world, C.spec(data, origin, look), (1140, 86, SW - 24, SH - 90))
    scr.heading(250, 86, "Hairstyle", f"Every collection's styles: {len(hair)} at this age")
    tabs = ["All", "Short", "Long", "Tied"]
    for i, t in enumerate(tabs):
        x = 250 + i * 104
        on = i == 0
        d.rounded_rectangle((x, 146, x + 96, 176), 8, fill=INK if on else PAPER, outline=INK, width=1)
        d.text((x + 48 - d.textlength(t, font=font(14, True)) / 2, 152), t, font=font(14, True), fill=PAPER if on else INK)
    thumbs = hair[:12]
    if look["hair"] not in thumbs:
        thumbs[2] = look["hair"]
    cw, chh = 140, 140
    for i, hid in enumerate(thumbs):
        x, y = 250 + (i % 6) * (cw + 8), 190 + (i // 6) * (chh + 30)
        spec = C.spec(data, origin, dict(look, hair=hid))
        img = character_image(world, spec, cw, chh, heads=True)
        scr.img.paste(img, (x, y))
        on = hid == look["hair"]
        d.rounded_rectangle((x - 2, y - 2, x + cw + 2, y + chh + 2), 8, outline=ACCENT if on else FAINT, width=3 if on else 1)
        name = world.garments[hid].meta["name"]
        d.text((x + cw / 2 - d.textlength(name, font=font(12)) / 2, y + chh + 6), name, font=font(12), fill=INK)
    d.text((250, 534), "Scroll for more  ·  styles that wait for a later age (beards, elders' styles) are not listed", font=font(13), fill=SOFT)
    scr.changeable(250, 556, "hairstyle: the barber (40 ryo), and free at each time skip")
    scr.heading(250, 600, "Hair color")
    cols = v["hair_colors"]
    swatch_row(scr, 250, 640, [hair_rgb(world, c) for c in cols], cols.index("AUBURN"), size=40, gap=12, per_row=13,
               labels=[world.hair_colors[c]["name"].split()[0] for c in cols])
    scr.changeable(250, 738, "hair color: the barber (60 ryo)")
    scr.footer()
    scr.save("3_hair")


def face_screen(world, data, origin="clanless"):
    scr = Screen("Who are you?", 3)
    d = scr.d
    o = data["origins"][origin]
    look = dict(o["defaults"]["male"], marks=["whiskers"], headwear="wg001_flight_goggles")
    preview_panel(scr, world, C.spec(data, origin, look), (1140, 86, SW - 24, SH - 90))
    v = C.view(data, origin, "child")
    scr.heading(250, 96, "Marks", f"Up to {data['max_marks']}, or none.")
    for i, m in enumerate(v["marks"]):
        x, y = 250 + i * 250, 170
        on = m in look["marks"]
        spec = C.spec(data, origin, dict(look, marks=[m], headwear=None))
        img = character_image(world, spec, 150, 150, heads=True, yaw=-12)
        scr.img.paste(img, (x, y))
        d.rounded_rectangle((x - 2, y - 2, x + 152, y + 152), 8, outline=ACCENT if on else FAINT, width=3 if on else 1)
        d.rectangle((x + 160, y + 4, x + 182, y + 26), fill=INK if on else PAPER, outline=INK, width=2)
        if on:
            d.line((x + 164, y + 15, x + 170, y + 22, x + 179, y + 8), fill=PAPER, width=3)
        d.text((x + 160, y + 40), m.replace(origin + "_", "").replace("_", " "), font=font(14), fill=INK)
    scr.changeable(250, 366, "marks: the barber (30 ryo); scars the story gives stay")
    scr.heading(250, 420, "Headwear", "Before Genin: goggles or a headband. The forehead protector comes at graduation.")
    hw = v["headwear"]
    for i, h in enumerate(hw):
        x, y = 250 + i * 170, 490
        spec = C.spec(data, origin, dict(look, headwear=h))
        img = character_image(world, spec, 150, 150, heads=True)
        scr.img.paste(img, (x, y))
        on = h == look["headwear"]
        d.rounded_rectangle((x - 2, y - 2, x + 152, y + 152), 8, outline=ACCENT if on else FAINT, width=3 if on else 1)
        name = world.garments[h].meta["name"] if h else "Bare head"
        d.text((x + 75 - d.textlength(name, font=font(13)) / 2, y + 158), name, font=font(13), fill=INK)
    scr.changeable(250, 690, "headwear: your home's wardrobe chest")
    scr.footer()
    scr.save("4_face")


def outfit_screen(world, data, origin="clanless"):
    scr = Screen("Who are you?", 4)
    d = scr.d
    o = data["origins"][origin]
    look = dict(o["defaults"]["female"])
    v = C.view(data, origin, "child")
    outfits = v["outfits"]["female"]
    preview_panel(scr, world, C.spec(data, origin, look), (1140, 86, SW - 24, SH - 90))
    scr.heading(250, 86, "Starting outfit", "From the Academy collection. Rank outfits come with each promotion.")
    cw, chh = 150, 210
    for i, oo in enumerate(outfits[:10]):
        x, y = 250 + (i % 5) * (cw + 22), 150 + (i // 5) * (chh + 34)
        pal = look["palette"] if look["palette"] in oo["palettes"] else oo["palettes"][0]
        spec = C.spec(data, origin, dict(look, outfit=oo["id"], palette=pal))
        img = character_image(world, spec, cw, chh, unit=chh / 36)
        scr.img.paste(img, (x, y))
        on = oo["id"] == look["outfit"]
        d.rounded_rectangle((x - 2, y - 2, x + cw + 2, y + chh + 2), 8, outline=ACCENT if on else FAINT, width=3 if on else 1)
        name = oo["id"].split(".")[1].replace("_", " ")
        tag = "clan" if oo["from"] == "clan" else ""
        d.text((x + cw / 2 - d.textlength(name, font=font(12)) / 2, y + chh + 4), name, font=font(12), fill=INK)
        if tag:
            d.rounded_rectangle((x + 4, y + 4, x + 44, y + 22), 5, fill=ACCENT)
            d.text((x + 10, y + 5), tag, font=font(11, True), fill=PAPER)
    scr.heading(250, 650, "Colors", "Each outfit's own palettes.")
    cur = next(x for x in outfits if x["id"] == look["outfit"])
    for i, pid in enumerate(cur["palettes"][:14]):
        palette_chip(scr, 250 + i * 52, 712, world, pid, pid == look["palette"])
    scr.changeable(250, 766, "outfit and colors: your home's wardrobe chest; the tailor sells more")
    scr.footer()
    scr.save("5_outfit")


def review_screen(world, data, origin="clanless"):
    scr = Screen("Who are you?", 6)
    d = scr.d
    o = data["origins"][origin]
    look = dict(o["defaults"]["male"], hair="hg006_short_spikes", hair_color="RAVEN", complexion=3, eye_color="SKY",
                marks=["whiskers"], headwear="wg001_flight_goggles", outfit="academy_genin.cold_morning", palette="ACADEMY_GENIN_INDIGO")
    spec = C.spec(data, origin, look)
    img = character_image(world, spec, 420, 640)
    d.rounded_rectangle((240, 86, 680, SH - 90), 14, fill=PANEL2)
    scr.img.paste(img, (250, 96))
    grown = P.grown(data, origin, look, "adult", next(x["id"] for x in C.view(data, origin, "adult")["outfits"]["male"] if x["rank"] == "jonin"))
    img2 = character_image(world, C.spec(data, origin, grown, "adult"), 200, 330, stage="adult")
    d.rounded_rectangle((700, 86, 920, 470), 14, fill=PANEL2)
    scr.img.paste(img2, (710, 96))
    d.text((712, 436), "One day (a preview)", font=font(13), fill=SOFT)
    x = 950
    d.text((x, 92), "Ren Tanaka", font=font(34, True), fill=INK)
    d.text((x, 140), "no clan · Academy student · age 11", font=font(16), fill=SOFT)
    rows = [("Name", "Ren Tanaka (he / him)", True), ("Body", "Body A", True), ("Complexion", "Amber", True),
            ("Eyes", "Sky Blue", True), ("Hairstyle", world.garments[look["hair"]].meta["name"], False),
            ("Hair color", world.hair_colors[look["hair_color"]]["name"], False), ("Marks", "whiskers", False),
            ("Outfit", look["outfit"].split(".")[1].replace("_", " "), False), ("Headwear", "flight goggles", False),
            ("Roots", "steady · weapons · leans to fire", True)]
    for i, (k, val, locked) in enumerate(rows):
        y = 180 + i * 40
        d.line((x, y + 32, SW - 40, y + 32), fill=PANEL2)
        d.text((x, y + 6), k, font=font(16, True), fill=INK)
        d.text((x + 150, y + 6), val, font=font(16), fill=INK)
        if locked:
            scr.lock(x + 430, y + 8, "locked")
        else:
            scr.changeable(x + 430, y + 8, "changeable later")
        d.text((SW - 76, y + 6), "edit", font=font(14, True), fill=ACCENT)
    # The starting key item, in hand: a small charred wooden charm (drawn as an icon; the item's model is the items session's).
    d.rounded_rectangle((700, 490, 920, 700), 14, fill=PANEL2)
    cx, cy = 810, 575
    d.ellipse((cx - 60, cy - 30, cx + 60, cy + 40), fill=(214, 176, 140))           # an open palm
    d.polygon([(cx - 6, cy - 34), (cx + 26, cy - 22), (cx + 18, cy + 22), (cx - 14, cy + 10)], fill=(74, 50, 36), outline=(34, 22, 16))
    d.line((cx - 6, cy - 34, cx - 14, cy + 10), fill=(120, 86, 60), width=2)       # the broken edge of half a pair
    d.line((cx + 8, cy - 46, cx + 4, cy - 30), fill=(150, 40, 34), width=3)        # its cord
    tw = d.textlength("The only thing that is yours.", font=font(14))
    d.text((810 - tw / 2, 640), "The only thing that is yours.", font=font(14), fill=INK)
    d.text((810 - d.textlength("half charm", font=font(12)) / 2, 664), "half charm", font=font(12), fill=SOFT)
    paragraph(d, x, 610, "You begin the story with this and the clothes you stand in; your outfit waits at your apartment.",
              600, 15, SOFT)
    scr.footer("Begin", dice=False)
    scr.save("7_review")


def mirror_screen(world, data):
    scr = Screen("Years later", None, "Varied")
    d = scr.d
    base = dict(data["origins"]["clanless"]["defaults"]["female"], hair="hg003_short_twin_tails", hair_color="CHESTNUT",
                eye_color="JADE", complexion=2, palette="ACADEMY_GENIN_SKY")
    teen = P.grown(data, "clanless", base, "teen", "kunoichi.wrap_runner")
    d.rounded_rectangle((40, 86, 420, SH - 40), 14, fill=PANEL2)
    scr.img.paste(character_image(world, C.spec(data, "clanless", base), 360, 700, unit=17), (50, 120))
    d.text((60, 96), "Before (11)", font=font(16, True), fill=INK)
    d.rounded_rectangle((440, 86, 900, SH - 40), 14, fill=PANEL2)
    scr.img.paste(character_image(world, C.spec(data, "clanless", teen, "teen"), 440, 700, stage="teen", unit=17), (450, 120))
    d.text((460, 96), "Now (15)", font=font(16, True), fill=INK)
    x = 940
    scr.heading(x, 96, "The mirror", "A time skip has passed. Restyle for free; everything locked stays as it was.")
    items = [("Hairstyle", f"{world.garments[base['hair']].meta['name']} grew into {world.garments[teen['hair']].meta['name']}"),
             ("Hair color", "unchanged"), ("Brows", "unchanged"), ("Marks", "unchanged"),
             ("Outfit", "your rank's outfit: Genin"), ("Headwear", "forehead protector available")]
    for i, (k, v) in enumerate(items):
        y = 180 + i * 64
        d.rounded_rectangle((x, y, SW - 40, y + 54), 10, fill=PAPER, outline=FAINT)
        d.text((x + 16, y + 8), k, font=font(17, True), fill=INK)
        d.text((x + 16, y + 30), v, font=font(14), fill=SOFT)
        d.text((SW - 110, y + 16), "change", font=font(14, True), fill=ACCENT)
    d.text((x, 580), "The hair the mirror suggests can be changed to any style your stage allows.", font=font(14), fill=SOFT)
    scr.lock(x, 610, "name, body, complexion, eyes, clan: locked")
    scr.button((SW - 260, SH - 84, SW - 40, SH - 40), "Done", primary=True)
    scr.save("8_years_later")


def all_screens(world, data):
    OUT.mkdir(parents=True, exist_ok=True)
    world.data = data
    for p in OUT.glob("screen_*.png"):
        p.unlink()
    world_screen(world, data)
    name_screen(world, data)
    body_screen(world, data)
    hair_screen(world, data)
    face_screen(world, data)
    outfit_screen(world, data)
    roots_screen(world, data)
    review_screen(world, data)
    mirror_screen(world, data)
