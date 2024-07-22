class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    



class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertAtbegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtIndex(self, data: int, index: int ):
        if index == 0:
            self.insertAtBegin(data)
            return
        
        position = 0
        curr = self.head
        while curr is not None and position < index - 1:
            position += 1
            curr = curr.next

        if curr is not None:
            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node
        else:
            print("Index not present")

    def inseratend(self, data: int):

        new_node = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = new_node
        



    def printAll(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

LL = LinkedList()
LL.insertAtbegin(1)
LL.insertAtbegin(2)
LL.insertAtbegin(3)
LL.insertAtIndex(4, 1)
LL.inseratend(5)
LL.printAll()
