"""Thread Wraps: a fitted dark long-sleeved shirt with chakra threads wound criss-cross from elbow to
wrist and crossed over the chest in a harness, a spool of wire thread hung at the hip."""
from kit import belt, body, sleeves
from kit_tsuchigumo import thread_spool, threads
from paint import solid

META = {
    "name": "Thread Wraps",
    "gender": "unisex",
    "description": "Fitted dark shirt with threads wound criss-cross on the forearms and crossed over the chest.",
    "tags": ["shinobi"],
}


def build(g):
    torso = body(g, "D", "weave", 23491)
    for face in torso.sides:
        face.hline(0, face.w - 1, 0, "D3")
    for arm in sleeves(g, "D", "weave", 23492, rows=(0, 11)):
        for face in arm.sides:
            threads(face, 0, 5, face.w - 1, 11, "A2", step=4)
    for i, rz in enumerate((-36, 36)):   # the chest harness of thread
        band = g.piece(f"harness_{i}", "TORSO", (-.5, -6.5, -.5), (1, 13, 1), pivot=(0, 5.0, -2.25), rotation=(0, 0, rz),
                       scale=(.6, 1, .6))
        solid(band, "A", "plain", 23495 + i, 2, edge=False)
    belt(g, "belt", y=9.4, role="P", height=2, buckle=None)
    thread_spool(g, "spool", (3.6, 10.4, -1.0))
