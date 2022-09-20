s = 0
while x := int(input()):
	if x <= 0:
		print(x)
		break
	s += x
	if s > 21:
		print(s)
		break
else:
	print(0)
