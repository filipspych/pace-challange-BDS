import shlex
import tempfile
from sys import platform
from igraph import Graph, os

def plotGraph(g: Graph):
    winda: bool = True if platform == "win32" else False
    filename = tempfile.NamedTemporaryFile(suffix=".svg").name
    pokazSvg(g, filename, winda)

def pokazSvg(g: Graph, filename: str, winda):
    EDGE_THICKNESS: float = 0.3
    VERTEX_SIZE: int = 5
    LAYOUT: str = "auto"
    WIDTH = 100
    HEIGHT = 100

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

    if winda:
        os.system("start " + filename)  # windows
    else:
        os.system("open " + shlex.quote(filename))  # MacOS/X