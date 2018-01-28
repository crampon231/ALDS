# -*- coding: utf-8 -*-

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j][1] <= x[1]:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
    
def merge(A, left, mid, right):
    n1 = mid - left
    n2 = right - mid
    L = A[left:left+n1]
    R = A[mid:mid+n2]
    L.append([None, float('inf')])
    R.append([None, float('inf')])
    
    i = 0
    j = 0
    for k in range(left, right):
        if L[i][1] <= R[j][1]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)


if __name__ == '__main__':

    n = int(input())
    A = [input().split(" ") for _ in range(n)]
    
    A_m = [(a[0], int(a[1])) for a in A]
    A_q = [(a[0], int(a[1])) for a in A]

    mergeSort(A_m, 0, n)
    quickSort(A_q, 0, n-1)

    if A_m == A_q:
        print("Stable")
    else:
        print("Not stable")

    for a in A_q:
        print(a[0], a[1])


