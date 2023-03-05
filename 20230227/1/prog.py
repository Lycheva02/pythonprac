from cowsay import cowsay
from cowsay import list_cows
import shlex

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
     if name not in list_cows():
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
    print(cowsay(gamefield[x][y].hello, cow=gamefield[x][y].name))
     


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
        case ['addmon', name, 'hello', hello, 'hp', hp, 'coords', xstr, ystr]:
            addmon(name, hello, hp, int(xstr), int(ystr))
        case ['addmon' | 'up' | 'down' | 'left' |'right', *wtv]:
            print("Invalid arguments")
        case _:
            print("Invalid command")
        
