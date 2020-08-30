
  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #implement merge part of merge sort
        
        # Loop thru both lists at the same time, adding the lower of the two elements to the new linked list, and           only incrementing forward the side thats lower.
        
        #create empty new list
        new_list = ListNode()
        #create dummy head to return at the end
        dummy = new_list
        #loop while there still elements in both lists
        while l1 and l2:
            if l1.val <= l2.val:
                #set the next element to be  l1
                new_list.next = l1
                #increment l1
                l1 = l1.next
            else:
                #set the next element to be a listnode with l2.val
                new_list.next = l2
                #increment l2
                l2 = l2.next
            #increment the new_list
            new_list = new_list.next
        #if the lists arnt equal, there are gonna be some unsorted things left. so we need to add those to our new list.
        new_list.next = l1 or l2
        return dummy.next
            
            
                


                
        
