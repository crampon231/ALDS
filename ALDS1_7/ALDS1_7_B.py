# -*- coding: utf-8 -*-


class Node():
    def __init__(self, parent=-1, left=-1, right=-1, depth=0, height=0, sibling=-1, degree=0):
        self.parent = parent
        self.left = left
        self.right = right
        self.depth = depth
        self.height = height
        self.sibling = sibling
        self.degree = degree


if __name__ == '__main__':

    n = int(input())
    T = [Node() for i in range(n)]

    for _ in range(n):
        i, left, right = [int(s) for s in input().split(" ")]
        has_left = (left != -1)
        has_right = (right != -1)
        if has_left:
            T[i].left = left
            T[left].parent = i
            T[i].degree += 1
        if has_right:
            T[i].right = right
            T[right].parent = i
            T[i].degree += 1
        if has_left and has_right:
            T[left].sibling = right
            T[right].sibling = left

    def setDepth(u, p):
        T[u].depth = p
        if T[u].right != -1:
            setDepth(T[u].right, p + 1)
        if T[u].left != -1:
            setDepth(T[u].left, p + 1)

    def setHeight(u):
        h1 = 0
        h2 = 0
        if T[u].right != -1:
            h1 = setHeight(T[u].right) + 1
        if T[u].left != -1:
            h2 = setHeight(T[u].left) + 1
        T[u].height = max(h1, h2)
        return T[u].height

    for i, n in enumerate(T):
        if n.parent == -1:
            root = i

    setDepth(root, 0)
    setHeight(root)

    for i, node in enumerate(T):
        if node.parent == -1:
            n_type = "root"
        elif node.left != -1 or node.right != -1:
            n_type = "internal node"
        else:
            n_type = "leaf"

        print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(
            i, node.parent, node.sibling, node.degree, node.depth, node.height, n_type))
