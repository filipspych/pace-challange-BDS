from parso import parse
import parser
import igraph as ig
import PZ
import PS
import PW
import signal
import kill

result: list[int] = []

def run():
    signal.signal(signal.SIGINT, exit)
    signal.signal(signal.SIGTERM, exit)

    G: ig.Graph = parser.parse()
    g: ig.Graph = G.copy()

    PZ.rozpocznij(g)
    while(g.vcount() > 0):
        v = PS.PS(G)
        result.append(g.vs[v]["index"])
        g = PZ.getGrafPoNastepnejIteracji(v)
    
    kill.uaktualnij_rozwiazanie(result)
    
    # PW.PW(G, result)

