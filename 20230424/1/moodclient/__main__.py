"""Client module."""
from . import client
import threading
import sys

try:
    """Initiate client."""
    game = client.Client_Gameplay(sys.argv[1])
    timer = threading.Thread(target=game.spam, args=(), daemon=True)
    timer.start()
    game.cmdloop()
except:  # noqa: E722
    pass
