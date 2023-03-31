"""Server realisation."""
import shlex
import asyncio


class Monster:
    """Monster entity."""

    def __init__(self, name, hello, hp):
        """Initiate monster."""
        self.name = name
        self.hello = hello
        self.hp = hp


class Gameplay():
    """Gameplay realisation."""

    gamefield = [[None for j in range(10)] for i in range(10)]
    x, y = 0, 0
    clients = {}
    players = {}
    weapons = {10: 'sword', 15: 'spear', 20: 'axe'}

    def encounter(self, nm, x, y):
        """Meet monster."""
        x_coord, y_coord = self.players[nm]
        mon = self.gamefield[x_coord][y_coord]
        return [mon.name, mon.hello]

    def addmon(self, name, hello, hp, x, y):
        """Add monster."""
        repl_flag = self.gamefield[x][y]
        self.gamefield[x][y] = Monster(name, hello, hp)
        ans = f"Added monster {name} to ({x}, {y}) saying {hello} with {hp} hp"
        if repl_flag:
            ans += "\nReplaced the old monster\n"
        return ans

    def attack(self, nm, name, damage):
        """Attack realisation."""
        weapon = self.weapons[damage]
        x_coord, y_coord = self.players[nm]
        m = self.gamefield[x_coord][y_coord]
        if not m or m.name != name:
            return f"No {name} here"
        damage = min(damage, m.hp)
        m.hp -= damage
        ans = f"{nm} attacked {m.name} with {weapon}, damage {damage} hp"
        if m.hp:
            ans += f"\n{m.name} now has {m.hp}\n"
        else:
            ans += f"\n{m.name} died\n"
            self.gamefield[x_coord][y_coord] = None
        return ans

    async def play(self, reader, writer):
        """Communicate with client."""
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
                    data = shlex.split(data)
                    match data:
                        case ['login', name]:
                            if name in self.clients:
                                writer.write('connection refused'.encode())
                                await writer.drain()
                                continue
                            nm = name
                            for i, iq in self.clients.items():
                                await iq.put(f"{nm} joined")
                            self.clients[nm] = q
                            self.players[nm] = [0, 0]
                            writer.write('\n'.encode())
                            await writer.drain()
                        case ['move', x_chng, y_chng]:
                            x_coord, y_coord = self.players[nm]
                            self.players[nm][0] = (x_coord + int(x_chng)) % 10
                            self.players[nm][1] = (y_coord + int(y_chng)) % 10
                            x_coord, y_coord = self.players[nm]
                            ans = f"Moved to ({x_coord}, {y_coord})"
                            if self.gamefield[x_coord][y_coord] is not None:
                                ans += f"\n{shlex.join(self.encounter(nm, x_coord, y_coord))}"
                            await self.clients[nm].put(ans)
                        case ['addmon', name, hello, hp, x_str, y_str]:
                            ans = self.addmon(name, hello, int(hp), int(x_str), int(y_str))
                            for i, iq in self.clients.items():
                                await iq.put(ans)
                        case ['attack', name, damage]:
                            ans = self.attack(nm, name, int(damage))
                            if ans == f"No {name} here":
                                await self.clients[nm].put(ans)
                            else:
                                for i, iq in self.clients.items():
                                    await iq.put(ans)
                        case ['SAYALL', args]:
                            if args[0] == args[-1] == '"':
                                args = args[1:-1]
                            for i, iq in self.clients.items():
                                if i == nm:
                                    continue
                                await iq.put(nm + ': ' + args)
                        case ['quit']:
                            break
                elif t is receive:
                    receive = asyncio.create_task(q.get())
                    writer.write(f"{t.result()}\n".encode())
                    await writer.drain()
        send.cancel()
        receive.cancel()
        if nm is not None:
            del self.clients[nm]
            for i, iq in self.clients.items():
                await iq.put(f"{nm} exit")
        writer.close()
        await writer.wait_closed()
