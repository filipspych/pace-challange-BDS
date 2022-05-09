from math import sqrt
from igraph import *
import numpy as np
import PZ
import random
import generating as gen
import parser

path = "e_001"

def Count(v: int, g: Graph):
    return MakeStep(g, [], v, v)

def MakeStep(g: Graph, visited: list, v: int, target: int):
    result = 0
    for w in g.neighbors(v, "out"):
        if w == target:
            result += 1
        if w not in visited:
            visited.append(w)
            result += MakeStep(g, visited, w, target)
            visited.remove(w)
    return result

def CountAllCycles(g: Graph):
    result = []
    for i in range(g.vcount()):
        #print("vert: ", i)
        result.append(Count(i, g))
    result_sum = sum(result)
    # for i in range(len(result)):
    #     result[i] = result[i] / result_sum
    return result

def ExactPS(g: Graph):
    res = CountAllCycles(g)
    print(res)
    return np.argmax(res)

def FullPS(g: Graph):
    visit_count = [0 for _ in range(g.vcount())]
    curr_v = random.randint(0, g.vcount()-1)
    
    walks = 1000
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

if __name__ == "__main__":
    (g, opt) = gen.GenerateRandomGraph(50, 10, 10)
    PZ.rozpocznij(g)
    
    r1 = CountAllCycles(g)
    r2 = FullPS(g)

    r = []

    for i in range(len(r1)):
        r.append( [r1[i], r2[i], i] )

    r.sort(key=lambda x: x[1])
    for i in range(len(r)):
        print(r[i])
    print(opt)


