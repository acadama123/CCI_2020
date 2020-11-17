'''
1. Listen
2. Example
3. Brute force
4. Optimize
5. Walk through
    Did not walk through the functions in SinglyLinkedList
6. Implement
7. Test
'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

    def getData(self):
        return self.data

    def getNextNode(self):
        return self.next_node

    def setNextNode(self, next_node):
        if isinstance(next_node, Node) or next_node == None:
            self.next_node = next_node
        else:
            print("Invalid input node.")

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def insert(self, data, pos=0):
        '''
            If pos > self.size, this function will insert the data to the end of
            the linked list.
        '''
        if not isinstance(pos, int) or pos < 0:
            print("Invalid position value.")
            return

        if pos == 0:
            oldHead = self.head
            self.head = Node(data)
            self.head.setNextNode(oldHead)
        else:
            curPos = 0
            curNode = self.head
            prevNode = None
            while curPos != pos:
                prevNode = curNode
                curNode = curNode.getNextNode()
                curPos += 1
                if curPos == self.size:
                    break
            newNode = Node(data)
            newNode.setNextNode(curNode)
            prevNode.setNextNode(newNode)
        self.size += 1

    def delete(self, pos):
        if not isinstance(pos, int) or pos < 0 or pos > (self.size - 1):
            print("Invalid position value.")
            return

        if pos == 0:
            newHead = self.head.getNextNode()
            targetNode = self.head
            self.head = newHead
        else:
            curPos = 0
            curNode = self.head
            prevNode = None
            while curPos != pos:
                prevNode = curNode
                curNode = curNode.getNextNode()
                curPos += 1
            targetNode = curNode
            prevNode.setNextNode(curNode.getNextNode())
        self.size -= 1
        return targetNode.getData()

    def search(self, data, getLoc=False):
        curPos = 0
        curNode = self.head
        while curPos < self.size:
            if curNode.getData() == data:
                if getLoc:
                    return (curNode, curPos)
                else:
                    return curNode
            curNode = curNode.getNextNode()
            curPos += 1
        return None

    def printList(self):
        curNode = self.head
        listStr = ""
        while curNode != None:
            listStr = listStr + str(curNode.getData())
            nextNode = curNode.getNextNode()
            if nextNode != None:
                listStr = listStr + " -> "
            curNode = nextNode
        print(listStr)
'''
# 2 -> 5 -> 9 -> -3 -> 12
list = SinglyLinkedList()
list.insert(9,0)
list.printList()
list.insert(12,3)
list.printList()
list.insert(3,1)
list.printList()
list.insert(2,0)
list.printList()
list.insert(5,1)
list.printList()
print(list.search(9))
print(list.search(5))
print(list.search(3))
print(list.search(12))
print(list.search(2))
print(list.search(20))
print(list.delete(4))
list.printList()
print(list.delete(3))
list.printList()
print(list.delete(1))
list.printList()
print(list.delete(0))
list.printList()
print(list.delete(0))
list.printList()
'''
