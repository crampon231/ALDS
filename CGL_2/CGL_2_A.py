# -*- coding: utf-8 -*-

import collections
import math


class Vector2(collections.namedtuple("Vector2", ["x",  "y"])):

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

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

    n = int(input())
    
    for _ in range(n):
        l = list(map(int, input().split()))
        s1 = Vector2(l[2], l[3]) - Vector2(l[0], l[1])
        s2 = Vector2(l[6], l[7]) - Vector2(l[4], l[5])

        if abs(s1.dot(s2)) == 0:
            print(1)
        elif abs(s1.cross(s2)) == 0:
            print(2)
        else:
            print(0)
