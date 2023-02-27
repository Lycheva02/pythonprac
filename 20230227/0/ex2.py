import shlex

fio = input()
place = input()

command = shlex.join(['register', fio, place])
print(command)
print(shlex.split(command))
