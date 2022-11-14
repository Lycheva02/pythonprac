class  InvalidInput(Exception):
    def __str__(self):
        return 'Invalid input'

class BadTriangle(Exception):
    def __str__(self):
        return 'Not a triangle'

def triangleSquare(s):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(s)
    except Exception:
        raise InvalidInput()
    if not all([type(x1) in [int, float], type(y1) in [int, float], type(x2) in [int, float], type(y2) in [int, float], type(x3) in [int, float], type(y3) in [int, float]]):
        raise BadTriangle()
    if (x1, y1) == (x2, y2) or (x1, y1) == (x3, y3) or (x2, y2) == (x3, y3):
        raise BadTriangle()
    dx = x1 - x2
    dy = y1 - y2
    dx1 = x1 - x3
    dy1 = y1 - y3
    if dx == 0 and dx1 == 0:
        raise BadTriangle()
    if dx != 0 and dx1 != 0:
        if dy/dx == dy1/dx1:
            raise BadTriangle()
    a = (dx**2+dy**2)**0.5
    b = (dx1**2 + dy1**2)**0.5
    dx2 = x2 - x3
    dy2 = y2 - y3
    c = (dx2**2 + dy2**2)**0.5
    # формула Герона
    p = (a + b + c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return s

while (s := input()):
    try:
        res = triangleSquare(s)
    except Exception as E:
        print(E)
    else:
        print(format(res, ".2f"))
