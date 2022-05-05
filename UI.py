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
    g: Graph = G.copy()
    skip = False
    OPT = opt.getMFVSDokladny(G)
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
            
    print('Size of found feedback vertex set: ' + str(len(result)))
    # x = input('If you want to compare with optimal solution, press \'o\'...')
    print('Size of minimal feedback vertex set: ' + str(len(OPT)))
    # if (x == 'o'):
    #     OPT = opt.getMFVSDokladny(G)    
    #     print('Size of minimal feedback vertex set: ' + str(len(OPT)))


def NextStep(result, G):
    v = PS.PS(G)
    result.append(v)
    return PZ.getGrafPoNastepnejIteracji(v)

(g, OPT) = gen.GenerateRandomGraph(30, 3)
print(OPT)
InitializeProcedure(g)
