from cowsay import cowsay

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

def addmon(x, y, hello):
     if not ((0 <= x <= 9) and (0 <= y <= 9)):
        print("Invalid arguments")
        return
     repl_flag = gamefield[x][y]
     gamefield[x][y] = hello
     print(f"Added monster to ({x}, {y}) saying {hello}")
     if repl_flag:
         print("Replaced the old monster")

def encounter(x, y):
    print(cowsay(gamefield[x][y]))
     


x, y = 0, 0

while True:
    try:
        s = input()
    except EOFError:
        break
    match s.split():
        case ['up' | 'down' | 'left' | 'right' as direction]:
            x,y = move(direction, x, y)
            if gamefield[x][y] != None:
                encounter(x,y)
        case 'addmon', xstr, ystr, hello:
            addmon(int(xstr), int(ystr), hello)
        case 'addmon' | 'up' | 'down' | 'left' |'right', *wtv:
            print("Invalid arguments")
        case _:
            print("Invalid command")
        
