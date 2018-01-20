# -*- coding: utf-8 -*-


class RingBuffer(list):
    def __init__(self, MAX):
        list.__init__(self)
        self.head = 0
        self.tail = 0
        self.MAX = MAX
        self[:] = [None] * MAX

    def isEmpty(self):
        return self.head == self.tail

    def enque(self, x):
        self[self.tail] = x
        if self.tail + 1 == self.MAX:
            self.tail = 0
        else:
            self.tail += 1

    def deque(self):
        x = self[self.head]
        if self.head + 1 == self.MAX:
            self.head = 0
        else:
            self.head += 1
        return x


if __name__ == '__main__':

    n, q = [int(c) for c in input().split(" ")]
    P = RingBuffer(n + 1)

    for i in range(n):
        P_name, P_time = input().split(" ")
        P.enque([P_name, int(P_time)])

    time = 0
    while not P.isEmpty():
        P_name, P_time = P.deque()

        if P_time > q:
            time = time + q
            P_time = P_time - q
            P.enque([P_name, P_time])
        else:
            time = time + P_time
            print(P_name, time)
