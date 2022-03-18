# UI component
# czyli PZ udostępnia PZ.getGrafPoNastepnejIteracji(int wierzcholekONajwikszeCyklowosci),
# PS udostępnia PS.getWierzcholekONajwiekszejCyklowosci(G)
# dodatkowo PZ.rozpocznij(G) który resetuje PZ i przekazuje PZ że teraz PZ będzie pracowało na grafie G

from igraph import *
import PZ
import PS
import tempfile
from sys import platform


def InitializeProcedure(G: Graph):

    winda: bool = True if platform == "win32" else False
    filename = tempfile.NamedTemporaryFile(suffix=".svg").name

    PZ.rozpocznij(G)
    result: list[int] = []
    g: Graph = G
    while(True):
        print('-------------------------------')
        print('i - next iteration')
        print('p - show graph')
        x = input()
        match x:
            case 'i':
                print('next iteration')
                g = NextStep(result, g)
            case 'p':
                print('showing plot')
                pokazSvg(g, filename, winda)


def NextStep(result, G):
    v = PS.PS(G)
    result.append(v)
    return PZ.getGrafPoNastepnejIteracji(v)

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
    input("Kliknij ENTER...")

InitializeProcedure(Graph.Full(5, directed=True))
