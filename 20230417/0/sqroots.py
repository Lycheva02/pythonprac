import asyncio

def sqroots(coeffs):
	a, b, c = map(int, coeffs.split())
	if a == 0:
		raise BaseException('Error a == 0')
	d = b*b - 4*a*c
	if d < 0:
		return ''
	if d == 0:
		return f"{-b/(2*a)}"
	else:
		return f"{(-b + d**0.5)/(2*a)} {(-b - d**0.5)/(2*a)}"
		
async def server(reader, writer):
	while data := await reader.readline():
		try:
			ans = sqroots(data.decode().strip())
		except:
			ans = ''
		writer.write((ans + '\n').encode())
	writer.close()
	await writer.wait_closed()

def sqrootnet(coeffs, s):
	s.sendall((coeffs).encode())
	return s.recv(128).decode().strip()

async def main():
	ser = await asyncio.start_server(server, '0.0.0.0', 1337)
	async with ser:
		await ser.serve_forever()

def serve():
	asyncio.run(main())
