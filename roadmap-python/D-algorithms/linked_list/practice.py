class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        print(" -> ".join(map(str, nodes)))
    
    def reverse(self):
        prev, current = None, self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
    def insert_beggining(self, data):
        # append to the beginning
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # search
    
    # remove, first, last or specific item

arry = [5,6,8,9,7,4,5,24,6]
linked_list = LinkedList()

for item in arry:
    linked_list.insert(item)
linked_list.display()
linked_list.reverse()
linked_list.display()
linked_list.insert_beggining(0)
linked_list.display()