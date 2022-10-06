def sub(x, y):
    if type(x) == list or type(x) == tuple:
        a = []
        for i in x:
            f = True
            for j in y:
                if i == j:
                    f = False
                    break
            if f:
                a.append(i)
        if type(x) == tuple:
            a = tuple(a)
        return a
    return x - y


vv = eval(input())
print(sub(vv[0], vv[1]))
