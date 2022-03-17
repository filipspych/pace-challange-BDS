import shlex
import os
import tempfile
from sys import platform
from re import template
from igraph import *
from typing import List

import PZ
import opt


def pokazSvg(g: Graph, filename: str):
    EDGE_THICKNESS: float = 2
    VERTEX_SIZE: int = 15
    LAYOUT: str = "circle"  # dostepne: auto, circle, star, grid, random, sugiyama, ORAZ INNE TUTAJ: https://igraph.org/c/html/latest/igraph-Layout.html
    WIDTH = 720
    HEIGHT = WIDTH

    filename=tempfile.NamedTemporaryFile(suffix='.svg').name # kompatybilnosc z inkspace
    # print(g)
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


# Sprawdzam czy jesteśmy na windowsie
winda: bool = True if platform == "win32" else False
filename = tempfile.NamedTemporaryFile(suffix=".svg").name
g: Graph = Graph.Growing_Random(10, 2, True).simplify()
mfvs: List[int] = opt.getMFVSDokladny(g)
pokazSvg(g, filename)
input("Pokazujemy graf wejciowy, kliknij ENTER by obliczyc dla niego MFVS...")
print("MFVS dokladny:", end=" ")
print(mfvs)
g.delete_vertices(mfvs)
pokazSvg(g, filename)
input("Pokazujemy graf po odjeciu MFVS, kliknij ENTER by zakonczyc program...")

