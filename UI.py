# UI component
# czyli PZ udostępnia PZ.getGrafPoNastepnejIteracji(int wierzcholekONajwikszeCyklowosci),
# PS udostępnia PS.getWierzcholekONajwiekszejCyklowosci(G)
# dodatkowo PZ.rozpocznij(G) który resetuje PZ i przekazuje PZ że teraz PZ będzie pracowało na grafie G
import igraph as ig


def InitializeProcedure(G):
    # PZ.rozpocznij(G)
    result = []
    g = G
    while(True):
        print('--------------------')
        print('i - next iteration')
        print('p - show graph')
        x = input()
        match x:
            case 'i':
                print('next iteration')
                # g = NextStep(result, g)
            case 'p':
                print('showing plot')
                # ig.plot(g)


def NextStep(result, G):
    v = PS.getWierzcholekONajwiekszejCyklowosci(G)
    result.append(v)
    return PZ.getGrafPoNastepnejIteracji(v)

InitializeProcedure(5)
