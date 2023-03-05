from cowsay import cowsay
from cowsay import list_cows
<<<<<<< HEAD
import shlex
=======
from io import StringIO
from cowsay import read_dot_cow

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

>>>>>>> 62c4d79 (jgsbat добавлена)

class Monster:
    def __init__(self, name, hello, hp):
        self.name = name
        self.hello = hello
        self.hp = hp
gamefield = [[None for j in range(10)] for i in range(10)]

def move(direction, x, y):
    match direction:
        case 'up':
            y = (y - 1)%10
        case 'down':
            y = (y + 1)%10
        case 'left':
            x = (x - 1)%10
        case 'right':
            x = (x + 1)%10
    print(f"Moved to ({x}, {y})")
    return (x, y)

def addmon(name, hello, hp, x, y):
     hp = int(hp)
     if not ((0 <= x <= 9) and (0 <= y <= 9)):
        print("Invalid arguments")
        return
     if name not in list_cows() and name != 'jgsbat':
         print("Cannot add unknown monster")
         return
     if hp <= 0:
         print("Invalid hp argument")
     repl_flag = gamefield[x][y]
     gamefield[x][y] = Monster(name, hello, hp)
     print(f"Added monster {name} to ({x}, {y}) saying {hello}")
     if repl_flag:
         print("Replaced the old monster")

def encounter(x, y):
<<<<<<< HEAD
    print(cowsay(gamefield[x][y].hello, cow=gamefield[x][y].name))
=======
    if gamefield[x][y][0] == 'jgsbat':
        print(cowsay(gamefield[x][y][1], cowfile=custom_cow))
    else:
        print(cowsay(gamefield[x][y][1], cow=gamefield[x][y][0]))
>>>>>>> 62c4d79 (jgsbat добавлена)
     


x, y = 0, 0

print("<<< Welcome to Python-MUD 0.1 >>>")
while True:
    try:
        s = input()
    except EOFError:
        break
    s = shlex.split(s)
    match s:
        case ['up' | 'down' | 'left' | 'right' as direction]:
            x,y = move(direction, x, y)
            if gamefield[x][y] != None:
                encounter(x,y)
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
        
