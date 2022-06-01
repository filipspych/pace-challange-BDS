from cgitb import reset
import parser
import igraph as ig
import PZ
import PS
import PW
import kill
import sys

def run(path: str="") -> tuple[int, int, list[int]]:
    G: ig.Graph = parser.parse(path)
    g: ig.Graph = G.copy()
    result: list[int] = []
    n = G.vcount()
    m = G.ecount()
    PZ.rozpocznij(g)
    while(g.vcount() > 0):
        v = PS.PS(g)
        result.append(g.vs[v]["name"])
        g = PZ.getGrafPoNastepnejIteracji(v)    
    # PW.PW(G, list(map(str,result)))
    return (n, m, result)

def return_result(path: str="") -> list[int]:
    return run(path)[2]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        result = return_result()
    else:
        result = return_result(sys.argv[1])
    kill.end_with_result(result)
