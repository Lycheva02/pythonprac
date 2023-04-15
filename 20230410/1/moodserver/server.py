"""
Server realisation.
"""
import shlex
import asyncio
import random
import gettext
import os
import locale

popath = os.path.join(os.path.dirname(__file__), "po")
translations = {'en_NG.UTF-8': gettext.translation("moodserver", popath, fallback=True), 'ru_RU.UTF-8': gettext.translation("moodserver", popath, languages=['ru'])}



class Monster:
    """
    Monster entity.
    
    :param name: monster's name.
    :type name: str
    :param hello: monster's hello string.
    :type hello: str
    :param hp: monster's health points.
    :type hp: int
    """

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
    locales = {}
    weapons = {10: gettext.gettext('sword'), 15: gettext.gettext('spear'), 20: gettext.gettext('axe')}

    def encounter(self, nm):
        """
        Meet monster.
        
        :param nm: player's name.
        :type name: str
        :return: monster's parameters.
        :rtype: list
        """
        x_coord, y_coord = self.players[nm]
        mon = self.gamefield[x_coord][y_coord]
        return [mon.name, mon.hello]

    def addmon(self, name, hello, hp, x, y, nm):
        """
        Add monster.
        
        :param name: monster's name.
        :type name: str
        :param hello: monster's hello word.
        :type hello: str
        :param hp: monster's health points.
        :type hp: int
        :param x: x coordinate.
        :type x: int
        :param y: y coordinate.
        :type y: int
        :return: message for players.
        :rtype: str
        """
        repl_flag = self.gamefield[x][y]
        self.gamefield[x][y] = Monster(name, hello, hp)
        ans = _("Added monster {} to ({}, {}) saying {} with {} hp").format(name, x, y, hello, hp)
        if repl_flag:
            ans += _("\nReplaced the old monster\n")
        return ans

    def attack(self, nm, name, damage):
        """
        Attack realisation.
        
        :param nm: player's name.
        :type nm: str
        :param name: monster's name.
        :type name: str
        :param damage: damage.
        :type damage: int
        :return: message for player.
        :rtype: str
        """
        weapon = self.weapons[damage]
        x_coord, y_coord = self.players[nm]
        m = self.gamefield[x_coord][y_coord]
        if not m or m.name != name:
            return _("No {} here").format(name)
        damage = min(damage, m.hp)
        m.hp -= damage
        ans = _("{} attacked {} with {}, damage {} hp").format(nm, m.name, weapon, damage)
        if m.hp:
            ans += _("\n{} now has {}\n").format(m.name, m.hp)
        else:
            ans += _("\n{} died\n").format(m.name)
            self.gamefield[x_coord][y_coord] = None
        return ans

    async def monster_motion(self):
        """
        Monster's movement realisation.
        """
        variants = {(0, 1): gettext.gettext('down'), (0, -1): gettext.gettext('up'), (1, 0): gettext.gettext('right'), (-1, 0): gettext.gettext('left')}
        while True:
            mon_places = [[x, y] for x in range(10) for y in range(10) if self.gamefield[x][y] is not None]
            if mon_places:
                while True:
                    mon_pos = random.choice(mon_places)
                    direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
                    x_new, y_new = (mon_pos[0] + direction[0]) % 10, (mon_pos[1] + direction[1]) % 10
                    if self.gamefield[x_new][y_new] is None:
                        break
                mon = self.gamefield[mon_pos[0]][mon_pos[1]]
                self.gamefield[mon_pos[0]][mon_pos[1]] = None
                self.gamefield[x_new][y_new] = mon
                ans = _("{} moved one cell {}").format(mon.name, variants[direction])
                for i, iq in self.clients.items():
                    await iq.put(ans)
                for pl, ppos in self.players.items():
                    if ppos == [x_new, y_new]:
                        ans = "MONSTER\n{}".format(shlex.join(self.encounter(pl)))
                        await self.clients[pl].put(ans)
            await asyncio.sleep(30)
   
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
                                translations[self.locales[nm]].install()
                                writer.write(_('connection refused').encode())
                                await writer.drain()
                                continue
                            nm = name
                            self.locales[nm] = 'en_NG.UTF-8'
                            for i, iq in self.clients.items():
                                translations[self.locales[i]].install()
                                await iq.put(_("{} joined").format(nm))
                            self.clients[nm] = q
                            self.players[nm] = [0, 0]
                            writer.write('\n'.encode())
                            await writer.drain()
                        case ['move', x_chng, y_chng]:
                            x_coord, y_coord = self.players[nm]
                            self.players[nm][0] = (x_coord + int(x_chng)) % 10
                            self.players[nm][1] = (y_coord + int(y_chng)) % 10
                            x_coord, y_coord = self.players[nm]
                            translations[self.locales[nm]].install()
                            ans = _("Moved to ({}, {})").format(x_coord, y_coord)
                            if self.gamefield[x_coord][y_coord] is not None:
                                ans += "\n{}".format(shlex.join(self.encounter(nm)))
                            await self.clients[nm].put(ans)
                        case ['addmon', name, hello, hp, x_str, y_str]:
                            ans = self.addmon(name, hello, int(hp), int(x_str), int(y_str))
                            for i, iq in self.clients.items():
                                translations[self.locales[i]].install()
                                await iq.put(ans)
                        case ['attack', name, damage]:
                            ans = self.attack(nm, name, int(damage))
                            translations[self.locales[nm]].install()
                            if ans == _("No {} here").format(name):
                                locale.setlocale(locale.LC_ALL, self.locales[nm])
                                await self.clients[nm].put(ans)
                            else:
                                for i, iq in self.clients.items():
                                    locale.setlocale(locale.LC_ALL, self.locales[i])
                                    await iq.put(ans)
                        case ['SAYALL', args]:
                            if args[0] == args[-1] == '"':
                                args = args[1:-1]
                            for i, iq in self.clients.items():
                                if i == nm:
                                    continue
                                await iq.put(nm + ': ' + args)
                        case ['LOCALE', arg]:
                            self.locales[nm] = locale.locale_alias[arg]
                            translations[self.locales[nm]].install()
                            ans = _("Set up locale: {}").format(arg)
                            await self.clients[nm].put(ans)
                        case ['quit']:
                            break
                elif t is receive:
                    receive = asyncio.create_task(q.get())
                    writer.write("{}\n".format(t.result()).encode())
                    await writer.drain()
        send.cancel()
        receive.cancel()
        if nm is not None:
            del self.clients[nm]
            for i, iq in self.clients.items():
                translations[self.locales[nm]].install()
                await iq.put(_("{} exit").format(nm))
        writer.close()
        await writer.wait_closed()
