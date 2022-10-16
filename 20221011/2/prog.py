from math import *

def f(s):
    def h(x):
        return (lambda x: eval(s))(x)
    return h

s = input().split()
w, h, a, b = int(s[0]), int(s[1]), float(s[2]), float(s[3])
fun = f(''.join(s[4:]))

screen = [[' ' for i in range(w)] for j in range(h)]

s = []

# строим таблицу значений и ищем максимум и минимум
x = a
st = (b - a)/w
while x < b:
    s.append([x, fun(x)])
    x += st
fmax = max(s, key = lambda x: x[1])[1]
fmin = min(s, key = lambda x: x[1])[1]

k = (fmax - fmin)/h

for i in s:
    x = int((i[0] - a)/st)
    if x == w:
        x -= 1
    y = int((i[1] - fmin)/k)
    if x != 0:
        for j in range(min(h - y - 1, yp) + 1, max(h - y - 1, yp)):
            screen[j][x] = '*'
    if y == h:
        screen[0][x] = '*'
        yp = 0
        continue
    screen[h - y - 1][x] = '*'
    yp = h - y - 1

for l in screen:
    print(''.join(l))
