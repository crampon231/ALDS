# -*- coding: utf-8 -*-


if __name__ == '__main__':

    n = int(input())
    A = [int(a) for a in input().split(" ")]
    B = A.copy()
    B.sort()
    V = [False]*n
    T = {B[i]:i for i in range(n)}

    ans = 0
    s = min(A)

    for i in range(n):
        if V[i]:
            continue
        cur = i
        S = 0 # sum of weight
        m = 10000 # min of cycle(init max weight)
        an = 0 # length of cycle
        while not V[cur]:
            V[cur] = True
            an += 1
            v = A[cur]
            m = min(m, v)
            S += v
            cur = T[v]
        ans += min(S + (an - 2)*m, m + S + (an + 1)*s)

    print(ans)