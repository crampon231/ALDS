# -*- coding: utf-8 -*-


if __name__ == '__main__':

    n = int(input())
    M = [list(map(int, input().split(" ")[1:])) for _ in range(n)]

    color = [0] * n
    d = [float("inf")] * n
    p = [None] * n

    def prim():
        d[0] = 0
        p[0] = -1

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
                if color[v] != 2 and M[u][v] != -1:
                    if M[u][v] < d[v]:
                        d[v] = M[u][v]
                        p[v] = u
                        color[v] = 1

    prim()
    sum = 0
    for i in range(n):
        if p[i] != -1:
            sum += M[i][p[i]]

    print(sum)
