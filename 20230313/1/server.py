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

    def encounter(self, x, y):
        mon = self.gamefield[self.x][self.y]
        return [mon.name, mon.hello]

    def addmon(self, name, hello, hp, x, y):
        repl_flag = self.gamefield[x][y]
        self.gamefield[x][y] = Monster(name, hello, hp)
        ans = f"Added monster {name} to ({x}, {y}) saying {hello}"
        if repl_flag:
            ans += "\nReplaced the old monster"
        return ans

    def attack(self, name, damage):
        m = self.gamefield[self.x][self.y]
        if not m or m.name != name:
            return f"No {name} here"
        damage = min(damage, m.hp)
        m.hp -= damage
        ans = f"Attacked {m.name}, damage {damage} hp"
        if m.hp:
            ans += f"\n{m.name} now has {m.hp}"
        else:
            ans += f"\n{m.name} died"
            self.gamefield[self.x][self.y] = None
        return ans

    async def play(self, reader, writer):
        while not reader.at_eof():
            data = await reader.readline()
            data = shlex.split(data.strip().decode())
            match data:
                case ['move', x_chng, y_chng]:
                    self.x = (self.x + int(x_chng)) % 10
                    self.y = (self.y + int(y_chng)) % 10
                    ans = f"Moved to ({self.x}, {self.y})"
                    if self.gamefield[self.x][self.y] != None:
                        ans += f"\n{shlex.join(self.encounter(self.x, self.y))}"
                    writer.write(ans.encode())
                    await writer.drain()
                case ['addmon', name, hello, hp, x_str, y_str]:
                    writer.write(self.addmon(name, hello, int(hp), int(x_str), int(y_str)).encode())
                    await writer.drain()
                case ['attack', name, damage]:
                    writer.write(self.attack(name, int(damage)).encode())
                    await writer.drain()
        writer.close()
        await writer.wait_closed()

async def main():
    gmpl = Gameplay()
    server = await asyncio.start_server(gmpl.play, '0.0.0.0', 8080)
    async with server:
        await server.serve_forever()

asyncio.run(main())
