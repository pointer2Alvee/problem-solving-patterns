# Q: Detect Cycle in a LL 
def has_cycle(head):
    slow = fast = head
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False