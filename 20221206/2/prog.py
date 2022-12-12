import asyncio
import random

async def merge(A, B, start, middle, finish, event_in1, event_in2, event_out):
    await event_in1.wait()
    await event_in2.wait()
    A = A.copy()
    n, m = start, 0
    i = start
    while (n <= middle - 1) and (m <= finish - middle - 1):
        if A[n] < A[middle+m]:
            B[i] = A[n]
            n += 1
        else:
            B[i] = A[middle+m]
            m += 1
        i += 1
    for j in range(n, middle):
        B[i] = A[j]
        i += 1
    for j in range(m, finish - middle):
        B[i] = A[middle+j]
        i += 1
    event_out.set()

async def mtasks(A):
    task = list()
    B = A.copy()
    
    def sorting(i, j, ev):
        if abs(i - j) <= 1:
            ev.set()
            return
        ev1 = asyncio.Event()
        ev2 = asyncio.Event()
        t = asyncio.create_task(merge(B, B, i, (i+j)//2, j, ev1, ev2, ev))
        task.append(t)
        sorting(i, (i+j)//2, ev1)
        sorting((i+j)//2, j, ev2)

    sorting(0, len(A), asyncio.Event())
    return task, B

import sys
exec(sys.stdin.read())
