from src.HashTable import HashTable


class SymbolTable:
    def __init__(self, size):
        self.__hashTable = HashTable(size)

    def add(self, key):
        self.__hashTable.add(key)

    def size(self):
        return self.__hashTable.size()

    def search(self, key):
        return self.__hashTable.search(key)

    def remove(self, key):
        return self.__hashTable.remove(key)

    def getPosition(self, key) -> (int, int):
        return self.__hashTable.getPosition(key)

    def __str__(self) -> str:
        return str(self.__hashTable)