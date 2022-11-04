from collections import Counter

class Omnibus:
    d = Counter()
    attrs = {}
    def __init__(self):
        self.attrs[id(self)] = list()
    def __setattr__(self, key, value):
        if key.startswith('_'):
            return
        if key not in self.attrs[id(self)]:
            self.attrs[id(self)] +=  [key]
            self.d[key] += 1
    def __getattr__(self, name):
        if name in self.attrs[id(self)]:
            return self.d[name]
    def __delattr__(self, attr):
        if attr not in self.attrs[id(self)]:
            return
        self.d[attr] -= 1
        self.attrs[id(self)].remove(attr)
        if self.d[attr] == 0:
            self.d.pop(attr)

import sys
exec(sys.stdin.read())
