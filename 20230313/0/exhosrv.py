import asyncio
import shlex

async def echo(reader, writer):
    print(writer.get_extra_info('peername'))
    while not reader.at_eof():
        data = await reader.readline()
        data = data.split(maxsplit=1)
        match data:
            case [b'print', wtv]:
                writer.write(wtv)
                await writer.drain()
            case [b'info', kind]:
                if kind not in [b'host\n', b'port\n']:
                    writer.write(b'Bad command\n')
                    await writer.drain()
                    continue
                writer.write((str(writer.get_extra_info('peername')[0 if kind==b'host\n' else 1]) + '\n').encode())
                await writer.drain()
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(echo, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())
