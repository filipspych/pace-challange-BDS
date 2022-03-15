import igraph as ig
import random
# n - number of nodes in graph
# k - the size of optimum DFVS solution. k <= n/2
# ed - edge density (m=ed*n)
# return - random graph with secified parameters
def GenerateRandomGraph(n, k, ed):
    # stwórz losowe drzewo o n wierzchołkach
    graph = ig.Graph.Tree_Game(n, directed=True)

    # wylosuj wierzchołki, które mają należeć to OPT
    OPT =  random.sample(range(n), k)

    # wygeneruj k wierzchołkowo-niezależnych cykli. (nie liczą się pętelki) 
    # Czyli na każdy wybrany wierzchołek musi przypadać
    # dokładnie jeden cykl. 
    generateNodeIndependentCycles(OPT)

def generateNodeIndependentCycles(graph: ig.Graph, OPT):
    # Ze zbióru wierzchołków, które nie są w OPT należy wybrać k rozłącznych niepustych podzbiorów.
    #   Wylosuj k liczb z zakresu od 0 do n-k-1.
    separators = random.sample(range(1, graph.vcount + 1), len(OPT))
    separators.append(0)
    separators.sort()
    #   Stwórz permutację podciągów, które nie są w OPT.
    permutation = [x for x in range(graph.vcount) if x not in OPT]
    random.shuffle(permutation)
    #   Stwórz listę list zawierających cykle odpowiadające wierzchołkom z OPT
    cycles = [permutation[separators[i-1]:separators[i]] for i in range(1, len(OPT) + 1)]
    #   Stwórz każdy z cykli w grafie
    i = 0
    for cycle in cycles:
        cycle.append(OPT[i])
        graph.add_edges([(i, (i + 1) % len(cycle)) for i in range(len(cycle))])
        i += 1
