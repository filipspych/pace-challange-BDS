from parso import parse
import parser
import igraph as ig
import PZ
import PS
import PW
import signal

result: list[int] = []

def uaktualnij_rozwiazanie(rozwiazanie: list[int]):
    result = rozwiazanie

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
    
    print_result()
    
    # PW.PW(G, result)

def print_result():
    for v in result:
        print("%d\n"%(v+1))

def exit(signum, frame):
    print_result()
    exit()

    

  

