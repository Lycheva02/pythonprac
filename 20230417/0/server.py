import sqroots
import asyncio

async def main():
	server = await asyncio.start_server(sqroots.server, '0.0.0.0', 1337)
	async with server:
		await server.serve_forever()

asyncio.run(main())
