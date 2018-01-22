# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, key, prev=None, nex=None):
        self.key = key
        self.prev = prev
        self.next = nex


class DoublyLinkedLiset(object):
    def __init__(self):
        self.nil = Node(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def insert(self, x):
        X = Node(x)
        X.next = self.nil.next
        self.nil.next.prev = X
        self.nil.next = X
        X.prev = self.nil

    def listSearch(self, x):
        cur = self.nil.next
        while (cur != self.nil and cur.key != x):
            cur = cur.next

        return cur

    def deleteNode(self, X):
        if X == self.nil:
            return
        X.prev.next = X.next
        X.next.prev = X.prev
        del X

    def deleteFirst(self):
        self.deleteNode(self.nil.next)

    def deleteLast(self):
        self.deleteNode(self.nil.prev)

    def deleteKey(self, x):
        self.deleteNode(self.listSearch(x))

    def printList(self):
        cur = self.nil.next
        ret = []

        while cur.key is not None:
            ret.append(cur.key)
            cur = cur.next

        print(' '.join(ret))


if __name__ == '__main__':

    n = int(input())
    dll = DoublyLinkedLiset()

    for _ in range(n):
        command = input().split(" ")
        if command[0] == "insert":
            dll.insert(command[1])
        elif command[0] == "delete":
            dll.deleteKey(command[1])
        elif command[0] == "deleteFirst":
            dll.deleteFirst()
        elif command[0] == "deleteLast":
            dll.deleteLast()

    dll.printList()
