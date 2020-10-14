from collections import deque


class HashTable:
    def __init__(self, length) -> None:
        self.__values = [deque() for _ in range(length)]
        self.__size = 0

    def hash(self, key) -> int:
        return hash(key) % len(self.__values)

    def size(self)->int:
        return self.__size

    def add(self, key):
        value = self.search(key)
        if value is False:
            hashedKey = self.hash(key)
            self.__values[hashedKey].append(key)
            self.__size += 1
        else:
            return value

    def remove(self, key) -> None:
        value = self.search(key)
        if value is not False:
            self.__values[self.hash(key)].remove(key)
            self.__size -= 1

    def search(self, key):
        return key in self.__values[self.hash(key)]

    def getPosition(self, key) -> (int, int):
        """returns pos in list and deque or (-1,-1) if not present"""
        value = self.search(key)
        if value is False:
            return (-1,-1)
        positionList = self.hash(key)
        positionDeque = 0
        for k in self.__values[positionList]:
            if k == key:
                return (positionList, positionDeque)
            else:
                positionDeque +=1

    def __str__(self) -> str:
        hashTable = ""
        for i in range(len(self.__values)):
            hashTable += str(i) + ": " + str(self.__values[i]) + "; \n"
        return hashTable
