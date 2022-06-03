import main
import os
import time

def run_test(path: str):
    # print('Testing instance from file: ' + path)
    start = time.time()
    (n, m, result) = main.run(path)
    end = time.time()
    # print("n = %d, m = %d, len(result) = %d, time = %f s"%(n, m, len(result), end - start))
    print("%s,%d,%d,%d,%f"%(os.path.basename(path), n, m, len(result), end - start))

if __name__=="__main__":
    directory = 'examples/heuristic_public'
    test = False
    for filename in os.listdir(directory):
        if filename == "h_073":
            test = True
        if test:
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                run_test(f)