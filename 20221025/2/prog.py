from itertools import *

def slide(seq, n):
    i, j = tee(iter(seq))
    while True:
        yield from islice(i, n)
        try:
            c = next(j)
            i, j = tee(j)
        except:
            break

import sys
exec(sys.stdin.read())
    
