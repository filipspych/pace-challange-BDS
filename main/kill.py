import signal
from datetime import datetime

should_end=None

def sigterm_handler(signum, frame):
    should_end = datetime.datetime.now()

signal.signal(signal.SIGTERM, sigterm_handler)
# print("stawiono handler sygnału")

def end_with_result(result):
    for v in result:
        print("%d"%(int(v)+1))
    exit()