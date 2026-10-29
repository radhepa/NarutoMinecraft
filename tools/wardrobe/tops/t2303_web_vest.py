"""Web Vest: a sleeveless plum vest over a dark fitted shirt, a full spider web worked across the
back in ochre thread and web-line trims down the front edges, the chunin's field wear."""
from kit import belt, body, sleeves
from kit_tsuchigumo import web, web_hem
from paint import k

META = {
    "name": "Web Vest",
    "gender": "unisex",
    "description": "Sleeveless plum vest with an ochre spider web across the back over a dark fitted shirt.",
    "tags": ["shinobi", "vest"],
}


def build(g):
    body(g, "D", "weave", 23461)
    sleeves(g, "D", "weave", 23462, rows=(0, 10), cuff="D3")
    vest = body(g, "P", "twill", 23463, layer="jacket", rows=(0, 10))
    web(vest.back, 3, 2, "A2", rings=(2, 4, 6, 8), y1=10)
    f = vest.front
    f.vline(3, 0, 10, k("P", 0)), f.vline(4, 0, 10, k("P", 0))
    f.vline(2, 0, 10, "A2"), f.vline(5, 0, 10, "A2")
    for face in vest.sides:
        web_hem(face, 10, "A2", "A1")
    belt(g, "belt", y=9.6, role="L", height=1, buckle="M")
