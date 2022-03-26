from typing import List
from igraph import *
import numpy as np
from itertools import chain, combinations

def getMFVSDokladny(g: Graph) -> List[int]:
    """Zwraca liste wierzcholkow bedacych optymalnym rozwiazaniem (MVFS). 
    Nie modyfikuje g."""
    g = g.copy()
    vertices: List[int] = range(g.vcount())
    pset = _powerset(vertices)
    mfvs = vertices
    for set in pset:
        if _isFVS(g, set) and len(mfvs) > len(set):
            mfvs = set
    return mfvs
    
def _isFVS(g: Graph, set: List[int]):
    g = g.copy()
    g.delete_vertices(set)
    return g.is_dag()

def _powerset(s):
    x = len(s)
    ret: List[List[int]] = []
    for i in range(1 << x):
        ret.append([s[j] for j in range(x) if (i & (1 << j))])
    return ret