from cowsay import cowsay
from cowsay import list_cows

gamefield = [[[None, None] for j in range(10)] for i in range(10)]  #[0] - name; [1] - hello

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

def addmon(name, x, y, hello):
     if not ((0 <= x <= 9) and (0 <= y <= 9)):
        print("Invalid arguments")
        return
     if name not in list_cows():
         print("Cannot add unknown monster")
         return
     repl_flag = gamefield[x][y][0]
     gamefield[x][y][0] = name
     gamefield[x][y][1] = hello
     print(f"Added monster {name} to ({x}, {y}) saying {hello}")
     if repl_flag:
         print("Replaced the old monster")

def encounter(x, y):
    print(cowsay(gamefield[x][y][1]))
     


x, y = 0, 0

while True:
    try:
        s = input()
    except EOFError:
        break
    match s.split():
        case ['up' | 'down' | 'left' | 'right' as direction]:
            x,y = move(direction, x, y)
            if gamefield[x][y][0] != None:
                encounter(x,y)
        case 'addmon', name, xstr, ystr, hello:
            addmon(name, int(xstr), int(ystr), hello)
        case 'addmon' | 'up' | 'down' | 'left' |'right', *wtv:
            print("Invalid arguments")
        case _:
            print("Invalid command")
        
