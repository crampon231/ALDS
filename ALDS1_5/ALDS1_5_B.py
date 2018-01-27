# -*- coding: utf-8 -*-

def merge(A, left, mid, right):
    global cnt
    n1 = mid - left
    n2 = right - mid
    L = A[left:left+n1]
    R = A[mid:mid+n2]
    L.append(float('inf'))
    R.append(float('inf'))
    
    i = 0
    j = 0
    for k in range(left, right):
        cnt += 1
        if L[i] <= R[j]:
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
    S = [int(s) for s in input().split(" ")]
    cnt = 0

    mergeSort(S, 0, n)

    print(" ".join(map(str, S)))
    print(cnt)