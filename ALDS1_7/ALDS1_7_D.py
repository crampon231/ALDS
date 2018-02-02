# -*- coding: utf-8 -*-
from collections import deque
import sys
sys.setrecursionlimit(100000)


if __name__ == '__main__':

    n = int(input())
    pre = deque([int(i) for i in input().split(" ")])
    ino = deque([int(i) for i in input().split(" ")])

    post = []
    def reconstruction(l, r):
        if l >= r:
            return
        c = pre.popleft()
        m = ino.index(c)
        reconstruction(l, m)
        reconstruction(m+1, r)
        
        post.append(c)

    reconstruction(0, n)
    print(" ".join(map(str, post)))