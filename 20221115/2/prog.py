class Num:
    def __set__(self, obj, val):
        if 'real' in dir(val):
            obj._num = val
        else:
            obj._num = len(val)
    def __get__(self, obj, cls):
        try:
            return obj._num
        except AttributeError:
            return 0

import sys
exec(sys.stdin.read())
