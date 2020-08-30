# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #implement merge part of merge sort
        
        # Loop thru both lists at the same time, adding the lower of the two elements to the new linked list, and           only incrementing forward the side thats lower.
        
        
        
        #if the l1 has smaller val add it to the list as our fist element, otherwise add the the 1st val from l2
        if (l1 == None) !=  (l2== None):
            if l1:
                return l1
            else:
                return l2
        elif l1 and l2:
            if l1.val <= l2.val:
                new_list = ListNode(l1.val)
                #increment the linked list  so it doesnt get added twice
                l1 = l1.next
            else:
                new_list = ListNode(l2.val)
                #increment the linked list so it doesnt get added twice
                l2 = l2.next
        else:
            return 
        #set dummy head
        dummy = new_list
        #loop while there still elements in both lists
        while l1 and l2:
            
            if l1.val <= l2.val:
                #set the next element to be a listnode with l1.val
                new_list.next = ListNode(l1.val)
                #increment the new_list 
                new_list = new_list.next
                #increment l1
                l1 = l1.next
            else:
                #set the next element to be a listnode with l2.val
                new_list.next = ListNode(l2.val)
                #increment the new_list 
                new_list = new_list.next
                #increment l2
                l2 = l2.next
        #if the lists arnt equal, there are gonna be some unsorted things left. so we need to add those to our new list.
        if l1:
            while l1:
                new_list.next = ListNode(l1.val)
                #increment the new_list 
                new_list = new_list.next
                #increment l1
                l1 = l1.next
                
        elif l2:
            while l2:
                new_list.next = ListNode(l2.val)
                #increment the new_list 
                new_list = new_list.next
                #increment l2
                l2 = l2.next
        #return the dummy
        return dummy
            
            
                
        
