import signal
from datetime import datetime

should_end=None
result=[]

def sigterm_handler(signum, frame):
    should_end = datetime.datetime.now()

def uaktualnij_rozwiazanie(rozwiazanie: list[int]):
    result = rozwiazanie

signal.signal(signal.SIGTERM, sigterm_handler)

def end_with_result():
    for v in result:
        print("%d"%(v+1))
    exit()