# -*- coding: utf-8 -*-

class HashTable(list):
    def __init__(self, length):
        list.__init__(self)
        self.length = length
        self[:] = [None] * length

    def h(self, key, i):
        h1 = key % self.length
        h2 = 1 + (key % (self.length - 1))
        return (h1 + i*h2) % self.length

    def insert(self, key):
        i = 0
        while True:
            h1 = key % self.length
            h2 = 1 + (key % (self.length - 1))
            j = (h1 + i*h2) % self.length
            #j = self.h(key, i) # slow...
            if self[j] is None:
                self[j] = key
                return j
            else:
                i += 1
    
    def search(self, key):
        i = 0
        while True:
            h1 = key % self.length
            h2 = 1 + (key % (self.length - 1))
            j = (h1 + i*h2) % self.length
            #j = self.h(key, i) # slow...
            if self[j] == key:
                return j
            elif self[j] is None or i >= self.length:
                return None
            else:
                i += 1

def getNum(char):
    char2num = str.maketrans("ACGT", "1234")
    return int(char.translate(char2num), 5)

if __name__ == '__main__':

    n = int(input())
    T = HashTable(1046527)
    C = [input().split(" ") for i in range(n)]
    
    for command, char in C:
        num = getNum(char)
        if command[0] == "i":
            T.insert(num)
        else:
            if T.search(num) is None:
                print("no")
            else:
                print("yes")