class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self) -> None:
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    
    def print_linkedlist(self):
        temp = self.head
        while(temp):
            print(temp.data, end='')
            temp = temp.next

    def reverse(self):
        prev = None
        current = self.head
        while (current):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    def insert_at_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertatindex(self, data, index):
        if index == 0:
            self.insert_at_begin(data)
        else:

            position = 0
            current_node = self.head

            while (current_node != None and position+1 != index):
                current_node = current_node.next
                position += 1
            if current_node != None:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def insertAtend(self, data) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = new_node

            
    def updateNode(self, data, index):
        current_node = self.head
        position = 0 
        if index == 0:
            current_node.data = data
        else:

            while(current_node != None and position  != index):
                current_node = current_node.next
                position += 1
            if current_node != None:
                current_node.data = data
            else:
                print("index Not present")
    
    def remove_first_node(self):
        if(self.head) == None:
            return
        self.head = self.head.next

    def remove_last_node(self):
        if (self.head == None):
            return

        current_node = self.head
        while(current_node.next != None and current_node.next.next != None):
            current_node = current_node.next
        
        current_node.next = None

    def remove_at_index(self, index):
        
        if (self.head) == None:
            return
        position = 0 
        current_node = self.head
        while(current_node.next != None and position+1 != index):
            current_node = current_node.next
            position+=1
        
        if current_node!= None:
            current_node.next = current_node.next.next
        else:
            print("Index Not present")

    def remove_node(self, data):
        current_node = self.head

        if (current_node.data == data):
            self.remove_first_node()
            return
        else:
            while current_node != None and current_node.next.data != data:
                current_node = current_node.next
            if current_node == None:
                return 
            else:
                current_node.next = current_node.next.next

    def size_of_LL(self):
        size = 0 
        if(self.head):
            current_node = self.head
            while(current_node):
                current_node = current_node.next
                size+=1
            print(size)

        else:
            print(0)


linkedlist = LinkedList()
linkedlist.push(2)
linkedlist.push(3)

linkedlist.push(4)

linkedlist.print_linkedlist()

print("Insert at begin")
linkedlist.insert_at_begin(5)
linkedlist.print_linkedlist()


print("Insert")
linkedlist.insertatindex(6, 2)
linkedlist.print_linkedlist()

print("Insert at index")
linkedlist.insertAtend(7)
linkedlist.print_linkedlist()

print("Update node")
linkedlist.updateNode(8, 2)
linkedlist.print_linkedlist()




