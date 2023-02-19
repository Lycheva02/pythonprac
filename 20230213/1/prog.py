import zlib
from glob import iglob
from os.path import basename, dirname
import sys
import os

if len(sys.argv) == 1:
    for b in iglob('.git/refs/heads/*'):
        print(b.split('/')[-1])

