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

    def print(self):
        self.inorder()
        self.preorder()

    def find(self, k):
        x = self.root
        while x is not None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def delete(self, z):
        # y is delete node.
        if z.left is None or z.right is None:
            y = z
        else:
            y = self.getSuccessor(z)
        
        if y.left is not None:
            x = y.left
        else:
            x = y.right
        
        if x is not None:
            x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x
        
        if y != z:
            z.key = y.key

        

    def getSuccessor(self, x):
        if x.right is not None:
            return self.getMinimum(x.right)

        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def getMinimum(self, x):
        while x.left is not None:
            x = x.left
        return x


if __name__ == '__main__':

    n = int(input())
    command = [input().split(" ") for _ in range(n)]
    T = BinarySearchTree()

    for c in command:
        if c[0] == "insert":
            T.insert(int(c[1]))
        elif c[0] == "find":
            z = T.find(int(c[1]))
            if z is None:
                print("no")
            else:
                print("yes")
        elif c[0] == "delete":
            z = T.find(int(c[1]))
            T.delete(z)
        else:
            T.print()