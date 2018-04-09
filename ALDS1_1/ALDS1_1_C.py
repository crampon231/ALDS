# -*- coding: utf-8 -*-

import math


def isPrime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':

    n = int(input())
    cnt = 0
    for _ in range(n):
        x = int(input())
        if isPrime(x):
            cnt += 1

    print(cnt)
