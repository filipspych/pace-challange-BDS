import re
from igraph import *

best_solution: list[int]


def PW(G: Graph, solution: list[int]) -> list[int]:
    global best_solution
    best_solution = solution
    _PW(G, solution, [])  # not optimal (graph copy, other?)
    return best_solution


def _PW(G: Graph, solution: list[int], musthaves: list[int]):
    global best_solution
    for v in solution:
        if v in musthaves:
            return
        new_solution = solution.copy()  # or that?
        new_solution.remove(v)  # and that
        g = (
            G.copy()
        )  # TODO: don't do that! extremaly slow and leaks huge memory. (remove and put back instead)
        print(new_solution)
        print(list(map(str, new_solution)))
        g.delete_vertices(list(map(str, new_solution)))
        if g.is_connected(mode="strong"):
            musthaves.append(v)
            _PW(G, solution, musthaves.copy())
        else:
            if len(best_solution) > len(solution):
                best_solution = solution
            _PW(g, new_solution.copy(), musthaves.copy())
