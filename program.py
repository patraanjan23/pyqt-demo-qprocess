import threading
import sys
from time import sleep

def print_num(odd=True):
    for x in range(50):
        if odd:
            if x % 2 == 1:
                print(x, flush=True)
                sleep(0.5)
        else:
            if x % 2 == 0:
                print(x, file=sys.stderr, flush=True)
                sleep(0.5)

if __name__ == "__main__":
    t1 = threading.Thread(target=print_num, args=(True,))
    t2 = threading.Thread(target=print_num, args=(False,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()