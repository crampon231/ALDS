# -*- coding: utf-8 -*-

from itertools import chain

if __name__ == '__main__':

    H, W = map(int, input().split())
    C = []
    hist = []
    for i in range(H):
        l = input().split()
        C.append([int(x) for x in l])
        hist.append([(int(x) + 1) % 2 for x in l])

    for i in range(1, H):
        for j in range(W):
            if C[i][j] == 0:
                hist[i][j] = hist[i - 1][j] + 1

    S = []
    max_area = 0
    for i in range(H):
        for j in range(W):
            rect = [j, hist[i][j]]
            if not S:
                S.append(rect)
            elif S[-1][1] < rect[1]:
                S.append(rect)
            elif S[-1][1] > rect[1]:
                while S and S[-1][1] > rect[1]:
                    post_rect = S.pop()
                    area = post_rect[1] * (j - post_rect[0])
                    max_area = max(max_area, area)
                S.append([post_rect[0], rect[1]])
        while S:
            post_rect = S.pop()
            area = post_rect[1] * (W - post_rect[0])
            max_area = max(max_area, area)

    print(max_area)
