# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #create hash_table to keep track of nodes visited
        hash_table = set()
        #go till the end of the list (if it exists)
        while head:
            #if the node is in the hash_table, return true
            if head in hash_table:
                return True
            #other wise add it , and keep on going
            hash_table.add(head)
            head = head.next
        #if the list has an end, return false
        return False
            
        
        
