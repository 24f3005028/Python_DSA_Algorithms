"""
LINKED LIST
"""
"""
Implementing Node class
    Data Members: daqta and next
    Functions: constuctor __init__()
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""
Implementing Linked List class:
    Data Members: head 
    Functions: constructor __init__(), isEmpty(), append(), delete(), display()
"""

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def append(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next

            temp.next = Node(data)

    def delete(self, v):
        # List is Empty
        if self.isEmpty():
            return "List is empty"
        # Element is at head itself
        if self.head.data == v:
            self.head = self.head.next
            return 
        # element v is found somewhere in the list
        temp1 = self.head
        temp2 = self.head
        while temp1.next != None and temp1.data != v:
            temp2 = temp1
            temp1 = temp1.next

        if temp1.data == v:
            temp2.next = temp1.next
            return
        
        # If  element does exist
        if temp1.next == None:
            return "Doesn't Exist"
    
    def display(self):
        if self.isEmpty():
            return "List is Empty"
        temp = self.head
        while temp != None:
            print(temp.data, end=" =>")
            temp = temp.next

L = [5,3,8,5,2,9]
L1 = LinkedList()
for v in L:
    L1.append(v)
L1.display()
L1.delete(8)
L1.display()