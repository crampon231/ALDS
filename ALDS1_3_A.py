# -*- coding: utf-8 -*-

if __name__ == '__main__':

    stack = []
    line = input().split(" ")
    for s in line:
        if s.isdigit():
            stack.append(s)
        else:
            v2 = stack.pop()
            v1 = stack.pop()
            stack.append(str(eval(v1 + s + v2)))

    print(stack.pop())

