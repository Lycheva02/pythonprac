import zlib
from glob import iglob
import os
import sys
import os

def print_last_commit(nm):
    with open('.git/refs/heads/' + nm) as f:
        id = f.readline().strip()
    with open('.git/objects/' + id[:2] + '/' + id[2:], 'rb') as f:
        head, _, body = zlib.decompress(f.read()).partition(b'\x00')
        print(body.decode())

def print_last_commit_tree(nm):
    with open('.git/refs/heads/' + sys.argv[1], 'rb') as f:
        data = f.read()
        id = data[:-1].decode()
    with open('.git/objects/' + id[:2] + '/'  + id[2:], 'rb') as f:
        data = zlib.decompress(f.read()).split()
        id = data[2].decode()
    with open('.git/objects/' + id[:2] + '/' + id[2:], 'rb') as f:
        head, _, body = zlib.decompress(f.read()).partition(b'\x00')
        while body:
            obj, _, body = body.partition(b'\x00')
            x, y = obj.split()
            c, body = body[:20], body[20:]
            print(f"{head[:4].decode()} {c.hex()} {y.decode()}")
'''
def print_branch(nm):
    with open('.git/refs/heads/' + sys.argv[1], 'rb') as f:
        data = f.read()
        id = data[:-1].decode()
    with open('.git/objects/' + id[:2] + '/' + id[2:], 'rb') as f:
        data = zlib.decompress(f.read()).split()
        print('TREE for commit ', id)
        id = data[2].decode()
        with open('.git/objects/' + id[:2] + '/' + id[2:], 'rb') as f:
             head, _, body = zlib.decompress(f.read()).partition(b'\x00')
             while body:
                 obj, _, body = body.partition(b'\x00')
                 x, y = obj.split()
                 c, body = body[:20], body[20:]
                 print(f"{head[:4].decode()} {c.hex()} {y.decode()}")
        while  b'parent' in data:
             id = data[4].decode()
             with open('.git/objects/' + id[:2] + '/' + id[2:], 'rb') as f:
                 data = zlib.decompress(f.read()).split()
                 print('TREE for commit ', id)
                 id = data[2].decode()
                 with open('.git/objects/' + id[:2] + '/' + id[2:], 'rb') as f:
                     head, _, body = zlib.decompress(f.read()).partition(b'\x00')
                     while body:
                         obj, _, body = body.partition(b'\x00')
                         x, y = obj.split()
                         c, body = body[:20], body[20:]
                         print(f"{head[:4].decode()} {c.hex()} {y.decode()}")
'''
if len(sys.argv) == 1:
    for b in iglob('.git/refs/heads/*'):
        print(b.split('/')[-1])
else:
#    print_last_commit(sys.argv[1])
    print_last_commit_tree(sys.argv[1])
#    print_branch(sys.argv[1])
