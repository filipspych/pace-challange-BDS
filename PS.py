from igraph import *
import numpy as np
import random


def PS(g: Graph):
    '''zakladam ze dostaje silnie spojna skladowa bez wierzcholkow w ktorych mozna utknac, 
    jesli nie przerywam prace na tym etapie na ktorym jest program i zwracam pusta tablice'''
    visit_count = [0 for _ in range(g.vcount())]
    curr_v = random.randint(0, g.vcount()-1)
    

    for i in range(g.vcount()* 1000): #na razie pozniej bedziemy testowac jakies metody wyznaczania tej wartosci
        visit_count[curr_v] += 1
        if(g.vs[curr_v].outdegree()==0): return []
        next_step = random.randint(0, g.vs[curr_v].outdegree()-1)
        (a, b) = g.es.select(_source=curr_v)[next_step].tuple
        if(a!=curr_v): curr_v = a
        else: curr_v = b
    # print(visit_count)
    return np.argmax(visit_count)


PS(Graph.Full(10))