# -*- coding: utf-8 -*-


def selectionSort(A, N):
    count = 0
        
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        if minj != i:
            count += 1

        A[i], A[minj] = A[minj], A[i]

    return A, count

if __name__ == '__main__':

    N = int(input())
    A = [int(a) for a in input().split(" ")]

    A, count = selectionSort(A, N)
    print(" ".join(map(str, A)))
    print(count)
