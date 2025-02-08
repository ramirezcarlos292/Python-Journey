class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self, data):
        new_node = Node(data)
        # check if list is empty
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
            
    def reverse(self):
        prev, current = None, self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        print(" -> ".join(map(str, nodes)))

class Solution:
    ## populate the linked list
    def reverseList(array): 
        linked_list = LinkedList()
        for item in array:
            linked_list.insert(item)
        linked_list.display()
        
        linked_list.reverse()
        linked_list.display()
                
        
      
    
        
Solution.reverseList([1,2,3,4,5])
