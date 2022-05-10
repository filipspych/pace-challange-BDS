from igraph import *
import numpy as np
import random

def PS(g: Graph):
    '''zakladam ze dostaje silnie spojna skladowa bez wierzcholkow w ktorych mozna utknac, 
    jesli nie przerywam prace na tym etapie na ktorym jest program i zwracam pusta tablice'''
    visit_count = [0 for _ in range(g.vcount())]
    curr_v = random.randint(0, g.vcount()-1)
    return curr_v

    # for i in range(int(g.vcount()* 1)): 
    #     visit_count[curr_v] += 1
    #     if(g.vs[curr_v].outdegree()==0): return []
    #     next_step = random.randint(0, g.vs[curr_v].outdegree()-1)
    #     curr_v = g.neighbors(curr_v, "out")[next_step]
    # print(len(visit_count))
    # return np.argmax(visit_count)


