from itertools import *

print(*list(filter(lambda x: x.count('TOR') == 2, list(map(''.join, list(product('ORT', repeat = int(input()))))))), sep = ', ')
