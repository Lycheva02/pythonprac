import asyncio

ev = asyncio.Event()

async def writer(queue, delay):
    i = 0
    await asyncio.sleep(delay)
    while not ev.is_set():
        await queue.put(str(f"{i}_{delay}))
        i += 1
        await asyncio.sleep(delay)
    await queue.put(None)

async def stacker(queue, stack):
    while not ev.is_set():
        a = await queue.get()
        await stack.put(a)

async def reader(stack, count, delay):
    for i in range(count):
        await asyncio.sleep(delay)
        print(await stack.get())
    ev.set()

async def main():
    d1, d2, d3, c = map(int, input().split(','))
    queue = asyncio.Queue()
    stack = asyncio.LifoQueue()
    await asyncio.gather(
        writer(queue, d1),
        writer(queue, d2),
        stacker(queue, stack),
        reader(stack, c, d3)
    )

asyncio.run(main())
