# -*- coding: utf-8 -*-

def parent(i):
    return i // 2


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1

class MaxHeap(list):
    def __init__(self, H=0):
        list.__init__(self)
        self.H = H
        self[:] = [None]

    def insert(self, key):
        self.H += 1
        self.append(-float("inf"))
        self.heapIncreaseKey(self.H, key)

    def heapIncreaseKey(self, i, key):
        if key < self[i]:
            return
        self[i] = key
        while i > 1 and self[parent(i)] < self[i]:
            pi = parent(i)
            self[i], self[pi] = self[pi], self[i]
            i = pi

    def heapExtract(self):
        if self.H < 1:
            raise "underflow"
        maximum = self[1]
        self[1] = self.pop()
        self.H -= 1
        self.maxHeapify(1)

        return maximum

    def maxHeapify(self, i):
        l = left(i)
        r = right(i)
        if l <= self.H and self[l] > self[i]:
            largest = l
        else:
            largest = i
        if r <= self.H and self[r] > self[largest]:
            largest = r

        if largest != i:
            self[i], self[largest] = self[largest], self[i]
            self.maxHeapify(largest)


if __name__ == '__main__':

    A = MaxHeap()
    while True:
        c = input().split(" ")
        if c[0] == "insert":
            A.insert(int(c[1]))
        elif c[0] == "extract":
            print(A.heapExtract())
        else:
            break

