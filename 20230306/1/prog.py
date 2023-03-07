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
    
    def __init__(self):
        self.gamefield = [[None for j in range(10)] for i in range(10)]
        self.x, self.y = 0, 0

    def encounter(x, y):
        if gamefield[x][y].name == 'jgsbat':
            print(cowsay(gamefield[x][y].hello, cowfile=custom_cow))
        else:
            print(cowsay(gamefield[x][y].hello, cow=gamefield[x][y].name))

    def do_left(self):
        self.x = (self.x - 1)%10
        print(f"Moved to ({self.x}, {self.y})")
        if self.gamefield[self.x][self.y] != None:
                self.encounter(self.x,self.y)

    def do_right(self):
        self.x = (self.x + 1)%10
        print(f"Moved to ({self.x}, {self.y})")
        if self.gamefield[self.x][self.y] != None:
                self.encounter(self.x,self.y)

    def do_up(self):
        self.y = (self.y - 1)%10
        print(f"Moved to ({self.x}, {self.y})")
        if self.gamefield[self.x][self.y] != None:
                self.encounter(self.x,self.y)

    def do_down(self):
        self.y = (self.y + 1)%10
        print(f"Moved to ({self.x}, {self.y})")
        if self.gamefield[self.x][self.y] != None:
                self.encounter(self.x,self.y)

    def do_addmon(name, hello, hp, x, y):
         if not ((0 <= x <= 9) and (0 <= y <= 9)):
            print("Invalid arguments")
            return
         if name not in self.cowlist:
             print("Cannot add unknown monster")
             return
         if hp <= 0:
             print("Invalid hp argument")
         repl_flag = self.gamefield[x][y]
         self.gamefield[x][y] = Monster(name, hello, hp)
         print(f"Added monster {name} to ({x}, {y}) saying {hello}")
         if repl_flag:
             print("Replaced the old monster")

    def do_quit(self, args):
        '''Выход из игры'''
        return 1

game = Gameplay()
game.cmdloop()

        case ['addmon', name, *parameters]:
            try:
                hello = parameters[parameters.index('hello') + 1]
                hp = parameters[parameters.index('hp') + 1]
                coord_ind = parameters.index('coords')
                xstr, ystr = parameters[coord_ind + 1: coord_ind + 3]
            except:
                print("Wrong parameters")
                continue
            addmon(name, hello, hp, int(xstr), int(ystr))
        case ['addmon' | 'up' | 'down' | 'left' |'right', *wtv]:
            print("Invalid arguments")
        case _:
            print("Invalid command")
        
