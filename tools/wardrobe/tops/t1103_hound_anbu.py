"""Hound ANBU: Kakashi's ANBU years, grey-white plated armor over a dark sleeveless shirt, black gloves
under long white guards, the red spiral on the left shoulder and his father's white-hilted tanto
across the back, the hilt over the right shoulder."""
from kit_hatake import white_fang_tanto
from kit_shinobi import anbu_arms, anbu_plates
from paint import cap, strip_fabric

META = {
    "name": "Hound ANBU",
    "gender": "unisex",
    "description": "ANBU plated armor, white arm guards, the shoulder spiral and a white-hilted tanto across the back.",
    "tags": ["shinobi", "armor"],
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "D", "weave", 11201, 2)
    cap(body, "D", seed=11201)
    anbu_plates(g, seed=11202)
    anbu_arms(g)
    white_fang_tanto(g, "tanto", pivot=(-2.0, 2.4, 2.9), rotation=(0, 0, 34), length=8)
