class Undead(Exception):
    def __str__(self):
        return 'Generic Undead'

class Skeleton(Undead):
    def __str__(self):
        return 'Skeleton'

class Zombie(Undead):
    def __str__(self):
        return 'Zombie'

class Ghoul(Undead):
    def __str__(self):
        return 'Generic Undead'

def necro(a):
    match a%3:
        case 0:
            raise Skeleton()
        case 1:
            raise Zombie()
        case 2:
            raise Ghoul

x, y = eval(input())
for i in range(x, y):
    try:
        necro(i)
    except Skeleton as S:
        print(S)
    except Zombie as Z:
        print(Z)
    except Undead as U:
        print(U)
