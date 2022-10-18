s = input().lower()
d = {}
for i in range(len(s) - 1):
    if not(s[i].isalpha() and s[i+1].isalpha()):
        continue
    ind = s[i] + s[i + 1]
    d[ind]  = d.get(ind, 0) + 1
print(len(d))
