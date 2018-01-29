# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(100000)

class Node():
    def __init__(self, ID=None, parent=-1, left=-1, right=-1):
        self.id = ID
        self.parent = parent
        self.left = left
        self.right = right

def preParse(u):
    if u == -1:
        return
    print(" " + str(u), end="")
    preParse(T[u].left)
    preParse(T[u].right)
    
def inParse(u):
    if u == -1:
        return
    inParse(T[u].left)
    print(" " + str(u), end="")
    inParse(T[u].right)
    
def postParse(u):
    if u == -1:
        return
    postParse(T[u].left)
    postParse(T[u].right)
    print(" " + str(u), end="")
    
    
if __name__ == '__main__':

    n = int(input())
    T = [Node() for i in range(n)]

    for _ in range(n):
        ID, left, right = list(map(int, input().split(" ")))
        T[ID].id = ID
        T[ID].left = left
        T[ID].right = right
        if left != -1:
            T[left].parent = ID
        if right != -1:
            T[right].parent = ID
    
    for node in T:
        if node.parent==-1:
            r = node.id
    
    print("Preorder")
    preParse(r)
    print()
        
    print("Inorder")
    inParse(r)
    print()
    
    print("Postorder")
    postParse(r)
    print()
    