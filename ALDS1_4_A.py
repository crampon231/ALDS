# -*- coding: utf-8 -*-


def linearSearch(l, key):
    m = len(l)
    l.append(key)
    i = 0
    while l[i] != key:
        i += 1
    l.pop()
    if i == m:
        return "NOT_FOUND"
    return i


if __name__ == '__main__':

    n = int(input())
    S = [int(s) for s in input().split(" ")]
    q = int(input())
    T = [int(t) for t in input().split(" ")]

    count = 0
    for t in T:
        if linearSearch(S, t) != "NOT_FOUND":
            count += 1

    print(count)
