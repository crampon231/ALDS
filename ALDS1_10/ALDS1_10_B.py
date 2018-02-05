# -*- coding: utf-8 -*-


if __name__ == '__main__':

    n = int(input())
    p = [0]
    for _ in range(n):
        r, c = list(map(int, input().split(" ")))
        p[-1] = r
        p.append(c)
    m = [[0 for i in range(n+1)] for j in range(n+1)]
    
    for i in range(1, n+1):
        m[i][i] = 0
    
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j])

    print(m[1][n])


