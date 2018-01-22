# -*- coding: utf-8 -*-


def bubbleSort(A, N):
    flag = True  # 未ソートの可能性があるか
    i = 0  # 未ソート部分の先頭
    inv_num = 0  # 転倒数
    while flag:
        flag = False
        for j in range(N - 1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                flag = True
                inv_num += 1
        i += 1

    return A, inv_num


if __name__ == '__main__':

    N = int(input())
    A = [int(a) for a in input().split(" ")]

    A, inv_num = bubbleSort(A, N)
    print(" ".join(map(str, A)))
    print(inv_num)
