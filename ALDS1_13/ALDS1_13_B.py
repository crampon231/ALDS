# -*- coding: utf-8 -*-

from collections import deque
import copy


class Puzzle(list):
    def __init__(self):
        list.__init__(self)
        self.space = None
        self.path = ""

    def __hash__(self):
        return hash(str(self[:]))


if __name__ == '__main__':

    N = 3
    N2 = 9
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    d = ["u", "l", "d", "r"]

    p = Puzzle()
    for i in range(N):
        p += [int(x) for x in input().split()]
    for i in range(N2):
        if p[i] == 0:
            p[i] = N2
            p.space = i
    target = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def isTarget(p):
        return p[:] == target[:]

    def bfs(s):
        Q = deque()
        V = set()
        Q.append(s)
        V.add(s)
        while Q:
            u = Q.popleft()
            if isTarget(u):
                return u.path
            sx = u.space // N
            sy = u.space % N
            for r in range(4):
                tx = sx + dx[r]
                ty = sy + dy[r]
                if not (0 <= tx < N and 0 <= ty < N):
                    continue
                v = Puzzle()
                v[:] = u[:]
                v.path = u.path
                change = tx * N + ty
                v[u.space], v[change] = v[change], v[u.space]
                v.space = change
                if not v in V:
                    V.add(v)
                    v.path += d[r]
                    Q.append(v)

        return "unsolvable"

    ans = bfs(p)
    print(len(ans))
