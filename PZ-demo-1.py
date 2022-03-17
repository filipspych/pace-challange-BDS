import shlex
import os
import tempfile
from sys import platform
from re import template
from igraph import *

# Sprawdzam czy jesteśmy na windowsie
winda: bool = True if platform == "win32" else False

# Demko UI z przegladarka
filename = tempfile.NamedTemporaryFile(suffix=".svg").name

t: Graph = Graph.Tree(16, 7, type="out")
for i in range(8):
    t.delete_vertices(0)
    print(t)
    # filename=tempfile.NamedTemporaryFile(suffix='.svg').name #  kompatybilnosc z inkspace + pozwala zachowac ten graf do konca wykonywania programu
    input("Kliknij ENTER...")
    t.write_svg(fname=filename)
    # plot(t)
    if winda:
        os.system("start " + filename)  # windows
    else:
        os.system("open " + shlex.quote(filename))  # MacOS/X

s: str = ""
while s != "usun":
    s = input(
        "Koniec. Wpisz 'usun', zeby skasowac obrazki grafow z pamieci komputera: "
    )

# zakonczenie programu usuwa pliki tymczasowe
print("Usuwam pliki tymczasowe...")
