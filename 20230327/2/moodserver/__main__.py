from . import server
import asyncio

async def main():
    gmpl = server.Gameplay()
    playing_server = await asyncio.start_server(gmpl.play, '0.0.0.0', 8080)
    async with playing_server:
        await playing_server.serve_forever()

asyncio.run(main())
