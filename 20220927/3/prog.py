A = []
B = []
a = list(eval(input()))
n = len(a)
A.append(a)

for i in range(n-1):
    A.append(list(eval(input())))
for i in range(n):
    B.append(list(eval(input())))

C = []

for i in range(n):
    ans = []
    for j in range(n):
        c = 0
        for k in range(n):
            c += A[i][k]*B[k][j]
        ans.append(c)
    C.append(ans)

for row in C:
    print(*row, sep = ',')
