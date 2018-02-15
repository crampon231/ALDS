# -*- coding: utf-8 -*-


if __name__ == '__main__':

    n = int(input())
    M = [[float("inf") for j in range(n)] for i in range(n)]

    for i in range(n):
        l = list(map(int, input().split(" ")))
        for k in range(l[1]):
            j = l[2 + 2 * k]
            c = l[2 + 2 * k + 1]
            M[i][j] = c

    d = [float("inf")] * n

    def dijkstra(s):
        color = [0] * n
        p = [None] * n
        d[s] = 0
        p[s] = -1

        while True:
            mincost = float("inf")
            for i in range(n):
                if color[i] != 2 and d[i] < mincost:
                    mincost = d[i]
                    u = i

            if mincost == float("inf"):
                break

            color[u] = 2

            for v in range(n):
                if color[v] != 2:
                    if d[u] + M[u][v] < d[v]:
                        d[v] = d[u] + M[u][v]
                        p[v] = u
                        color[v] = 1

    dijkstra(0)
    for i in range(n):
        print(i, d[i])
