# -*- coding: utf-8 -*-
import math
from operator import itemgetter
from bisect import bisect_left, bisect_right

if __name__ == '__main__':

    P = [tuple(map(int, input().split())) + (i,)
         for i in range(int(input()))]  # (x,y,i)
    P.sort()
    root = int(math.sqrt(len(P)))
    low = [x for x, y, i in P[::root]]
    high = [x for x, y, i in P[root - 1::root]] + [float('inf')]

    # disjoint subsets (ordered by y) of P
    P = [sorted(P[i:i + root], key=itemgetter(1))
         for i in range(0, len(P), root)]
    P = [([y for x, y, i in Pi], Pi)
         for Pi in P]  # ([y in subsets], [subsets])
    q = int(input())
    Q = [list(map(int, input().split(" "))) for _ in range(q)]

    for sx, tx, sy, ty in Q:
        ret = []
        for i in range(bisect_left(high, sx), bisect_right(low, tx)):
            k, v = P[i]
            for i in range(bisect_left(k, sy), bisect_right(k, ty)):
                if sx <= v[i][0] <= tx:
                    ret.append(v[i][2])
        if ret:
            ret.sort()
            print('\n'.join(map(str, ret)))
        print()
