"""Server module."""
from . import server
import asyncio


async def main():
    """Initiate server."""
    gmpl = server.Gameplay()
    playing_server = await asyncio.gather(
        asyncio.start_server(gmpl.play, '0.0.0.0', 8080),
        gmpl.monster_motion()
        )
    async with playing_server:
        await playing_server.serve_forever()

def start_game():
    asyncio.run(main())
 
if __name__ == '__main__':
    start_game()
