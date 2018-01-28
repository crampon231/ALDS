# -*- coding: utf-8 -*-


def CountingSort(A, k, n):
    B = [None]*(n+1)
    C = [0]*k
    
    for j in range(1, n+1):
        C[A[j]] += 1

    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    
    for j in range(n, 0, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1
    
    return B


if __name__ == '__main__':
    k = 10000
    n = int(input())
    A = [None] + [int(a) for a in input().split(" ")]
    
    B = CountingSort(A, k, n)
    print(" ".join(map(str, B[1:])))
