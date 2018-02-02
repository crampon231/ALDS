# -*- coding: utf-8 -*-


class Node():
    def __init__(self, key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class BinarySearchTree(list):
    def __init__(self):
        list.__init__(self)
        self.root = None

    def insert(self, z):
        z = Node(z)
        y = None
        x = self.root

        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def preorder(self):
        def preParse(u):
            if u == None:
                return
            print(" " + str(u.key), end="")
            preParse(u.left)
            preParse(u.right)
        preParse(self.root)
        print("")

    def inorder(self):
        def inParse(u):
            if u == None:
                return
            inParse(u.left)
            print(" " + str(u.key), end="")
            inParse(u.right)
        inParse(self.root)
        print("")


if __name__ == '__main__':

    n = int(input())
    command = [input().split(" ") for _ in range(n)]
    T = BinarySearchTree()

    for c in command:
        if c[0] == "insert":
            T.insert(int(c[1]))
        else:
            T.inorder()
            T.preorder()
