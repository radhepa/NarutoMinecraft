"""ANBU Armor: a black sleeveless undershirt under grey-white plated chest armor, long white arm
guards over black gloves, the red spiral tattoo on the left shoulder and a tanto across the back."""
from kit_shinobi import anbu_arms, anbu_plates, tanto
from paint import cap, strip_fabric

META = {
    "name": "ANBU Armor",
    "gender": "unisex",
    "description": "Grey-white plated chest armor over a black sleeveless shirt, white arm guards, a tanto.",
    "tags": ["shinobi", "armor"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 151, 2)
    cap(body, "D", seed=151)
    anbu_plates(g)
    anbu_arms(g)
    tanto(g)   # across the back: wrapped hilt over the right shoulder
