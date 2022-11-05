from math import isclose

def lines_cross(x1, y1, x2, y2, x3, y3, x4, y4):  # пересекаются ли отрезки, по координатам их концов
    if x2 - x1 == 0:
        if x4 - x3 == 0:
            return (y3 - y1)*(y3 - y2) <= 0 or (y4 - y1)*(y4 - y2) <= 0
        k2 = (y4 - y3)/(x4 - x3)
        b2 = y3 - k2*x3
        y = k2*x1 + b2
        return (y - y1)*(y - y2) <= 0 and (y - y3)*(y - y4) <= 0
    k1 = (y2 - y1)/(x2-x1)
    b1 = y2 - k1*x2
    if x4 - x3 == 0:
        y = k1*x3 + b1
        return (y - y1)*(y - y2) <= 0 and (y - y3)*(y - y4) <= 0
    k2 = (y4 - y3)/(x4 - x3)
    b2 = y3 - k2*x3
    if k1 == k2:
        return b1 == b2
    x = (b2 - b1)/(k1 - k2)
    return (x - x1)*(x - x2) <= 0 and (x - x3)*(x - x4) <= 0

class Triangle:
    def __init__(self, *args):
        self.coord = list(args)
    def __abs__(self):
        if self.coord[0] == self.coord[1] or self.coord[0] == self.coord[2] or self.coord[1] == self.coord[2]:
            return 0
        dx = self.coord[0][0] - self.coord[1][0]
        dy = self.coord[0][1] - self.coord[1][1]
        dx1 = self.coord[0][0] - self.coord[2][0]
        dy1 = self.coord[0][1] - self.coord[2][1]
        if dx == 0 and dx1 == 0:
            return 0
        if dx != 0 and dx1 != 0:
            if dy/dx == dy1/dx1:
                return 0
        a = (dx**2+dy**2)**0.5
        b = (dx1**2 + dy1**2)**0.5
        dx2 = self.coord[1][0] - self.coord[2][0]
        dy2 = self.coord[1][1] - self.coord[2][1]
        c = (dx2**2 + dy2**2)**0.5
        # формула Герона
        p = (a + b + c)/2
        s = (p*(p-a)*(p-b)*(p-c))**0.5
        return s
    def __bool__(self):
        return abs(self) > 0
    def __lt__(self, other):
        return abs(self) < abs(other)
    def dot_in(self, arg):    # содержит ли треугольник точку
        s1 = abs(Triangle(self.coord[0], self.coord[1], arg))
        s2 = abs(Triangle(self.coord[0], self.coord[2], arg))
        s3 = abs(Triangle(self.coord[2], self.coord[1], arg))
        return isclose(s1 + s2 + s3, abs(self))
    def __contains__(self, other):
        if abs(other) == 0:
            return True
        return self.dot_in(other.coord[0]) and self.dot_in(other.coord[1]) and self.dot_in(other.coord[2])
    def __and__(self, other):
        if abs(self) == 0 or abs(other) == 0:
            return False
        if self in other or other in self:
            return True
        if lines_cross(self.coord[0][0], self.coord[0][1], self.coord[1][0], self.coord[1][1], other.coord[0][0], other.coord[0][1], other.coord[1][0], other.coord[1][1]):
            return True
        if lines_cross(self.coord[0][0], self.coord[0][1], self.coord[1][0], self.coord[1][1], other.coord[2][0], other.coord[2][1], other.coord[1][0], other.coord[1][1]):
            return True
        if lines_cross(self.coord[0][0], self.coord[0][1], self.coord[1][0], self.coord[1][1], other.coord[0][0], other.coord[0][1], other.coord[2][0], other.coord[2][1]):
            return True
        if lines_cross(self.coord[0][0], self.coord[0][1], self.coord[2][0], self.coord[2][1], other.coord[0][0], other.coord[0][1], other.coord[1][0], other.coord[1][1]):
            return True
        if lines_cross(self.coord[0][0], self.coord[0][1], self.coord[2][0], self.coord[2][1], other.coord[2][0], other.coord[2][1], other.coord[1][0], other.coord[1][1]):
            return True
        if lines_cross(self.coord[0][0], self.coord[0][1], self.coord[2][0], self.coord[2][1], other.coord[0][0], other.coord[0][1], other.coord[2][0], other.coord[2][1]):
            return True
        if lines_cross(self.coord[2][0], self.coord[2][1], self.coord[1][0], self.coord[1][1], other.coord[0][0], other.coord[0][1], other.coord[1][0], other.coord[1][1]):
            return True
        if lines_cross(self.coord[2][0], self.coord[2][1], self.coord[1][0], self.coord[1][1], other.coord[2][0], other.coord[2][1], other.coord[1][0], other.coord[1][1]):
            return True
        if lines_cross(self.coord[2][0], self.coord[2][1], self.coord[1][0], self.coord[1][1], other.coord[0][0], other.coord[0][1], other.coord[2][0], other.coord[2][1]):
            return True
        return False

import sys
exec(sys.stdin.read())
