# -*- coding: utf-8 -*-


if __name__ == '__main__':
    n, m = map(int, input().split())
    C = [int(x) for x in input().split()]
    T = [float("inf") for _ in range(n+1)]
    T[0] = 0

    for i in range(m):
        for j in range(C[i], n+1):
            T[j] = min(T[j], T[j - C[i]] + 1)

    print(T[n])
