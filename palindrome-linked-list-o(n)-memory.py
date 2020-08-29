# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        lst = []
        
        while head:
            #append the current node to the list
            lst.append(head.val)
            #go to the next node
            head = head.next
        
        #see if the list is the same forwards and backwards
        
        return lst == lst[::-1]
        
