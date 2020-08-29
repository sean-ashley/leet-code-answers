# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #set slow and fast to head
        slow = head
        fast = head
        #while both fast and fast.next are not none
        while fast and fast.next:
            #iterate slow by 1
            slow = slow.next
            #iterate fast by 2
            fast = fast.next.next
            #if slow and fast are the same, its true (since the hare caught up to the tortoise)
            if slow == fast:
                return True
        #otherwise if we reached the end of the lsit its false
         
        return False
