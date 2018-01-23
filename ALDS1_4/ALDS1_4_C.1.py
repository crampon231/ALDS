# -*- coding: utf-8 -*-

class HashTable(dict):
    def __init__(self, length):
        dict.__init__(self)
        self.length = length
        #self[:] = [None] * length

    def h1(self, key):
        return key % self.length

    def h2(self, key):
        return 1 + (key % (self.length - 1))

    def h(self, key, i):
        return (self.h1(key) + i*self.h2(key)) % self.length

    def insert(self, key):
        i = 0
        while True:
            j = self.h(key, i)
            if self[j] is None:
                self[j] = key
                return j
            else:
                i += 1
    
    def search(self, key):
        i = 0
        while True:
            j = self.h(key, i)
            if self[j] == key:
                return j
            elif self[j] is None or i >= self.length:
                return None
            else:
                i += 1

def getNum(char):
    char2num = str.maketrans("ACGT", "1234")
    return int(char.translate(char2num))

if __name__ == '__main__':

    n = int(input())
    T = HashTable(n)
    C = [input().split(" ") for i in range(n)]
    C = map(lambda x:(x[0], getNum(x[1])), C)
    
    for command, num in C:
        if command == "insert":
            T.insert(num)
        else:
            if T.search(num) is None:
                print("no")
            else:
                print("yes")
