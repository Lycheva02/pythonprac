a = list(eval(input()))
keys = []
for i in a:
    keys.append(i*i % 100)
n = len(a)

for i in range(n):
    for j in range(n-i-1):
        if keys[j] > keys[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            keys[j], keys[j+1] = keys[j+1], keys[j]

print(a)
