# -*- coding: utf-8 -*-

from collections import deque

if __name__ == '__main__':
    n = int(input())
    L = deque()

    for _ in range(n):
        command = input().split(" ")
        if command[0] == "insert":
            L.appendleft(command[1])
        elif command[0] == "delete":
            try:
                L.remove(command[1])
            except:
                pass
        elif command[0] == "deleteFirst":
            L.popleft()
        elif command[0] == "deleteLast":
            L.pop()

    print(" ".join(L))
