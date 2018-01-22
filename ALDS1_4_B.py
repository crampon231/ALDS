# -*- coding: utf-8 -*-


def binarySearch(A, key):
    left = 0
    right = len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] == key:
            return mid
        elif key < A[mid]:
            right = mid
        else:
            left = mid + 1

    return "NOT_FOUND"


if __name__ == '__main__':

    n = int(input())
    S = [int(s) for s in input().split(" ")]
    q = int(input())
    T = [int(t) for t in input().split(" ")]

    count = 0
    for t in T:
        if binarySearch(S, t) != "NOT_FOUND":
            count += 1

    print(count)
