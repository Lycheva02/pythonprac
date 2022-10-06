from math import *
def Calc(s,t,u):
    def h(x):
        r = (lambda x: eval(s))(x)
        y = (lambda x: eval(t))(x)
        return (lambda x, y: eval(u))(r, y)
    return h

a = eval(input())
x = eval(input())
F = Calc(a[0], a[1], a[2])
print(F(x))
