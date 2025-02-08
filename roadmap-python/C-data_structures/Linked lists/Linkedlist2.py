class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        # if LL is empty, new_node will become first in LL
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def insert_at_begin(self, data):
        # create a new node
        new_node = Node(data)
        # new_node next will be the head 
        new_node.next = self.head
        # the head now will be the new node
        self.head = new_node
    
    def insert_after(self, data, prev_node):
        if not prev_node:
            print("Node must be in linked list.")
            return
        new_node = Node(data)
        
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
    # traverse         
    def display(self):
        current = self.head
        while current:
            print(current.data, end = " - > ")
            current = current.next
        print("None")
        
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(4)
llist.append(5)
llist.insert_at_begin(5)
llist.insertion_after(9, 3)
llist.reverse()
llist.display()            
