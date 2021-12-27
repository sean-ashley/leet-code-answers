# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #set up two dummies, fast and slow
        
        fast_dummy = head
        slow_dummy = head
        
        #run fast dummy n times
        for i in range(n):
            fast_dummy = fast_dummy.next
            
            
        #special case, if we are asked to remove the first element, just return head.next
        #we will know it is the first element if slow dummy is equal to head
        if not fast_dummy:
            return head.next
        #now start the slow dummy, the distance between these two dummies will be n, so once
        #fast dummy has reached the end, slow dummy will be n away from the end.
        
        #we actually want 1 before the nth node from the end so we can actually remove the nth node
        #this is why we are checking if fast_dummy.next exists
        while fast_dummy.next:
            
            fast_dummy = fast_dummy.next
            slow_dummy = slow_dummy.next

      
        slow_dummy.next = slow_dummy.next.next
    

        return head
