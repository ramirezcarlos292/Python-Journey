class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        # if linked list is empty add incoming new_node
        # to be the head of the linked list 
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        # iterate over the linked list to append new_node
        # to the last of the linked list
        while last.next:
            last = last.next
        last.next = new_node
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")
        
        
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

llist.display()