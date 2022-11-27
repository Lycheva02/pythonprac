import sys
s = bytes(sys.stdin.read(), encoding='utf8')
s = s.decode('utf8')
s = s.encode('latin1')
s = s.decode('cp1251')
print(s)
