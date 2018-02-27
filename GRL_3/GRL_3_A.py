# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(200000)


if __name__ == '__main__':

    n, m = [int(s) for s in input().split()]
    E = [set() for _ in range(n)]
    for _ in range(m):
        s, t = [int(s) for s in input().split(" ")]
        E[s].add(t)
        E[t].add(s)

    def dfs(current, prev):
        global timer
        prenum[current] = timer
        lowest[current] = prenum[current]
        timer += 1

        visited[current] = 1

        for v in E[current]:
            if visited[v] == 0:
                parent[v] = current
                dfs(v, current)
                lowest[current] = min(lowest[current], lowest[v])
            elif v != prev:  # current -> v is back-edge
                lowest[current] = min(lowest[current], prenum[v])

    prenum = [None] * n
    parent = [None] * n
    lowest = [float("inf")] * n
    timer = 1
    visited = [0] * n

    dfs(0, -1)

    ap = []
    np = 0
    for i in range(1, n):
        p = parent[i]
        if p == 0:
            np += 1
        elif prenum[p] <= lowest[i]:
            ap.append(p)

    if np > 1:
        ap.append(0)

    ap = list(set(ap))
    ap.sort()
    if ap:
        print("\n".join(map(str, ap)))
