class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return str(self.val)

array = [1,2,3,4,5]
for item in array:
    ITEM = ListNode(item)

    
curr = Head

def display(head):
    curr = head
    elements = []
    
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    
    print((" -> ").join(elements))
    
display(Head)
        


