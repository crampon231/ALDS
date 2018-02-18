# -*- coding: utf-8 -*-


if __name__ == '__main__':

    n, m = [int(s) for s in input().split()]
    A = [[float("inf") for j in range(n)] for i in range(n)]

    for i in range(n):
        A[i][i] = 0

    for _ in range(m):
        s, t, d = map(int, input().split())
        A[s][t] = d

    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])

    negative = False
    for i in range(n):
        if A[i][i] < 0:
            negative = True

    if negative:
        print("NEGATIVE CYCLE")
    else:
        for i in range(n):
            print(" ".join(map(lambda x: str(x).upper(), A[i])))
