w = int(input())

d = {}

while (s := input()):
    for i in range(len(s)):
        if not s[i].isalpha():
            s = s[:i] + ' ' + s[i+1:]
    s = s.lower()
    s = s.split()
    for i in s:
        if len(i) == w:
            d[i] = d.get(i, 0) + 1

ans = []
m = max(d.values())

for i in d:
    if d[i] == m:
        ans.append(i)

ans.sort()
print(*ans)
