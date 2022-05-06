import re
from igraph import *

best_solution: list[str]


def PW(G: Graph, solution: list[str]) -> list[str]:
    global best_solution
    best_solution = solution
    _PW(G, solution, [])  # not optimal (graph copy, other?)
    return best_solution


def _PW(G: Graph, solution: list[str], musthaves: list[str]):
    global best_solution
    for v in solution:
        if v in musthaves:
            continue
        new_solution = solution.copy()  # or that?
        new_solution.remove(v)  # and that
        g = (
            G.copy()
        )  # TODO: don't do that! extremaly slow and leaks huge memory. (remove and put back instead)
        g.delete_vertices(new_solution)
        if not g.is_dag():
            musthaves.append(v)
        else:
            if len(best_solution) > len(new_solution):
                print('New best solution, len: {}'.format(len(new_solution)))
                best_solution = new_solution
            _PW(G, new_solution.copy(), musthaves.copy())
