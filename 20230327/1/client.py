from cowsay import cowsay
from cowsay import list_cows
from io import StringIO
from cowsay import read_dot_cow
import shlex
import cmd
import socket
import sys
import threading
import time
import readline

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

class Gameplay(cmd.Cmd):
    prompt = '>>> '
    intro = "<<< Welcome to Python-MUD 0.1 >>>"
    cowlist = list_cows() + ['jgsbat']
    weaponlist = {'sword': 10, 'spear': 15, 'axe': 20}
    gamefield = [[None for j in range(10)] for i in range(10)]
    x, y = 0, 0
    ON = True

    def __init__(self, name, *args):
        super().__init__(*args)
        self.name = name
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('localhost', 8080))
        self.socket.send(f'login {name}\n'.encode())
        data = self.socket.recv(1024).decode().strip()
        if data == 'connection refused':
            self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()
            self.ON = False
            return 1

    def do_left(self, args):
        '''Move one step left'''
        if args:
            print("Invalid arguments")
            return 0
        self.socket.send('move -1 0\n'.encode())

    def do_right(self, args):
        '''Move one step right'''
        if args:
            print("Invalid arguments")
            return 0
        self.socket.send('move 1 0\n'.encode())

    def do_up(self, args):
        '''Move one step up'''
        if args:
            print("Invalid arguments")
            return 0

    def do_down(self, args):
        '''Move one step down'''
        if args:
            print("Invalid arguments")
            return 0
        self.socket.send('move 0 1\n'.encode())

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
        self.socket.send((shlex.join(["addmon", name, hello, str(hp), str(x), str(y)]) + '\n').encode())
        #print(self.socket.recv(1024).decode().strip())

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
            return 
        damage = self.weaponlist[args[1]]
        self.socket.send((shlex.join(["attack", name, str(damage)]) + '\n').encode())

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
        
    def do_sayall(self, args):
        self.socket.send((shlex.join(["SAYALL", str(args)]) + '\n').encode())

    def do_quit(self, args):
        '''Exit the game'''
        self.socket.send('quit\n'.encode())
        #data = self.socket.recv(1024).decode()
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        self.ON = False
        return 1

    def do_EOF(self, args):
        return 1

    def default(line):
        print("Invalid command")

    def spam(self):
        while self.ON:
            try:
                data = self.socket.recv(1024).decode().strip()
            except OSError:
                break
            if data.startswith("Moved ") and len(data.split('\n')) > 1:
                data = data.split('\n')
                print(f"{data[0]}\n{self.prompt}{readline.get_line_buffer()}", end = '', flush=True)
                if len(data) == 2:
                    data = data[1].split()
                if  data[0] == 'jgsbat':
                    print(f"{cowsay(data[1], cowfile=custom_cow)}\n{self.prompt}{readline.get_line_buffer()}", end = '', flush=True)
                else:
                    print(f"{cowsay(data[1], cow=data[0])}\n{self.prompt}{readline.get_line_buffer()}", end = '', flush=True)
            else:
                print(f"{data}\n{self.prompt}{readline.get_line_buffer()}", end = '', flush=True)

try:
    game = Gameplay(sys.argv[1])
    timer = threading.Thread(target=game.spam, args=())
    timer.start()
    game.cmdloop()
except:
	 pass      
