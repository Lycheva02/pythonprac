import inspect
import types

class check(type):
    def __new__(meta, nm, par, ns):
        def ch_an(self):
            for nm, tp in inspect.get_annotations(self.__class__).items():
                if nm not in dir(self):
                    return False
                if isinstance(tp, types.GenericAlias):
                    tp = tp.__origin__
                if not isinstance(getattr(self, nm), tp):
                    return False
            return True
        cls = super().__new__(meta, nm, par, ns)
        cls.check_annotations = ch_an
        return cls

import sys
exec(sys.stdin.read())
