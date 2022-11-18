def objcount(cls):
    cls.counter = 0
    cls.___init___ = cls.__init__
    def fun(self, *args, **kwargs):
        cls.counter += 1
        cls.___init___(self, *args, **kwargs)
    cls.__init__ = fun
    try:
        cls.___del___ = cls.__del__
    except:
        cls.___del___ = lambda x: None
    def f(self):
        cls.counter -= 1
        cls.___del___(self)
    cls.__del__ = f
    return cls

import sys
exec(sys.stdin.read())
