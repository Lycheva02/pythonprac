import sys
import os
import gettext

def fun(s):
    popath = os.path.join(os.path.dirname(__file__), "po")
    translation = gettext.translation("counter", popath, fallback=True)
    _, ngettext = translation.gettext, translation.ngettext
    N = len(s.split())
    return ngettext("{} word entered", "{} words entered", N).format(N)
