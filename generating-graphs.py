import igraph as ig
import random
# n - number of nodes in graph
# k - the size of optimum DFVS solution. k <= n/2
# ed - edge density (m=ed*n)
# return - random graph with secified parameters
def GenerateRandomGraph(n, k, ed=0):
    # stwórz losowe drzewo o n wierzchołkach
    graph = ig.Graph.Tree_Game(n, directed=True)
    ig.plot(graph, vertex_label=[str(i) for i in range(n)])
    # wylosuj wierzchołki, które mają należeć to OPT
    OPT =  random.sample(range(n), k)

    topologicalOrder = [i for i in graph.topological_sorting() if i not in OPT]

    # wygeneruj k wierzchołkowo-niezależnych cykli. (nie liczą się pętelki) 
    # Czyli na każdy wybrany wierzchołek musi przypadać
    # dokładnie jeden cykl. 
    generateNodeIndependentCycles(graph, OPT, n)
    return (graph, OPT)

def generateNodeIndependentCycles(graph: ig.Graph, OPT, n):
    # Ze zbióru wierzchołków, które nie są w OPT należy wybrać k rozłącznych niepustych podzbiorów.
    #   Wylosuj k liczb z zakresu od 0 do n-k-1.
    separators = random.sample(range(1, 1 + n), len(OPT))
    separators.append(0)
    separators.sort()
    print("separators" + str(separators))
    #   Stwórz permutację podciągów, które nie są w OPT.
    permutation = [x for x in range(n) if x not in OPT]
    print(permutation)
    random.shuffle(permutation)
    print(permutation)
    #   Stwórz listę list zawierających cykle odpowiadające wierzchołkom z OPT
    cycles = [permutation[separators[i-1]:separators[i]] for i in range(1, len(OPT) + 1)]
    #   Stwórz każdy z cykli w grafie
    i = 0
    for cycle in cycles:
        cycle.append(OPT[i])
        graph.add_edges([(cycle[v], cycle[(v + 1) % len(cycle)]) for v in range(len(cycle))])
        i += 1
