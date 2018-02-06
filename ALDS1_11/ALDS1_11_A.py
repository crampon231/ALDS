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
                M[u-1][v-1] = 1
        
    for r in M:
        print(" ".join(map(str, r)))