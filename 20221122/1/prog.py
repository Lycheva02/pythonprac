import sys

s = sys.stdin.buffer.read()
n = s[0]
other = s[1:]
l = len(other)

parts = list()
for i in range(n):
    parts.append(other[i*l//n:(i+1)*l//n])

ans = s[:1] + b''.join(sorted(parts))
sys.stdout.buffer.write(ans)
