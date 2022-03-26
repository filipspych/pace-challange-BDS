import shlex
import os
import tempfile
from sys import platform
from re import template
from igraph import *

import PZ


def pokazSvg(g: Graph, filename: str):
    EDGE_THICKNESS: float = 0.3
    VERTEX_SIZE: int = 5
    LAYOUT: str = "auto"  # dostepne: auto, circle, star, grid, random, sugiyama, ORAZ INNE TUTAJ: https://igraph.org/c/html/latest/igraph-Layout.html
    WIDTH = 3000
    HEIGHT = WIDTH

    # filename=tempfile.NamedTemporaryFile(suffix='.svg').name # kompatybilnosc z inkspace
    print(g)
    g.write_svg(
        fname=filename,
        vertex_size=VERTEX_SIZE,
        edge_stroke_widths=[EDGE_THICKNESS] * g.ecount(),
        font_size=VERTEX_SIZE,
        width=WIDTH,
        height=HEIGHT,
        layout=LAYOUT,
    )
    # plot(g)
    if winda:
        os.system("start " + filename)  # windows
    else:
        os.system("open " + shlex.quote(filename))  # MacOS/X
    input("Kliknij ENTER...")


# Sprawdzam czy jesteśmy na windowsie
winda: bool = True if platform == "win32" else False
filename = tempfile.NamedTemporaryFile(suffix=".svg").name

g: Graph = Graph.Growing_Random(500, 2, True).simplify()
pokazSvg(g, filename)

PZ.rozpocznij(g)
for i in range(8):
    g = PZ.getGrafPoNastepnejIteracji(0)
    pokazSvg(g, filename)

s: str = ""
while s != "usun":
    s = input(
        "Koniec. Wpisz 'usun', zeby skasowac obrazki grafow z pamieci komputera: "
    )

# zakonczenie programu usuwa pliki tymczasowe
print("Usuwam pliki tymczasowe...")
