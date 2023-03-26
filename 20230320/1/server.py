import shlex
import asyncio

class Monster:
    def __init__(self, name, hello, hp):
        self.name = name
        self.hello = hello
        self.hp = hp

class Gameplay():
    gamefield = [[None for j in range(10)] for i in range(10)]
    x, y = 0, 0
    clients = {}
    players = {}

    def encounter(self, nm, x, y):
        x_coord, y_coord = self.players[nm]
        mon = self.gamefield[x_coord][y_coord]
        return [mon.name, mon.hello]

    def addmon(self, name, hello, hp, x, y):
        repl_flag = self.gamefield[x][y]
        self.gamefield[x][y] = Monster(name, hello, hp)
        ans = f"Added monster {name} to ({x}, {y}) saying {hello}"
        if repl_flag:
            ans += "\nReplaced the old monster"
        return ans

    def attack(self, name, damage):
        x_coord, y_coord = self.players[nm]
        m = self.gamefield[x_coord][y_coord]
        if not m or m.name != name:
            return f"No {name} here"
        damage = min(damage, m.hp)
        m.hp -= damage
        ans = f"Attacked {m.name}, damage {damage} hp"
        if m.hp:
            ans += f"\n{m.name} now has {m.hp}"
        else:
            ans += f"\n{m.name} died"
            self.gamefield[x_coord][y_coord] = None
        return ans

    async def play(self, reader, writer):
        nm = None
        q = asyncio.Queue()
        send = asyncio.create_task(reader.readline())
        receive = asyncio.create_task(q.get())
        while not reader.at_eof():
            done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
            for t in done:
                if t is send:
                    send = asyncio.create_task(reader.readline())
                    data = t.result().decode().strip()
                    ans = f'{nm}'
                    data = shlex.split(data)
                    match data:
                        case ['login', name]:
                            if name in self.clients:
                                writer.write('connection refused'.encode())
                                await writer.drain()
                                continue
                            nm = name
                            self.clients[nm] = q
                            self.players[nm] = [0,0]
                            writer.write('\n'.encode())
                            await writer.drain()
                        case ['move', x_chng, y_chng]:
                            x_coord, y_coord = self.players[nm]
                            self.players[nm][0] = (x_coord + int(x_chng)) % 10
                            self.players[nm][1] = (y_coord + int(y_chng)) % 10
                            x_coord, y_coord = self.players[nm]
                            ans = f"Moved to ({x_coord}, {y_coord})"
                            if self.gamefield[x_coord][y_coord] != None:
                                ans += f"\n{shlex.join(self.encounter(x_coord, y_coord))}"
                            writer.write(ans.encode())
                            await writer.drain()
                        case ['addmon', name, hello, hp, x_str, y_str]:
                            writer.write(self.addmon(name, hello, int(hp), int(x_str), int(y_str)).encode())
                            await writer.drain()
                        case ['attack', name, damage]:
                            writer.write(self.attack(name, int(damage)).encode())
                            await writer.drain()
                        case ['quit']:
                            writer.write('quit'.encode())
                            await writer.drain()
                            break
                elif t is receive:
                    receive = asyncio.create_task(q.get())
                    writer.write(f"{t.result()}\n".encode())
                    await writer.drain()
        send.cancel()
        receive.cancel()
        if nm != None:
            del self.clients[nm]
            for i, iq in self.clients.items():
                await iq.put(f"{nm} exit")
        writer.close()
        await writer.wait_closed()

async def main():
    gmpl = Gameplay()
    server = await asyncio.start_server(gmpl.play, '0.0.0.0', 8080)
    async with server:
        await server.serve_forever()

asyncio.run(main())
