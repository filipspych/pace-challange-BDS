from typing import List
from igraph import *
import numpy as np


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
    po kazdym wykonaniu getGrafPoNastepnejIteracji(). To protect
    your graph g from changing, you have to pass g.copy(). Jezeli
    PZ ma graf pusty, to ta metoda nic nie robi."""
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
