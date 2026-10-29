"""Scholar's Robe: the long sober robe of the village's teachers, archivists and letter-writers,
falling to the knee with a pale inner collar at the throat, broad sleeves to the wrist, a narrow
sash knotted at the side and a bound book tucked into the sash at the front."""
from kit_household import overlap, robe_skirt, sash, wide_sleeves
from paint import cap, solid, strip_fabric

META = {
    "name": "Scholar's Robe",
    "gender": "unisex",
    "description": "Knee-length robe, pale inner collar, broad wrist sleeves, side-knotted sash with a book tucked in.",
    "tags": ["civilian", "robe", "wrap"],
    "covers_waist": True,
}


def build(g):
    body = g.part("body")
    strip_fabric(body, "P", "twill", 37140, 2)
    cap(body, "P", texture="twill", seed=37140)
    overlap(body.front, "S3", "P1", rows=12, collar="S3", under="S4")
    for face in (body.right, body.left):
        face.vline(1, 0, 11, "P1")
    robe_skirt(g, "robe", 7, "P", "twill", 37141, hem="P0", overlap_key="P1")
    wide_sleeves(g, "sleeve", "P", "twill", 37143, top=2.0, length=9, hem="S3", arm_rows=9)
    sash(g, "sash", "D", y=7.8, height=2, knot="side", seed=37148)
    book = g.piece("book", "TORSO", (0, 0, 0), (2, 3, 1), pivot=(-3.4, 6.4, -3.05), rotation=(0, 0, 8))
    solid(book, "L", "leather", 37152, 2, edge=False)
    for face in (book.left, book.top):
        face.fill("S4")
    book.front.vline(0, 0, 2, "L1"), book.front.set(1, 1, "S3")
