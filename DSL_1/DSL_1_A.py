# -*- coding: utf-8 -*-
class DisjointSet():
    def __init__(self, size):
        self.size = size
        self.rank = [None] * size
        self.parents = [None] * size
        for i in range(size):
            self.makeSet(i)

    def makeSet(self, x):
        self.parents[x] = x
        self.rank[x] = 0

    def findSet(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.findSet(self.parents[x])
        return self.parents[x]

    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def unite(self, x, y):
        self.link(self.findSet(x), self.findSet(y))

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.parents[y] = x
        else:
            self.parents[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1


if __name__ == '__main__':

    n, q = [int(s) for s in input().split(" ")]
    com = [list(map(int, input().split(" "))) for _ in range(q)]
    ds = DisjointSet(n)

    for c, x, y in com:
        if c == 0:
            ds.unite(x, y)
        else:
            print(int(ds.same(x, y)))
