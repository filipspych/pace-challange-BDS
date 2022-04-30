from typing import Iterator
from igraph import *

def parse(filePath: str) -> Graph:
    with open(filePath) as f:
        return __parse(f)

def __parse(stream) -> Graph:
    a = stream.next().split(" ")
    
