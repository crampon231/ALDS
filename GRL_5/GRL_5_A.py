# -*- coding: utf-8 -*-

from collections import deque


if __name__ == '__main__':

    n = int(input())
    E = [set() for _ in range(n)]
    for _ in range(n - 1):
        s, t, d = map(int, input().split())
        E[s].add((t, d))
        E[t].add((s, d))

    Q = deque()

    def bfs(s):
        d = [float("inf")] * n
        Q.append(s)
        d[s] = 0
        while Q:
            u = Q.popleft()
            for v, w in E[u]:
                if d[v] == float("inf"):
                    d[v] = d[u] + w
                    Q.append(v)

        return d

    d = bfs(0)
    tgt = d.index(max(d))
    d = bfs(tgt)
    print(max(d))
