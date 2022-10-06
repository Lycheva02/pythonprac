def Pareto(pair):
    a = []
    for i in pair:
        f = True
        for j in pair:
            if (i[0] <= j[0]) and (i[1] <= j[1]):
                if (i[0] < j[0]) or (i[1] < j[1]):
                    f = False
                    break
        if f:
            a.append(i)
    return tuple(a)

print(Pareto(list((eval(input())))))
