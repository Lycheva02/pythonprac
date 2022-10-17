st = input()
w = len(st)  # ширина контейнера, включая стенки

liquid = 0
h = 2

while (s := input()) != st:
    h += 1
    if s[1] == '~':
        liquid += w - 2

st = ''.join(['#' for i in range(h)])
cont = [st]

gas_layer = '#' + ''.join(['.' for i in range(h - 2)]) + '#'
liquid_layer = '#' + ''.join(['~' for i in range(h - 2)]) + '#'

liq_new = liquid//(h-2)
if liquid % (h-2) > 0:
    liq_new += 1
gas_new = w - 2 - liq_new

for i in range(gas_new):
    cont.append(gas_layer)
for i in range(liq_new):
    cont.append(liquid_layer)

cont.append(st)
for l in cont:
    print(l)

liq_new = liquid
volume = (h - 2) * (w - 2)
gas_new  = volume - liq_new

if gas_new >= liq_new:
    dl = 18 - len(str(gas_new)) - len(str(volume))
    gas_layer = ''.join(['.' for i in range(dl)]) + ' ' + str(gas_new) + '/' + str(volume)
    dl2 = round(liq_new/gas_new * dl)
    liquid_layer = ''.join(['~' for i in range(dl2)]) + ''.join([' ' for i in range(19 - dl2 - len(str(liq_new)) - len(str(volume)))]) + str(liq_new) + '/' + str(volume)
    print(gas_layer, liquid_layer, sep = '\n')

else:
    dl = 18 - len(str(liq_new)) - len(str(volume))
    liquid_layer = ''.join(['~' for i in range(dl)]) + ' ' + str(liq_new) + '/' + str(volume)
    dl2 = round(gas_new/liq_new * dl)
    gas_layer = ''.join(['.' for i in range(dl2)]) + ''.join([' ' for i in range(19 - dl2 - len(str(gas_new)) - len(str(volume)))]) + str(gas_new) + '/' + str(volume)
    print(gas_layer, liquid_layer, sep = '\n')
