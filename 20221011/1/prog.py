from fractions import *

def fun(s, w, n, a, m, b):
    A = 0
    for i in range(n, -1, -1):
        A += a[n - i] * s**i
    B = 0
    for i in range(m, -1, -1):
        B += b[m - i] * s**i
    if B == 0:
        return False
    if A == B*w:
        return True
    return False

st = list(map(Fraction, input().split(',')))
s, w = st[0], st[1]
n = int(st[2])
a = st[3:4+n]
m = int(st[4+n])
b = st[5+n:]

print(fun(s, w, n, a, m, b))

