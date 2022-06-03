from igraph import *
import igraph as ig
import sys
from typing import List
import numpy as np
import random
import signal
from datetime import datetime

def parse(filePath="") -> Graph:
    if filePath != "":
        with open(filePath) as f:
            return __parse(iter(f.readlines()))
    else:
        return __parse(iter(sys.stdin))

def read_line(iterator) -> list[int]:
    return list(map(lambda x: int(x), skip_comments(iterator).split()));

def skip_comments(iterator) -> str:
    line = next(iterator)
    # print(line)
    while line[0] == '%':
        line = next(iterator)
    return line

def __parse(iterator) -> Graph:
    line = read_line(iterator)
    n = line[0]
    edge_list = []
    for i in range(n):
        edge_list = edge_list + [(i, v-1) for v in read_line(iterator)]
        # print("Line number")
        # print(i)
        # print()
        # if i % 1000 == 0:
        #     print(i)
    return Graph(n=n, edges=edge_list, directed=True, vertex_attrs={"name": list(map(str, [i for i in range(n)]))})
    

def rozpocznij(g: Graph):
    """Resetuje PZ i ustawia g jako aktualnie przetwarzany graf.
    Uwaga: zwrocony tutaj graf ulegnie zmianom po kazdym
    wykonaniu getGrafPoNastepnejIteracji(). To protect your
    graph g from changing, you have to pass g.copy()."""
    global _g
    _g = g
    _urdzennij()


def getGrafPoNastepnejIteracji(wierzcholekONajwikszeCyklowosci: int) -> Graph:
    """Uwaga, graf jest zwracany przez referencję i ulegnie zmianom
    po kazdym wykonaniu getGrafPoNastepnejIteracji(). To keep immutable 
    graph, you have to do g.copy(). 
    Jezeli PZ ma graf pusty, to ta metoda nic nie robi."""
    if _g.vcount() == 0:
        return _g
    _g.delete_vertices(wierzcholekONajwikszeCyklowosci)
    _urdzennij()
    return _g


def _urdzennij():
    """Jezeli PZ ma graf pusty, to ta metoda nic nie robi."""
    if _g.vcount() == 0:
        return _g
    usuwaneWierzcholki: List[int] = [-1]
    while len(usuwaneWierzcholki) > 0 and _g.vcount() > 0:
        # czytelniej by bylo to zrobic selectem _g.vs.select(_indegree_eq=0)...
        usuwaneWierzcholki = np.where(
            np.logical_or(
                np.asarray(_g.indegree()) == 0, np.asarray(_g.outdegree()) == 0
            )
        )[0]
        _g.delete_vertices(usuwaneWierzcholki)



def PS(g: Graph):
    '''zakladam ze dostaje silnie spojna skladowa bez wierzcholkow w ktorych mozna utknac, 
    jesli nie przerywam prace na tym etapie na ktorym jest program i zwracam pusta tablice'''
    visit_count = [0 for _ in range(g.vcount())]
    curr_v = random.randint(0, g.vcount()-1)
    

    for i in range(g.vcount() * 1): #na razie pozniej bedziemy testowac jakies metody wyznaczania tej wartosci
        visit_count[curr_v] += 1
        if(g.vs[curr_v].outdegree()==0): return []
        next_step = random.randint(0, g.vs[curr_v].outdegree()-1)
        (a, b) = g.es.select(_source=curr_v)[next_step].tuple
        if(a!=curr_v): curr_v = a
        else: curr_v = b
    # print(len(visit_count))
    return np.argmax(visit_count)

#PS(Graph.Full(10))

should_end=None

def sigterm_handler(signum, frame):
    global should_end
    should_end = datetime.datetime.now()

signal.signal(signal.SIGTERM, sigterm_handler)
# print("stawiono handler sygnału")

def end_with_result(result):
    for v in result:
        print("%d"%(int(v)+1))
    exit()

def run(path: str="") -> tuple[int, int, list[int]]:
    G: ig.Graph = parse(path)
    g: ig.Graph = G.copy()
    result: list[int] = []
    n = G.vcount()
    m = G.ecount()
    rozpocznij(g)
    # print("rozpoczęto procedurę")
    while(g.vcount() > 0):
        v = PS(g)
        # print(v)
        result.append(g.vs[v]["name"])
        g = getGrafPoNastepnejIteracji(v)    
    # print("Zakończono PZ")
    # PW.PW(G, list(map(str,result)))
    return (n, m, result)

def return_result(path: str="") -> list[int]:
    return run(path)[2]

if __name__ == "__main__":
    result = return_result()
    end_with_result(result)
