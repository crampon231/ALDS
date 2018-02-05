# -*- coding: utf-8 -*-


if __name__ == '__main__':

    
    def lcs(X, Y):
        m = len(X)
        n = len(Y)
        c = [[-1 for i in range(n+1)] for j in range(m+1)]
        X = " " + X
        Y = " " + Y
        for i in range(m+1):
            c[i][0] = 0
        for j in range(1, n+1):
            c[0][j] = 0
        for i  in range(1, m+1):
            for j in range(1, n+1):
                if X[i] == Y[j]:
                    c[i][j] = c[i-1][j-1] + 1
                else:
                    c[i][j] = max(c[i-1][j], c[i][j-1])
        return c[m][n]

    def lcs2(X, Y):
        n = len(Y)
        dp = [0]*(n+1)
    
        for c in X:
            tmp = dp[:]
            for j in range(n):
                if c == Y[j]:
                    dp[j+1] = tmp[j] + 1
                elif dp[j+1] < dp[j]:
                    dp[j+1] = dp[j]
    
        return dp[-1]

    q = int(input())
    for _ in range(q):
        X = input()
        Y = input()
        print(lcs2(X,Y))

