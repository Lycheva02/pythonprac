m, n = eval(input())
print([i for i in range(m,n) if all(i%j for j in range(2,i))])
