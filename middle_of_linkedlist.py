# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        length_of_ll = 0
        
        dummy1 = head
        
        while dummy1:
            length_of_ll += 1
            dummy1 = dummy1.next
            
        
        middle_idx = (length_of_ll // 2)  +1
        
        idx = 1
        
        while idx != middle_idx:
            head = head.next
            idx +=1
            
        
        return head
