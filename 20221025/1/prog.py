def fib(m, n):
    x, y = 1, 1
    if m == 0:
        yield x
        m += 1
        n -= 1
    if m == 1:
        yield y
        m += 1
        n -= 1
    for i in range(2, m):
        x, y = y, x + y
    for i in range(m, m + n):
        x, y = y, x + y
        yield y

import sys
exec(sys.stdin.read())
