import parser
import igraph as ig
import generating as gen
from CycleCounter import ExactPS, FullPS
import PZ
import PS
import PW
import kill

result: list[int] = []
path = "e_001"

if __name__ == "__main__":
    G: ig.Graph = parser.parse(path)
    #(G, opt) = gen.GenerateRandomGraph(50, 20, 1000)
    g: ig.Graph = G.copy()

    PZ.rozpocznij(g)
    while(g.vcount() > 0):
        v = PS.PS(g)
        # print(FullPS(g))
        # v = ExactPS(g)
        print(v)
        result.append(g.vs[v]["name"])
        #result.append(g.vs[v])
        g = PZ.getGrafPoNastepnejIteracji(v)    
    
    #print(result)
    print("len:")
    print(len(result))

    PW.PW(G, list(map(str,result)))
    # kill.end_with_result(result)


