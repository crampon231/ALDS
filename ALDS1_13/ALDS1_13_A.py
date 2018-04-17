# -*- coding: utf-8 -*-


if __name__ == '__main__':

    N = 8
    FREE = -1
    NOT_FREE = 1
    row = [FREE] * N
    col = [FREE] * N
    dpos = [FREE] * (2 * N - 1)
    dneg = [FREE] * (2 * N - 1)
    X = [["." for _ in range(N)] for _ in range(N)]

    k = int(input())
    for _ in range(k):
        i, j = map(int, input().split())
        X[i][j] = "Q"
        row[i] = col[j] = dpos[i + j] = dneg[i - j + N - 1] = NOT_FREE

    def printBoard(X):
        for i in range(N):
            print("".join(X[i]))

    def recursive(i):
        if i == N:
            printBoard(X)
            return
        if "Q" in X[i]:
            recursive(i + 1)

        for j in range(N):
            if NOT_FREE in [row[i], col[j], dpos[i + j], dneg[i - j + N - 1]]:
                continue
            else:
                X[i][j] = "Q"
                row[i] = col[j] = dpos[i + j] = dneg[i - j + N - 1] = NOT_FREE
            recursive(i + 1)
            X[i][j] = "."
            row[i] = col[j] = dpos[i + j] = dneg[i - j + N - 1] = FREE

    recursive(0)
