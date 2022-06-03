from math import sqrt
from igraph import *
import numpy as np
import PZ
import random
import generating as gen
import parser
import timeit
import csv

path = "e_001"

def Count(v: int, g: Graph):
    return MakeStep(g, [], v, v)

def MakeStep(g: Graph, visited: list, v: int, target: int):
    result = 0
    for w in g.neighbors(v, "out"):
        if w == target:
            result += 1
        elif w not in visited:
            visited.append(w)
            result += MakeStep(g, visited, w, target)
            visited.remove(w)
    return result

def CountAllCycles(g: Graph):
    result = []
    for i in range(g.vcount()):
        print("vert: ", i)
        result.append(Count(i, g))
    result_sum = sum(result)
    # for i in range(len(result)):
    #     result[i] = result[i] / result_sum
    return result

def ExactPS(g: Graph):
    res = CountAllCycles(g)
    print(res)
    return np.argmax(res)

def FullPS(g: Graph, walks: int):
    visit_count = [0 for _ in range(g.vcount())]
    curr_v = random.randint(0, g.vcount()-1)
    
    for j in range(walks):
        curr_v = random.randint(0, g.vcount()-1)
        for i in range(g.vcount()): 
            visit_count[curr_v] += 1
            if(g.vs[curr_v].outdegree()==0): return []
            next_step = random.randint(0, g.vs[curr_v].outdegree()-1)
            curr_v = g.neighbors(curr_v, "out")[next_step]

    # for i in range(len(visit_count)):
    #     visit_count[i] = visit_count[i] / steps

    return visit_count

main_result = []

def QuickExact(g: Graph):
    global main_result 
    main_result = [0 for _ in range(g.vcount())]
    for i in range(g.vcount()):
        print("vert: ", i)
        MakeQuickStep(g, [], i, i)
    return main_result

def MakeQuickStep(g: Graph, visited: list, v: int, target: int):
    global main_result
    result = 0
    for w in g.neighbors(v, "out"):
        if w == target:
            result += 1
        elif w not in visited and w > target:
            visited.append(w)
            result += MakeQuickStep(g, visited, w, target)
            visited.remove(w)
    main_result[v] += result
    return result

if __name__ == "__main__":
    (g, opt) = gen.GenerateRandomGraph(100, 20, 10)
    PZ.rozpocznij(g)
    

    walks = [1, 10, 100, 1000, 10000]
    res = []

    #res.append(QuickExact(g))
    for walk in walks:
        print(walk)
        res.append(FullPS(g, walk))
    
    sums = []
    for result in res:
        sums.append(sum(result))

    r = []
    for i in range(len(res[0])):
        r.append( [res[j][i]/sums[j] for j in range(1, len(res))] )

    r.sort(key=lambda x: x[-1])
    # for i in range(len(r)):
    #     text = str(res[0][i]) + ","
    #     for el in r[i]:
    #         text = text + str(el) + ","
    #     text = text[:-2]
    #     print(text)
    with open("plot.csv", 'w') as file:
        writer = csv.writer(file)
        for i in range(len(r)):
            writer.writerow(r[i])
    print(opt)


