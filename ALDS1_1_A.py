# -*- coding: utf-8 -*-

def insertionSort(A, N):
    for i in range(1, N):
        print(" ".join(map(str, A)))
        
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
    
    return A

if __name__ == '__main__':

    N = int(input())
    A = [ int(a) for a in input().split(" ")]

    A = insertionSort(A, N)
    print(" ".join(map(str, A)))