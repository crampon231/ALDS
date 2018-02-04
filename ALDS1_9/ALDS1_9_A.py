# -*- coding: utf-8 -*-


if __name__ == '__main__':

    H = int(input())
    A = [None] + [int(i) for i in input().split(" ")]

    def parent(i):
        return i // 2

    def left(i):
        return 2*i

    def right(i):
        return 2*i + 1

    for i in range(1, H+1):
        print("node {}: key = {},".format(i, A[i]), end=" ")
        if parent(i) >= 1:
            print("parent key = {},".format(A[parent(i)]), end=" ")
        if left(i) <= H:
            print("left key = {},".format(A[left(i)]), end=" ")
        if right(i) <= H:
            print("right key = {},".format(A[right(i)]), end=" ")
        print("")
