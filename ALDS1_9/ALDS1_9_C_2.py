# -*- coding: utf-8 -*-
from heapq import heappush, heappop

if __name__ == '__main__':

    q = []
    while True:
        c = input().split(" ")
        if c[0]=='end':
            break
        if c[0]=='insert':
            heappush(q, -int(c[1]))
        else:
            print(-heappop(q))