class SinglyNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)
    
# Append items into singly linked list 
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

# print(Head)
 
curr = Head

# traverse a linked list - O(n)
def traverse(curr):
    while curr:
        print(curr)
        curr = curr.next
# traverse(curr)


# Fancy display linked list - O(n), while traversing
def traverse_display(head):   
    curr = head
    elements = []
    ## traverse
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print((" -> ").join(elements))
traverse_display(Head)

# Search an item in a linked list
def search(head, val):
    curr = head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    
    return False
## Append operations
# append to the beginning


# append to the end


# append between

## Remvoe operations
# remove

print(search(Head, 3))