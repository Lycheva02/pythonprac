import cmd
import threading
import time
import readline
import socket
import sys

globalsock = None

class simple(cmd.Cmd):

    def do_echo(self, arg):
        globalsock.sendall(arg.strip().encode())

def receiver(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        globalsock.connect((sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 1337))
        while msg := sys.stdin.readline():
            globalsock.sendall(msg.strip().encode())
            print(globalsock.recv(1024).decode())

cmdline = simple()
timer = threading.Thread(target=receiver, args=('0.0.0.0', 1337))
timer.start()
cmdline.cmdloop()
