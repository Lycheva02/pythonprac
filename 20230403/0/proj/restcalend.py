import calendar

def restmonth(y, m)
    s = calendar.month(y, m)
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

    return '\n'.join(ans)
 
 if __name__ == '__main__':
    print(restmonth(int(sys.argv[1]), int(sys.argv[2])))
