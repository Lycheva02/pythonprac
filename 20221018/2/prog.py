from math import *
import copy

def quit(s):
    print(s.format(len(s_fun), k))

s_fun = {'quit': quit}
k = 0

while True:
    k += 1
    sv = input()
    s = sv.split()
    if s[0] == 'quit':
        s = sv[6:-1]
        quit(s)
        break
    if s[0][0] == ':':
        s[0] = s[0][1:]
        def f(args, s = s):
            d = {}
            t = s[1:-1]
            n = 0
            for i in t:
                d[i] = eval(args[n])
                n += 1
            return (lambda: eval(s[-1], globals(), d))()
        s_fun[s[0]] = f
        continue
    print((s_fun[s[0]])(s[1:]))
        
        
        
