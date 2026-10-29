"""Mesh Half-Sleeve Tee: a plain round-necked tee with half sleeves edged in the accent colour, the
chain mesh showing at the throat and running down the forearms to the wrist."""
from kit import neckline
from kit_field import chain, half_sleeves, mesh_arms, shirt

META = {
    "name": "Mesh Half-Sleeve Tee",
    "gender": "unisex",
    "description": "Round-necked tee with accent-edged half sleeves over a mesh undershirt and mesh forearms.",
    "tags": ["shinobi", "genin"],
}


def build(g):
    body = shirt(g, "D", 32140, sleeve=-1, texture="knit")
    neckline(body.front, "round", "D")
    chain(body.front, 3, 0, 4, 0)
    body.strip.hline(0, body.strip.w - 1, 11, "D1")
    half_sleeves(g, "D", 32143, length=5, texture="knit")
    for side in ("right", "left"):
        g.part(f"{side}_sleeve").strip.hline(0, 15, 5, "A2")
    mesh_arms(g, (6, 10))
