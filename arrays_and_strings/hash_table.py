from singly_linked_list import Node, SinglyLinkedList

class KeyValuePair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return str(self.key) + ": " + str(self.value)

class HashTable:
    def __init__(self, size=16):
        if not self._isValidSize(size):
            raise ValueError("Invalid size value! Should be an integer greater than 0.")
        self.table = [SinglyLinkedList() for __ in range(size)]
        self.size = size

    def _isValidSize(self, size):
        return isinstance(size, int) and size > 0

    def _hash(self, key):
        '''
            Hash a given key and return the corresponding index in the table.
            Todo: Figure out why hash function always return the same value.
        '''
        if isinstance(key, str):
            return self._hashStr(key) % self.size
        elif isinstance(key, int):
            return self._hashInt(key) % self.size
        elif isinstance(key, float):
            return self._hashFloat(key) % self.size
        else:
            raise TypeError("Invalid key type!")

    def _hashStr(self, key):
        # Inspired by Python's string_hash function
        hashVal = 0
        bitShiftAmount = 7
        multNum = 18
        for chr in key:
            hashVal = (hashVal * multNum) ^ (ord(chr) << bitShiftAmount)
        hashVal = hashVal ^ len(key)
        return hashVal

    def _hashInt(self, key):
        bitShiftAmount = 4
        bitXorAmount = 62982
        multNum = 27
        return ((key ^ bitXorAmount) * multNum) << bitShiftAmount

    def _hashFloat(self, key):
        bitShiftAmount = 8
        bitXorAmount = 53671
        multNum = 72
        divNum = 714
        return (int(key * multNum / divNum) << bitShiftAmount) ^ bitXorAmount

    def insert(self, key, value):
        hashIdx = self._hash(key)
        newKeyVal = KeyValuePair(key, value)
        list = self.table[hashIdx]
        if list.search(newKeyVal) is not None:
            print(f"Key {key} already exists in table.")
        else:
            list.insert(newKeyVal)

    def search(self, key, getLoc=False):
        hashIdx = self._hash(key)
        list = self.table[hashIdx]
        targetKeyVal = KeyValuePair(key, None) # Utilize KeyValuePair's __eq__
        searchResult = list.search(targetKeyVal, getLoc=True)
        if searchResult is None:
            print(f"Did not find the key: {key}.")
            return None
        if getLoc:
            pos = searchResult[1]
            return (hashIdx, pos)
        else:
            foundKeyVal = searchResult[0]
            return foundKeyVal

    def delete(self, key):
        searchResult = self.search(key, getLoc=True)
        if searchResult is None:
            return None
        hashIdx, pos = searchResult
        list = self.table[hashIdx]
        return list.delete(pos)

    def update(self, key, newVal):
        searchResult = self.search(key, getLoc=True)
        if searchResult is None:
            return None
        newKeyVal = KeyValuePair(key, newVal)
        hashIdx, pos = searchResult
        list = self.table[hashIdx]
        list.delete(pos)
        list.insert(newKeyVal, pos)

    def printTable(self):
        for idx in range(self.size):
            print(str(idx) + "| ", end="")
            self.table[idx].printList()

    def rehash(self):
        pass

    def expand(self, size):
        pass

table = HashTable()
table.insert("apple", 204)
table.insert(239, "Orange")
table.insert(3921, ["Hash", "Function", "Is", "Difficult", "To", "Create", 420])
table.printTable()
print(table.search(3921))
print(table.delete(3921))
table.printTable()
table.delete(22)
table.insert(239, 11)
table.update(239, 11)
table.printTable()
'''
kvpair = KeyValuePair("apple", 204)
print(str(kvpair))
'''
