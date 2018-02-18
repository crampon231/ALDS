# -*- coding: utf-8 -*-


class Node():
    def __init__(self, loc=None, left=None, right=None):
        self.loc = loc
        self.l = left
        self.r = right

class Point():
    def __init__(self, id, xy):
        self.id = int(id)
        self.x = int(xy[0])
        self.y = int(xy[1])

if __name__ == '__main__':

    n = int(input())
    P = [Point(i, input().split(" ")) for i in range(n)]
    q = int(input())
    Q = [list(map(int, input().split(" "))) for _ in range(q)]
    T = [None] * n

    def make2DTree(l, r, depth):
        global np
        if l >= r:
            return None

        mid = (l + r) // 2
        t = np
        np += 1
        if depth % 2 == 0:
            P[l:r] = sorted(P[l:r], key=lambda p: p.x)
        else:
            P[l:r] = sorted(P[l:r], key=lambda p: p.y)

        T[t] = Node(loc=mid)
        T[t].l = make2DTree(l, mid, depth + 1)
        T[t].r = make2DTree(mid + 1, r, depth + 1)

        return t

    def find(v, sx, tx, sy, ty, depth, ans):
        x = P[T[v].loc].x
        y = P[T[v].loc].y

        if (sx <= x <= tx) and (sy <= y <= ty):
            ans.append(P[T[v].loc].id)

        if depth % 2 == 0:
            if T[v].l is not None and sx <= x:
                find(T[v].l, sx, tx, sy, ty, depth + 1, ans)
            if T[v].r is not None and x <= tx:
                find(T[v].r, sx, tx, sy, ty, depth + 1, ans)

        else:
            if T[v].l is not None and sy <= y:
                find(T[v].l, sx, tx, sy, ty, depth + 1, ans)
            if T[v].r is not None and y <= ty:
                find(T[v].r, sx, tx, sy, ty, depth + 1, ans)

    np = 0
    root = make2DTree(0, n, 0)

    for sx, tx, sy, ty in Q:
        ans = []
        find(root, sx, tx, sy, ty, 0, ans)
        ans.sort()
        if ans:
            print("\n".join(map(str, ans)))
        print("")
