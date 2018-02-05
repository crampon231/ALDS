# -*- coding: utf-8 -*-


if __name__ == '__main__':

    n = int(input())
    F = [None]*(n+1)

    def fibonacci(n):
        if n == 0 or n == 1:
            F[n] = 1
            return F[n]
        if F[n] is not None:
            return F[n]
        
        F[n] = fibonacci(n-2) + fibonacci(n-1)
        return F[n]

    print(fibonacci(n))

