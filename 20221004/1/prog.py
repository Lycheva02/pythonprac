def bs(a, s):
	if len(s) == 0:
		return False
	if a == s[(len(s) - 1)//2]:
		return True
	if a < s[(len(s) - 1)//2]:
		return bs(a, s[:(len(s) - 1)//2])
	return bs(a, s[(len(s) - 1)//2 + 1:])

a, s = eval(input())
print(bs(a, s))
