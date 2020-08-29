# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #initialize these variables, prev will start at None since thats the last node in the list
        #curr is head because we are going to sdtart at the had of the list
        prev = None
        curr = head
        while curr:
            #store the node after head
            temp = curr.next
            #change the head next node to the previous node (equivalent to swapping index -1 with 1)
            curr.next = prev
            #previous node becomes the current node as we are reversing the list
            prev = curr
            #the head becomes the head.next
            curr = temp
        return prev
        
        
        
