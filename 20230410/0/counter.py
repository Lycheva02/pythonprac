import sys
import os
import gettext

popath = os.path.join(os.path.dirname(__file__), "po")
translation = gettext.translation("counter", popath, fallback=True)
_, ngettext = translation.gettext, translation.ngettext

while (s := sys.stdin.readline()):
	N = len(s.split())
	print(ngettext("{} word entered", "{} words entered", N).format(N))
