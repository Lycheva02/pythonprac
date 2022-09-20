x = eval(input())
ans = ''
if (x%2 == 0) and (x%25 == 0):
	ans += 'A + B - '
elif (x%2 != 0) and (x%25 == 0):
	ans += 'A - B + '
else:
    ans += 'A - B - '
if (x%8 == 0):
	ans += 'C +'
else:
	ans += 'C -'
print(ans)
