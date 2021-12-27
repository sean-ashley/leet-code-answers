# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #first pass to get the length
        
        length = 0
        
        #get a dummy to traverse
        
        dummy = head
        
        while dummy:
            length += 1
            
            dummy = dummy.next
        #index until the node right before the one we want to remove
        idx = 0
        dummy2 = head
        while idx < length - n - 1:
            idx += 1
            head = head.next
            
        #special case 1, if we want to remove the first one, just return dummy2.next        
        if n == length:
            return dummy2.next
        #normal case, remove the wanted node
        elif head.next:
            head.next = head.next.next
        #otherwise, return none
        else:
            return None
        
        return dummy2
