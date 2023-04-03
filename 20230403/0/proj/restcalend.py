import calendar
s = calendar.month(2023, 4)
s = s.split('\n')
n = len(s[1])
ans = ['Calendar\n========\n\n', '+--------------------+']
ans.append('|' + s[0] + ' '*(n - len(s[0])) + '|')
ans.append('+--+--+--+--+--+--+--+')
ans.append('|' + s[1].replace(' ', '|') + '|')
ans.append('+--+--+--+--+--+--+--+')
for i in range(2, len(s)):
    if not s[i]:
        break
    j = s[i].ljust(n)
    j = [j[:2], j[3:5], j[6:8], j[9:11], j[12:14], j[15:17], j[18:]]
    j = '|'.join(j)
    ans.append('|' + j + '|')
    ans.append('+--+--+--+--+--+--+--+')

print('\n'.join(ans))
