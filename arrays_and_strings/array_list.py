'''
Main idea of an array list:
+ Allocate space before hand so if user wants to expand the array, we don't need
to reallocate space as often.
+ The size of the array differs of the actual size of the list structure used
because we want to give the impression that the array is expanding.
_   array size: 1       actual size: 1
1   array size: 1       actual size: 1
1, _    array size: 1       actual size: 2
1, 5    array size: 2       actual size: 2
1, 5, _, _  array size: 2       actual size: 4
1, 5, 8, _  array size: 3       actual size: 4
1, 5, 8, 12, _, _, _, _     array size: 4       actual size: 8
1, 5, 8, 12, 7, 23, 65, _   array size:7        actual size: 8
'''

class ArrayList:
    def __init__(self, size=16):
        self.dataAr = [None] * size
        self.arSize = size

    def expand(self, factor=2):
        '''
            Hidden from user; if user want to allocate more space to array,
            use a different function.
        '''
        newAr = [None] * (self.arSize * factor)
        for idx in range(self.arSize):
            newAr[idx] = self.dataAr[idx]
        self.dataAr = newAr

    def add(self, data):
        if self.arSize >= len(self.dataAr):
            self.expand()
        self.dataAr[self.arSize] = data
        self.arSize += 1

    def get(self, idx):
        if not self.isValidIndex(idx):
            return None
        else:
            return self.dataAr[idx]

    def set(self, data, idx):
        # Change the value at positions where there's already a value
        if not self.isValidIndex(idx):
            return None
        else:
            oldData = self.dataAr[idx]
            self.dataAr[idx] = data
            return oldData

    def remove(self, idx):
        if not self.isValidIndex(idx):
            return None
        else:
            removedData = self.dataAr[idx]
            self.dataAr[idx] = None
            return removedData

    def isValidIndex(self, idx):
        if not isinstance(idx, int) or idx < 0:
            print("Invalid index value.")
            return False
        elif idx >= self.arSize:
            print("Index out of range.")
            return False
        else:
            return True

    def clear(self):
        self.dataAr = [None] * len(self.dataAr)

    def size(self):
        return self.arSize

    def printArray(self):
        print(self.dataAr[:self.arSize])

'''
1, 5, 8, 12, _, _, _, _         array size: 4       actual size: 8
1, 5, 8, 12, 7, 23, 65, _       array size: 7       actual size: 8
1, 5, 8, 12, 7, 23, 65, 11      array size: 8       actual size: 8
1, 5, 8, 12, 7, 23, 65, None    array size: 8       actual size: 8
'''

array = ArrayList(4)
array.printArray()
array.set(5, 1)
array.set(1, 0)
array.set(8, 2)
array.set(12, 3)
array.printArray()
array.set(7, 4)
array.add(7)
array.printArray()
print(array.size())
array.add(23)
array.add(65)
array.add(11)
array.printArray()
print(array.size())
array.get(10)
print(array.get(7))
array.remove(10)
array.remove(7)
array.printArray()
print(array.size())
array.add(77)
array.printArray()
print(array.size())
print(len(array.dataAr))
