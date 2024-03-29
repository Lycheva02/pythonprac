from cowsay import cowsay
from cowsay import list_cows
from io import StringIO
from cowsay import read_dot_cow
import shlex
import cmd

custom_cow = read_dot_cow(StringIO('''
$the_cow = <<EOC;
           $thoughts
           $thoughts
    ,_                    _,
    ) '-._  ,_    _,  _.-' (
    )  _.-'.|\\\\--//|.'-._  (
     )'   .'\\/o\\/o\\/'.   `(
      ) .' . \\====/ . '. (
       )  / <<    >> \\  (
        '-._/``  ``\\_.-'
  jgs     __\\\\'--'//__
         (((""`  `"")))
EOC'''))

class Monster:
    def __init__(self, name, hello, hp):
        self.name = name
        self.hello = hello
        self.hp = hp

class Gameplay(cmd.Cmd):
    prompt = '>>> '
    intro = "<<< Welcome to Python-MUD 0.1 >>>"
    cowlist = list_cows() + ['jgsbat']
    weaponlist = {'sword': 10, 'spear': 15, 'axe': 20}
    gamefield = [[None for j in range(10)] for i in range(10)]
    x, y = 0, 0

    def encounter(self, x, y):
        if self.gamefield[x][y].name == 'jgsbat':
            print(cowsay(self.gamefield[x][y].hello, cowfile=custom_cow))
        else:
            print(cowsay(self.gamefield[x][y].hello, cow=self.gamefield[x][y].name))

    def do_left(self, args):
        '''Move one step left'''
        if args:
            print("Invalid arguments")
            return 0
        self.x = (self.x - 1)%10
        print(f"Moved to ({self.x}, {self.y})")
        if self.gamefield[self.x][self.y] != None:
                self.encounter(self.x,self.y)

    def do_right(self, args):
        '''Move one step right'''
        if args:
            print("Invalid arguments")
            return 0
        self.x = (self.x + 1)%10
        print(f"Moved to ({self.x}, {self.y})")
        if self.gamefield[self.x][self.y] != None:
                self.encounter(self.x,self.y)

    def do_up(self, args):
        '''Move one step up'''
        if args:
            print("Invalid arguments")
            return 0
        self.y = (self.y - 1)%10
        print(f"Moved to ({self.x}, {self.y})")
        if self.gamefield[self.x][self.y] != None:
                self.encounter(self.x,self.y)

    def do_down(self, args):
        '''Move one step down'''
        if args:
            print("Invalid arguments")
            return 0
        self.y = (self.y + 1)%10
        print(f"Moved to ({self.x}, {self.y})")
        if self.gamefield[self.x][self.y] != None:
                self.encounter(self.x,self.y)

    def do_addmon(self, args):
        ''' Add a monster:  addmon <name> coord <x> <y> hello <message> hp <health points>'''
        args = shlex.split(args)
        try:
            name = args[0]
            hello = args[args.index('hello') + 1]
            hp = int(args[args.index('hp') + 1])
            coord_ind = args.index('coords')
            x, y = list(map(int, args[coord_ind + 1: coord_ind + 3]))
        except:
            print("Wrong parameters")
            return 0
        if not ((0 <= x <= 9) and (0 <= y <= 9)):
            print("Invalid arguments")
            return 0
        if name not in self.cowlist:
            print("Cannot add unknown monster")
            return 0
        if hp <= 0:
            print("Invalid hp argument")
        repl_flag = self.gamefield[x][y]
        self.gamefield[x][y] = Monster(name, hello, hp)
        print(f"Added monster {name} to ({x}, {y}) saying {hello}")
        if repl_flag:
            print("Replaced the old monster")

    def do_attack(self, args):
        '''Attack the monster: attack <name> [with <weapon>]'''
        if not args:
            print("The name is essential")
            return 0
        args = shlex.split(args)
        name = args[0]
        args.pop(0)
        if not args:
            args = shlex.split('with sword')
        if len(args) != 2:
            print("Invalid input")
            return 0
        if args[1] not in self.weaponlist:
            print("Unknown weapon")
            return 0
        damage = self.weaponlist[args[1]]
        m = self.gamefield[self.x][self.y]
        if not m or m.name != name:
            print(f"No {name} here")
            return 0
        damage = min(damage, m.hp)
        m.hp -= damage
        print(f"Attacked {m.name}, damage {damage} hp")
        if m.hp:
            print(f"{m.name} now has {m.hp}")
        else:
            print(f"{m.name} died")
            self.gamefield[self.x][self.y] = None

    def complete_attack(self, prefix, line, start, end):
        weapon_variants = self.weaponlist
        name_variants = self.cowlist
        if (not prefix and line.split()[-1] == 'with') or prefix == 'with':
            return [i for i in weapon_variants]
        if line.split()[-2] == 'with':
            return [i for i in weapon_variants if i.startswith(prefix)]
        if not prefix:
            return [i for i in name_variants]
        return [i for i in name_variants if i.startswith(prefix)]

    def do_quit(self, args):
        '''Exit the game'''
        return 1

    def do_EOF(self, args):
        return 1

    def default(line):
        print("Invalid command")

game = Gameplay()
game.cmdloop()
        
