from cgitb import reset
import parser
import igraph as ig
import generating as gen
from CycleCounter import ExactPS, FullPS
import PZ
import PS
import PW
import kill
import sys

def run(path: str="") -> tuple[int, int, list[int]]:
    G: ig.Graph = parser.parse(path)
    #(G, opt) = gen.GenerateRandomGraph(50, 20, 1000)
    g: ig.Graph = G.copy()
    result: list[int] = []
    n = G.vcount()
    m = G.ecount()
    PZ.rozpocznij(g)
    while(g.vcount() > 0):
        v = PS.PS(g)
<<<<<<< HEAD
        # print(FullPS(g))
        # v = ExactPS(g)
        print(v)
=======
>>>>>>> c4bd73f61317457b1bb6b1592c4dfe0f35b5ff0e
        result.append(g.vs[v]["name"])
        #result.append(g.vs[v])
        g = PZ.getGrafPoNastepnejIteracji(v)    
<<<<<<< HEAD
    
    #print(result)
    print("len:")
    print(len(result))

    PW.PW(G, list(map(str,result)))
    # kill.end_with_result(result)
=======
    # PW.PW(G, list(map(str,result)))
    return (n, m, result)
>>>>>>> c4bd73f61317457b1bb6b1592c4dfe0f35b5ff0e

def return_result(path: str="") -> list[int]:
    return run(path)[2]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        result = return_result()
    else:
        result = return_result(sys.argv[1])
    kill.end_with_result(result)
