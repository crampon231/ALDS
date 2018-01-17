# -*- coding: utf-8 -*-


def bubbleSort(A, N):

    flag = True  # 未ソートの可能性があるか
    i = 0  # 未ソート部分の先頭
    inv_num = 0  # 転倒数
    while flag:
        flag = False
        for j in range(N - 1, i, -1):
            if A[j][1] < A[j - 1][1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                flag = True
                inv_num += 1
        i += 1

    return A, inv_num


def selectionSort(A, N):
    count = 0

    for i in range(N):

        minj = i
        for j in range(i, N):
            if A[j][1] < A[minj][1]:
                minj = j
        if minj != i:
            count += 1

        A[i], A[minj] = A[minj], A[i]

    return A, count


if __name__ == '__main__':

    N = int(input())
    A = [(a[0], int(a[1])) for a in input().split(" ")]

    A_bubble, _ = bubbleSort(A.copy(), N)
    A_selection, _ = selectionSort(A.copy(), N)

    A_bubble = [a[0] + str(a[1]) for a in A_bubble]
    A_selection = [a[0] + str(a[1]) for a in A_selection]

    print(' '.join(A_bubble))
    print("Stable")
    print(" ".join(A_selection))
    if A_selection == A_bubble:
        print("Stable")
    else:
        print("Not stable")
