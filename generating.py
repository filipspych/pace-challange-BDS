from calendar import c
from itertools import cycle
import igraph as ig
import random
import plot
# n - number of nodes in graph
# k - the size of optimum DFVS solution. k <= n/2
# ed - edge density (m=ed*n)
# return - random graph with secified parameters
def GenerateRandomGraph(n: int, k: int, ed: float):
    # stwórz losowe drzewo o n wierzchołkach
    graph = ig.Graph.Tree_Game(n, directed=True)
    # plot.plotGraph(graph)
    # wylosuj wierzchołki, które mają należeć to OPT
    OPT =  random.sample(range(n), k)

    # stwórz listę wierzchołków nie należących do rozwiązania. Lista posortowana topologicznie.
    notOPT = [i for i in graph.topological_sorting() if i not in OPT]
    for i in range(len(notOPT)):
        notOPT[i] = (i, notOPT[i])

    # wygeneruj k wierzchołkowo-niezależnych cykli. (nie liczą się pętelki) 
    # Na każdy wierzchołek z OPT musi przypadać
    # dokładnie jeden cykl. 
    generateNodeIndependentCycles(graph, OPT, notOPT)

    generateOverlappingCycles(graph, OPT, notOPT, ed)
    return (graph, OPT)

def generateOverlappingCycles(graph, OPT, notOPT, ed):
    while(graph.vcount() * ed > graph.ecount()):
        # print("generateOverlappingCycles")
        # wylosuj podzbiór z OPT oraz podzbiór z topologicalOrder
        fromOPT = random.sample(OPT, random.randint(1, len(OPT)))
        notFromOPT = random.sample(notOPT, random.randint(1, len(OPT)))
        addCycleToGraph(graph, fromOPT, notFromOPT)

def addCycleToGraph(graph: ig.Graph, fromOPT: list[int], notFromOPT: list[tuple]):
    # posortuj verticiesNotFromOPT względem porządku topologicznego
    notFromOPT.sort(key = lambda indexedVertex: indexedVertex[0])
    cycle = [el[1] for el in notFromOPT]

    # dodaj na koniec jeden wierzchołek z OPT
    cycle.append(fromOPT.pop())
    
    # losowo powsadzaj wierzchołki z fromOPT do notFromOPT
    indicies = [i for i in range(len(cycle))]
    for vertex in fromOPT:
        index = random.choice(indicies)
        cycle.insert(index, vertex)
        indicies.append(len(indicies))

    # Stwórz krawędzie pomiędzy kolejnymi wierzchołkami z verticiesNotFromOPT

    graph.add_edges([
        (cycle[v], cycle[(v + 1) % len(cycle)])
        for v in range(len(cycle))
        if not graph.are_connected(cycle[v], cycle[(v + 1) % len(cycle)])])


def generateNodeIndependentCycles(graph: ig.Graph, OPT, notOPT: list[tuple]):
    # Ze zbióru wierzchołków, które nie są w OPT należy wybrać k rozłącznych niepustych podzbiorów. W tym celu:
    # Wylosuj k liczb z zakresu od 0 do n-k-1.
    separators = random.sample(range(1, 1 + graph.vcount()), len(OPT))
    separators.append(0)
    separators.sort()
    # print("separators" + str(separators))
    # Stwórz permutację wiezchołków, które nie są w OPT.
    permutation = notOPT.copy()
    # print(permutation)
    random.shuffle(permutation)
    # print(permutation)
    # Stwórz listę list zawierających cykle odpowiadające wierzchołkom z OPT
    cycles = [permutation[separators[i-1]:separators[i]] for i in range(1, len(OPT) + 1)]
    #   Stwórz każdy z cykli w grafie
    i = 0
    for cycle in cycles:
        addCycleToGraph(graph, [OPT[i]], cycle)
        i += 1


#(g, OPT) = GenerateRandomGraph(4, 1)
#print("OPT = " + str(OPT))
#plot.plotGraph(g)
# ig.plot(g, vertex_label=[str(i) for i in range(8)])