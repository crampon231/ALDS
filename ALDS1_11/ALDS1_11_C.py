# -*- coding: utf-8 -*-
from collections import deque


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
    d = [-1] * n
    Q = deque()

    def bfs(s):  # breadth-first search
        color[s] = 1
        d[s] = 0
        Q.append(s)

        while len(Q) != 0:
            u = Q.popleft()
            for v in range(n):
                if M[u][v] == 1 and color[v] == 0:
                    color[v] = 1
                    d[v] = d[u] + 1
                    Q.append(v)
            color[u] = 2

    bfs(0)
    for i in range(n):
        print(i + 1, d[i])
