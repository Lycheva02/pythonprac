from collections import UserString
import sys

class DivStr(UserString):
    def __init__(self, s=""):
        self.data = s

    def __floordiv__(self, n):
        k = len(self.data) // n
        seq = [self.data[i * k:i * k + k] for i in range(n)]
        return iter(seq)

    def __mod__(self, n):
        k = len(self.data) % n
        if k == 0:
            return (DivStr())
        return DivStr(self.data[-k:])


exec(sys.stdin.read())
