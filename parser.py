from igraph import *
import sys

def parse(filePath="", from_file=False) -> Graph:
    if from_file:
        with open(filePath) as f:
            return __parse(iter(f.readlines()))
    else:
        return __parse(iter(sys.stdin))

def read_line(iterator) -> list[int]:
    return list(map(lambda x: int(x), skip_comments(iterator).split(" ")));

def skip_comments(iterator) -> str:
    line = next(iterator)
    while line[0] == '%':
        line = next(iterator)
    return line

def __parse(iterator) -> Graph:
    line = read_line(iterator)
    n = line[0]
    edge_list = []
    for i in range(n):
        for v in read_line(iterator):
            edge_list.append((i, v-1))
    return Graph(n=n, edges=edge_list, directed=True, vertex_attrs={"index": [i for i in range(n)]})