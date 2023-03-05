from cowsay import cowsay
from cowsay import list_cows
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
     if name not in list_cows() and name != 'jgsbat':
         print("Cannot add unknown monster")
         return
     repl_flag = gamefield[x][y][0]
     gamefield[x][y][0] = name
     gamefield[x][y][1] = hello
     print(f"Added monster {name} to ({x}, {y}) saying {hello}")
     if repl_flag:
         print("Replaced the old monster")

def encounter(x, y):
    if gamefield[x][y][0] == 'jgsbat':
        print(cowsay(gamefield[x][y][1], cowfile=custom_cow))
    else:
        print(cowsay(gamefield[x][y][1], cow=gamefield[x][y][0]))
     


x, y = 0, 0

print("<<< Welcome to Python-MUD 0.1 >>>")
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
        
