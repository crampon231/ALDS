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


if __name__ == '__main__':

    a, b, c, d = map(int, input().split())
    p1 = Vector2(a, b)
    p2 = Vector2(c, d)
    base = p2 - p1
    q = int(input())
    ans = []
    for _ in range(q):
        e, f = map(int, input().split())
        p = Vector2(e, f)
        hypo = Vector2(e - a, f - b)
        proj = p1 + base * (hypo.dot(base) / float(base.x**2 + base.y**2))
        x = p + (proj - p) * 2
        ans.append(x)

    for x in ans:
        print(x.x, x.y)
