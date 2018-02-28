# -*- coding: utf-8 -*-
from operator import itemgetter

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

    n, m = [int(s) for s in input().split()]
    E = []
    for _ in range(m):
        E.append([int(s) for s in input().split(" ")])

    def kruskal(n, E):
        E = sorted(E, key=itemgetter(2))
        totalCost = 0
        S = DisjointSet(n)
        # K = []

        for s, t, w in E:
            if S.findSet(s) != S.findSet(t):
                S.unite(s, t)
                # K.append([s,t,w])
                totalCost += w

        return totalCost

    print(kruskal(n, E))
