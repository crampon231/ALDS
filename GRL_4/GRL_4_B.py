# -*- coding: utf-8 -*-

from collections import deque


if __name__ == '__main__':

    n, m = [int(s) for s in input().split()]
    E = [set() for _ in range(n)]
    for _ in range(m):
        s, t = [int(s) for s in input().split(" ")]
        E[s].add(t)

    color = [0] * n
    indeg = [0] * n
    for s in range(n):
        for t in E[s]:
            indeg[t] += 1

    Q = deque()
    out = []

    def bfs(s):
        Q.append(s)
        color[s] = 1
        while Q:
            u = Q.popleft()
            out.append(u)
            for v in E[u]:
                indeg[v] -= 1
                if indeg[v] == 0 and color[v] == 0:
                    color[v] = 1
                    Q.append(v)

    for u in range(n):
        if indeg[u] == 0 and color[u] == 0:
            bfs(u)

    print("\n".join(map(str, out)))
