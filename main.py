import parser
import igraph as ig
import PZ
import PS
import PW
import kill

result: list[int] = []
path = "h_001"

if __name__ == "__main__":
    G: ig.Graph = parser.parse(path)
    g: ig.Graph = G.copy()

    PZ.rozpocznij(g)
    while(g.vcount() > 0):
        v = PS.PS(g)
        # print(v)
        result.append(g.vs[v]["name"])
        g = PZ.getGrafPoNastepnejIteracji(v)    
    
    print(result)
    print("len:")
    print(len(result))

    PW.PW(G, result)
    kill.end_with_result(result)


