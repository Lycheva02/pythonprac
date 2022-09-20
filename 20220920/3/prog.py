n = int(input())
i = n
while i <= n+2:
    j = n
    while j <= n+2:
        p = i*j
        s = 0
        while p:
            s += p%10
            p //= 10
        if s == 6:
            print(i, ' * ', j, ' = :=)', end = ' ')
        else:
            print(i, ' * ', j, ' = ', i*j, end = ' ')
        j += 1
    print('\n')
    i += 1
