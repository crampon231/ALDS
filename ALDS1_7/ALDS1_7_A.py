# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(200000)

class Node():
    def __init__(self, ID, parent=-1, left=-1, right=-1, depth=0, children=[]):
        self.id = ID
        self.parent = parent
        self.left = left
        self.right = right
        self.depth = depth
        self.children = children


if __name__ == '__main__':

    n = int(input())
    tree = [Node(i) for i in range(n)]

    for _ in range(n):
        line = [int(l) for l in input().split(" ")]
        ID = line[0]
        d = line[1]
        if d == 0:
            continue
        else:
            children = line[2:]
            tree[ID].children = children
            tree[ID].left = children[0]
            for j in range(0, d):
                tree[children[j]].parent = ID
                if j < d - 1:
                    tree[children[j]].right = children[j + 1]

    def setDepth(u, p):
        tree[u].depth = p
        if tree[u].right != -1:
            setDepth(tree[u].right, p)
        if tree[u].left != -1:
            setDepth(tree[u].left, p + 1)

    for node in tree:
        if node.parent == -1:
            root = node.id

    setDepth(root, 0)

    for node in tree:
        if node.parent == -1:
            n_type = "root"
        elif node.left != -1:
            n_type = "internal node"
        else:
            n_type = "leaf"

        print("node {}: parent = {}, depth = {}, {}, {}".format(
            node.id, node.parent, node.depth, n_type, node.children))
        