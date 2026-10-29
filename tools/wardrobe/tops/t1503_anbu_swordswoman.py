"""ANBU Swordswoman: Yugao Uzuki in the Black Ops: the grey plated armor over a black shirt, long
white arm guards, the red spiral on the left arm and her katana slung across the back on a black
strap, the hilt over the right shoulder."""
from kit_gekko import katana, sword_strap
from kit_shinobi import anbu_arms, anbu_plates
from paint import cap, strip_fabric

META = {
    "name": "ANBU Swordswoman",
    "gender": "unisex",
    "description": "ANBU plated armor, white arm guards, the spiral tattoo, a katana on the back on a black strap.",
    "tags": ["shinobi", "armor"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 15730, 2)
    cap(body, "D", seed=15730)
    anbu_plates(g, seed=15731)
    jacket = g.part("jacket")
    sword_strap(jacket.front, "K", rows=9)
    sword_strap(jacket.back, "K", rows=9, mirror=True)
    anbu_arms(g)
    katana(g, pivot=(-1.4, 2.2, 3.0), cord="A2")
