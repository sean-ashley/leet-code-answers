# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #create two empty strings for both linked lists to accumulate
        lst1 = ""
        lst2= ""
        
        #accumulate both numbers by concatenating them as strings
        
        #accumulate lst1
        pointer = l1
        while pointer != None:
            lst1 += str(pointer.val)
            pointer = pointer.next
        #accumulate lst2
        pointer = l2
        
        while pointer != None:
            lst2 += str(pointer.val)
            pointer = pointer.next
        
        #reverse lst1 and lst2 using string slicing
        
        lst1 = lst1[-1::-1]
        lst2 = lst2[-1::-1]
        #add both numbers
        new_lst = int(lst1) + int(lst2)
        
        #reverse new list
        new_lst = str(new_lst)[-1::-1]
        
        #iterate thru new list, creating a new linked list
        
        #setup dummy head
        dummy_head = ListNode(val = int(new_lst[0]))
        for i in range(len(new_lst)):
            #if its the first item in the list, dont worry about setting it next to anything yet
            if i == 0:
                head = dummy_head
            else:
                node = ListNode(val = int(new_lst[i]))
                head.next = node
                head = node
            
        return dummy_head
                