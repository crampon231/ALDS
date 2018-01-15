# -*- coding: utf-8 -*-

def maximum_profit_1(n, R):
    maxv = R[1] - R[0]
    for j in range(1, n):
        for i in range(j):
            maxv = max(maxv, R[j]-R[i])

    return maxv

def maximum_profit_2(n, R):
    minv = R[0]
    maxv = R[1] - R[0]
    for j in range(1, n):
        maxv = max(maxv, R[j]-minv)
        minv = min(minv, R[j])

    return maxv

if __name__ == '__main__':

    n = int(input())
    R = [ int(input()) for i in range(n)]

    ans = maximum_profit_2(n ,R)
    print(ans)