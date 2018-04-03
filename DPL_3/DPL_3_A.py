# -*- coding: utf-8 -*-

from itertools import chain

if __name__ == '__main__':

    H, W = map(int, input().split())
    C = []
    dp = []
    for i in range(H):
        l = input().split()
        C.append([int(x) for x in l])
        dp.append([(int(x) + 1) % 2 for x in l])

    for i in range(1, H):
        for j in range(1, W):
            if C[i][j] == 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                               dp[i - 1][j - 1]) + 1
                
    max_width = max(list(chain.from_iterable(dp)))
    print(max_width**2)
