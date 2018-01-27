# -*- coding: utf-8 -*-


if __name__ == '__main__':

    n = int(input())
    A = [int(a) for a in input().split(" ")]
    q = int(input())
    M = [int(m) for m in input().split(" ")]

    def solve(i, m):
        if m == 0:
            return True
        if i >= n or m > sum(A):
            return False
        res = solve(i+1, m) or solve(i+1, m-A[i])
        return res

    ans = []
    for m in M:
        if solve(0, m):
            ans.append("yes")
        else:
            ans.append("no")

    print("\n".join(ans))
