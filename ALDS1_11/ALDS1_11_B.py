# -*- coding: utf-8 -*-


if __name__ == '__main__':

    n = int(input())
    M = [[0 for i in range(n)] for j in range(n)]
    for _ in range(n):
        l = list(map(int, input().split(" ")))
        u = l[0]
        k = l[1]
        if k != 0:
            for v in l[2:]:
                M[u - 1][v - 1] = 1

    color = [0] * n
    d = [0] * n
    f = [0] * n
    time = 0

    def dfs(u):  # depth-first search
        global time
        color[u] = 1
        time += 1
        d[u] = time
        for v in range(n):
            if M[u][v] == 1 and color[v] == 0:
                dfs(v)
        color[u] = 2
        time += 1
        f[u] = time

    for u in range(n):
        if color[u] == 0:
            dfs(u)

    for u in range(n):
        print(u + 1, d[u], f[u])
