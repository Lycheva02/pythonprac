import sys, struct

s = sys.stdin.buffer.read()
res = ''
print(struct.unpack('4s', s[8:12]))
if len(s) >= 44 and struct.unpack('4s', s[8:12]) == "WAVE":
    try:
        res += 'Size=' + str(struct.unpack('I', s[4:8])) + ', '
        res += 'Type=' + str(struct.unpack('H', s[20:22])) + ', '
        res += 'Channels=' + str(struct.unpack('H', s[22:24])) + ', '
        res += 'Rate=' + str(struct.unpack('I', s[24:28])) + ', '
        res += 'Bits=' + str(struct.unpack('H', s[34:36])) + ', '
        res += 'Data size=' + str(struct.unpack('I', s[40:44]))
        print(res)
    except:
        print("NO")
else:
    print("NO")
        
