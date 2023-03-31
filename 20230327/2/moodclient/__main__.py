from . import client
import threading
import sys

try:
    game = client.Gameplay(sys.argv[1])
    timer = threading.Thread(target=game.spam, args=(), daemon=True)
    timer.start()
    game.cmdloop()
except:
	pass 
