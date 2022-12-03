import inspect

def dump_meth(nm, meth):
    def new_meth(self, *args, **kwargs):
        print(f"{nm}: {args}, {kwargs}")
        return meth(self, *args, **kwargs)
    return new_meth 

class dump(type):
    def __new__(meta, name, par, ns):
        cls = super().__new__(meta, name, par, ns)
        for nm, meth in inspect.getmembers(cls, inspect.isfunction):
            setattr(cls, nm, dump_meth(nm, meth))
        return cls

import sys
exec(sys.stdin.read())
