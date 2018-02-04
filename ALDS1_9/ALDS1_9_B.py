# -*- coding: utf-8 -*-


def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def maxHeapify(A, i):
    global H
    l = left(i)
    r = right(i)
    if l <= H and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r <= H and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest)


def buildMaxHeap(A):
    for i in range(H // 2, 0, -1):
        maxHeapify(A, i)


if __name__ == '__main__':

    H = int(input())
    A = [None] + [int(i) for i in input().split(" ")]

    buildMaxHeap(A)

    print(" " + " ".join(map(str, A[1:])))
