# -*- coding: utf-8 -*-


def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j + g] = A[j]
            j -= g
            cnt += 1
        A[j + g] = v


def shellSort(A, n):

    def func(m):
        if m == 0:
            return 1
        else:
            return func(m - 1) * 3 + 1

    G = []
    i = 0

    while True:
        gi = func(i)
        if gi <= n:
            G.append(gi)
            i += 1
        else:
            break

    G = G[::-1]
    for g in G:
        insertionSort(A, n, g)

    return A, G


if __name__ == '__main__':

    n = int(input())
    A = [int(input()) for i in range(n)]

    cnt = 0
    A, G = shellSort(A, n)

    print(len(G))
    print(" ".join(map(str, G)))
    print(cnt)
    for i in range(n):
        print(A[i])
