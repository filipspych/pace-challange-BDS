# UI component
# czyli PZ udostępnia PZ.getGrafPoNastepnejIteracji(int wierzcholekONajwikszeCyklowosci),
# PS udostępnia PS.getWierzcholekONajwiekszejCyklowosci(G)
# dodatkowo PZ.rozpocznij(G) który resetuje PZ i przekazuje PZ że teraz PZ będzie pracowało na grafie G

from igraph import *
import PZ
import PS
import plot
import generating as gen
import opt
import time
import PW
import random

initialG: Graph = Graph()
def InitializeProcedure(G: Graph, skip = False):
    global initialG
    initialG = G.copy()
    PZ.rozpocznij(G)
    result: list[int] = []
    g: Graph = G.copy()
    # OPT = opt.getMFVSDokladny(G)

    while(g.vcount() > 0):
        if (not skip):
            print('-------------------------------')
            print('i - next iteration')
            print('p - show graph')
            print('r - show current result')
            print('s - skip iterations')
            x = input()
            match x:
                case 'i':
                    print('next iteration')
                    g = NextStep(result, g)
                case 'p':
                    print('showing plot')
                    plot.plotGraph(g)
                case 'r':
                    print('Current result:' + str(result))
                case 's':
                    skip = True
        else:
            g = NextStep(result, g)
    result = list(map(int,PW.PW(initialG, list(map(str, result)))))
    print('Size of found feedback vertex set: ' + str(len(result)))
    # x = input('If you want to compare with optimal solution, press \'o\'...')
    # print('Size of minimal feedback vertex set: ' + str(len(OPT)))
    # if (x == 'o'):
    #     OPT = opt.getMFVSDokladny(G)    
    #     print('Size of minimal feedback vertex set: ' + str(len(OPT)))


def NextStep(result, G):
    v = PS.PS(G)
    # v = random.randint(0, G.vcount() - 1)
    result.append(G.vs[v]["name"])
    return PZ.getGrafPoNastepnejIteracji(v)


for i in range(10):
    (g, OPT) = gen.GenerateRandomGraph(10000, 10, 200)
    g.vs["name"] = [str(i) for i in range(g.vcount())]
    start = time.time()
    InitializeProcedure(g.copy(), True)
    end = time.time()
    print('time elapsed: ' + str(end - start))

