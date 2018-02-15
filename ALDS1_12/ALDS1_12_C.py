# -*- coding: utf-8 -*-
from heapq import heappush, heappop

if __name__ == '__main__':

    n = int(input())
    M = [set() for i in range(n)]

    for i in range(n):
        l = list(map(int, input().split(" ")))
        for k in range(l[1]):
            j = l[2 + 2 * k]
            c = l[2 + 2 * k + 1]
            M[i].add((j, c))

    d = [float("inf")] * n
    h = []

    def dijkstra(s):
        color = [0] * n
        p = [None] * n
        d[s] = 0
        heappush(h, (d[s], s))

        while h:
            _, u = heappop(h)

            color[u] = 2

            for v, c in M[u]:
                if color[v] != 2:
                    if d[u] + c < d[v]:
                        d[v] = d[u] + c
                        color[v] = 1
                        heappush(h, (d[v], v))

    dijkstra(0)
    for i in range(n):
        print(i, d[i])
