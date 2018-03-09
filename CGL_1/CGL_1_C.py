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
    if 0:  # intersect
        return 0
    a, b = s1
    c, d = s2
    return min(getDistanceSP(s1, c), getDistanceSP(s1, d), getDistanceSP(s2, a), getDistanceSP(s2, b))


def ccw(p0, p1, p2):
    a = p1 - p0
    b = p2 - p0
    if a.cross(b) > 0:
        return 1
    elif a.cross(b) < 0:
        return -1
    elif a.dot(b) < 0:
        return 2
    elif abs(a) < abs(b):
        return -2
    else:
        return 0


if __name__ == '__main__':

    a, b, c, d = map(int, input().split())
    p0 = Vector2(a, b)
    p1 = Vector2(c, d)
    q = int(input())
    ans = []
    for _ in range(q):
        e, f = map(int, input().split())
        p2 = Vector2(e, f)
        ans.append(ccw(p0, p1, p2))
    dic = {1: "COUNTER_CLOCKWISE", -1: "CLOCKWISE",
           2: "ONLINE_BACK", -2: "ONLINE_FRONT", 0: "ON_SEGMENT"}
    for a in ans:
        print(dic[a])
