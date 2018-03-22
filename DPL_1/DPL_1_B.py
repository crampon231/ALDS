# -*- coding: utf-8 -*-


if __name__ == '__main__':

    N, W = map(int, input().split())
    I = [None] + [list(map(int, input().split())) for _ in range(N)]
    C = [[0 for _ in range(W + 1)] for _ in range(N + 1)]

    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if I[i][1] <= w:
                C[i][w] = max(C[i - 1][w - I[i][1]] + I[i][0], C[i - 1][w])
            else:
                C[i][w] = C[i - 1][w]

    print(C[N][W])
