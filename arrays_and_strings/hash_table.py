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
        if not self.isValidSize(size):
            raise ValueError("Invalid size value! Should be an integer greater than 0.")
        self.table = [None] * size
        for i in range(size):
            self.table[i] = SinglyLinkedList()
        self.size = size

    def isValidSize(self, size):
        return isinstance(size, int) and size > 0

    def hash(self, key):
        '''
            Hash a given key and return the corresponding index in the table.
        '''
        if isinstance(key, str):
            return self.hashStr(key) % self.size
        elif isinstance(key, int):
            return self.hashInt(key) % self.size
        elif isinstance(key, float):
            return self.hashFloat(key) % self.size
        else:
            raise TypeError("Invalid key type!")

    def hashStr(self, key):
        # Inspired by Python's string_hash function
        hashVal = 0
        bitShiftAmount = 7
        multNum = 18
        for chr in key:
            hashVal = (hashVal * multNum) ^ (ord(chr) << bitShiftAmount)
        hashVal = hashVal ^ len(key)
        return hashVal

    def hashInt(self, key):
        bitShiftAmount = 4
        bitXorAmount = 62982
        multNum = 27
        return ((key ^ bitXorAmount) * multNum) << bitShiftAmount

    def hashFloat(self, key):
        bitShiftAmount = 8
        bitXorAmount = 53671
        multNum = 72
        divNum = 714
        return (int(key * multNum / divNum) << bitShiftAmount) ^ bitXorAmount

    def insert(self, key, value):
        hashIdx = self.hash(key)
        newKeyVal = KeyValuePair(key, value)
        list = self.table[hashIdx]
        if list.search(newKeyVal) == None:
            list.insert(newKeyVal)
        else:
            raise ValueError("Key already exists in table!")

    def delete(self, key):
        pass

    def search(self, key):
        pass

    def update(self, key, newVal):
        pass

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
'''
kvpair = KeyValuePair("apple", 204)
print(str(kvpair))
'''
