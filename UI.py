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


def InitializeProcedure(G: Graph):
    PZ.rozpocznij(G)
    result: list[int] = []
    g: Graph = G
    OPT = opt.getMFVSDokladny(G.copy())
    while(g.vcount() > 0):
        print('-------------------------------')
        print('i - next iteration')
        print('p - show graph')
        print('r - show current result')
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
    print('Size of found feedback vertex set: ' + str(len(result)))
    print('Size of minimal feedback vertex set: ' + str(len(OPT)))


def NextStep(result, G):
    v = PS.PS(G)
    result.append(v)
    return PZ.getGrafPoNastepnejIteracji(v)

(g, OPT) = gen.GenerateRandomGraph(8, 2)
print(OPT)
InitializeProcedure(g)
