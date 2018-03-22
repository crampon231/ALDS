# -*- coding: utf-8 -*-

import bisect

if __name__ == '__main__':

    n = int(input())
    a = [int(input()) for _ in range(n)]

    L = [None] * n
    L[0] = a[0]
    length = 1

    for i in range(1, n):
        if L[length - 1] < a[i]:
            L[length] = a[i]
            length += 1
        else:
            indx = bisect.bisect_left(L[:length], a[i])
            L[indx] = a[i]

    print(length)
