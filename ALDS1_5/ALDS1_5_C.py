# -*- coding: utf-8 -*-
from math import sin, cos, pi



def koch(d, p1, p2):
    if d == 0:
        return

    s = [None, None]
    u = [None, None]
    t = [None, None]
    
    s[0] = (2*p1[0] + p2[0])/3
    s[1] = (2*p1[1] + p2[1])/3
    t[0] = (p1[0] + 2*p2[0])/3
    t[1] = (p1[1] + 2*p2[1])/3
    u[0] = (t[0] - s[0])*cos(1/3*pi) - (t[1] - s[1])*sin(1/3*pi) + s[0]
    u[1] = (t[0] - s[0])*sin(1/3*pi) + (t[1] - s[1])*cos(1/3*pi) + s[1]

    koch(d-1, p1, s)
    print(s[0], s[1])
    koch(d-1, s, u)
    print(u[0], u[1])
    koch(d-1, u, t)
    print(t[0], t[1])
    koch(d-1, t, p2)

if __name__ == '__main__':

    n = int(input())
    a = [0, 0]
    b = [100, 0]

    print(a[0], a[1])
    koch(n ,a ,b)
    print(b[0] ,b[1])

    