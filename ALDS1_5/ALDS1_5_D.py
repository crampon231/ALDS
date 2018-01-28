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
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            cnt += n1 - i
            j += 1


def mergeSort(A, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge(A, left, mid, right)
    

if __name__ == '__main__':

    n = int(input())
    A = [int(a) for a in input().split(" ")]
    cnt = 0
    mergeSort(A, 0, n)
    print(cnt)
