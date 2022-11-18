class Alpha:
    __slots__ = list('abcdefghijklmnopqrstuvwxyz')
    def __init__(self, **kwargs):
        for i in kwargs:
            setattr(self, i, kwargs[i])
    def __str__(self):
        res = ''
        for i in self.__slots__:
            try:
                ch = getattr(self, i)
            except AttributeError:
                pass
            else:
                if res != '':
                    res += ', '
                res += f"{i}: {ch}"
        return res

class AlphaQ:
    d = dict()
    s = 'abcdefghijklmnopqrstuvwxyz'
    def __init__(self, **kwargs):
        for i in kwargs:
            if i in self.s:
                self.d[i] = kwargs[i]
            else:
                raise AttributeError()
    def __getattr__(self, key):
        if key in self.d:
            return self.d[key]
        else:
            raise AttributeError()
    def __setattr__(self, key, val):
        if key in self.s:
            self.d[key] = val
        else:
            raise AttributeError()
    def __str__(self):
        res = ''
        for i in self.s:
            if i in self.d:
                if res != '':
                    res += ', '
                res += f"{i}: {self.d[i]}"
        return res
                
import sys
exec(sys.stdin.read())

            
