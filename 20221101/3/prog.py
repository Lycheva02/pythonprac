from math import log

class Grange:
    def __init__(self, b0, q, bn):
        self.b0 = b0
        self.q = q
        self.bn = bn
    def __len__(self):
        if self.bn <= self.b0:
            return 0
        return int(log((self.bn-1)/self.b0, self.q)) + 1
    def __bool__(self):
        return len(self) != 0
    def __getitem__(self, var):
        if isinstance(var, slice):
            if var.step:
                q = self.q**var.step
            else:
                q = self.q
            return Grange(var.start, q, var.stop)
            
        return self.b0 * self.q**var
    def __iter__(self):
        return iter([self.b0 * self.q**i for i in range(len(self))])
    def __str__(self):
        return f"grange({self.b0}, {self.q}, {self.bn})"
    def __repr__(self):
        return f"grange({self.b0}, {self.q}, {self.bn})"


import sys
exec(sys.stdin.read())
