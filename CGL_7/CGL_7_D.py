# -*- coding: utf-8 -*-

import collections
import math


class Vector2(collections.namedtuple("Vector2", ["x",  "y"])):

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __pos__(self):
        return Vector2(+self.x, +self.y)

    def __abs__(self):  # norm
        return math.sqrt(float(self.x * self.x + self.y * self.y))

    def __truediv__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

    def abs2(self):
        return float(self.x * self.x + self.y * self.y)

    def dot(self, other):  # dot product
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # cross product
        return self.x * other.y - self.y * other.x


def getDistanceSP(segment, point):
    p = point
    p1, p2 = segment
    if (p2 - p1).dot(p - p1) < 0:
        return abs(p - p1)
    if (p1 - p2).dot(p - p2) < 0:
        return abs(p - p2)
    return abs((p2 - p1).cross(p - p1)) / abs(p2 - p1)


def getDistance(s1, s2):
    a, b = s1
    c, d = s2
    if intersect(s1, s2):  # intersect
        return 0
    return min(getDistanceSP(s1, c), getDistanceSP(s1, d), getDistanceSP(s2, a), getDistanceSP(s2, b))


def ccw(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    if a.cross(b) > 0:
        return 1  # COUNTER_CLOCKWISE
    elif a.cross(b) < 0:
        return -1  # CLOCKWISE
    elif a.dot(b) < 0:
        return 2  # ONLINE_BACK
    elif abs(a) < abs(b):
        return -2  # ONLINE_FRONT
    else:
        return 0  # ON_SEGMENT


def intersect(s1, s2):
    a, b = s1
    c, d = s2
    return ccw(a, b, c) * ccw(a, b, d) <= 0 and ccw(c, d, a) * ccw(c, d, b) <= 0


def project(l, p):
    p1, p2 = l
    base = p2 - p1
    hypo = p - p1
    return p1 + base * (hypo.dot(base) / abs(base)**2)


class Circle():
    def __init__(self, c, r):
        self.c = c
        self.r = r


def getCrossPoints(c, l):
    pr = project(l, c.c)
    p1, p2 = l
    e = (p2 - p1) / abs(p2 - p1)
    base = math.sqrt(c.r * c.r - (pr - c.c).abs2())
    return [pr + e * base, pr - e * base]


if __name__ == '__main__':

    a, b, r = map(int, input().split())
    c = Circle(Vector2(a, b), r)
    n = int(input())
    res = []
    for _ in range(n):
        ps = list(map(int, input().split()))
        l = [Vector2(ps[0], ps[1]), Vector2(ps[2], ps[3])]

        ans = getCrossPoints(c, l)
        ans = sorted(ans, key=lambda x: (x.x, x.y))
        res.append(ans)

    for ans in res:
        print("{:.8f} {:.8f} {:.8f} {:.8f}".format(
            ans[0].x, ans[0].y, ans[1].x, ans[1].y))
"""
    cf =[
    [-0.43468860, -0.90058083, 0.95192997, -0.30631573],
    [-0.77700043, 0.62950007 ,0.93916259 ,0.34347290],
    [-0.84991694, -0.52691669, 0.92050517, -0.39073037],
    [-0.94804172, 0.31814603 ,-0.63686394, -0.77097621],
    [-0.24253563, 0.97014250 ,0.24253563 ,-0.97014250],
    [-0.31622777, -0.94868330, 0.31622777, 0.94868330],
    [-0.32432432, -0.94594595, 0.00000000, -1.00000000],
    [0.26322452 ,-0.96473460 ,0.83266589 ,0.55377570]]
    for i, ans in enumerate(res):
        print(ans[0].x - cf[i][0], ans[0].y- cf[i][1], ans[1].x- cf[i][2], ans[1].y- cf[i][3])
"""
