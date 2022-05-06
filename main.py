import parser
import igraph as ig
import PZ
import PS
import PW
import kill

result: list[int] = []

def run(path):
    G: ig.Graph = parser.parse(path)
    g: ig.Graph = G.copy()

    PZ.rozpocznij(g)
    while(g.vcount() > 0):
        v = PS.PS(G)
        result.append(g.vs[v]["index"])
        g = PZ.getGrafPoNastepnejIteracji(v)
    
    
    # PW.PW(G, result)
    kill.end_with_result(result)
