class DoublyNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return str(self.val)
    

head = tail = DoublyNode(1)
# print(head)
# print(tail)

# display - O(n)
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(" <-> ".join(elements))

# display(head)

# Insert at the beggining - O(1)
def insert_at_beginnig(head, tail, val):
    new_node = DoublyNode(val, next=head)
    head.prev = new_node
    
    return new_node, tail

head, tail = insert_at_beginnig(head, tail, 3)
display(head)

# Insert at the end - O(1)
def insert_at_end(head, tail, val):
    new_node = DoublyNode(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display(head)