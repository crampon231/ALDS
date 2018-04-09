# -*- coding: utf-8 -*-


def pow(x, n, M=1):
    if n == 0:
        return 1
    res = pow((x * x) % M, n // 2, M)
    if n % 2 == 1:
        res = (res * x) % M
    return res


if __name__ == '__main__':

    M = 1000000007
    m, n = map(int, input().split())
    print(pow(m, n, M))
