# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = ""
        num2 = ""
        
        #create num1
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
            
        
        #reverse it
        num1 = num1[::-1]
        
        #create num2
                
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
            
        
        #reverse it
        num2 = num2[::-1]
        
        #convert them to ints and and the numbers, and then reverse taht number
        
        num3 = str((int(num1) + int(num2)))[::-1]
        
        #loop thru tht number and create our new linkedlist
        
        #instantiate our linked list and a dummy head
        l3 = ListNode(val = int(num3[0]))
        dummy = l3
        
        for i in range(1,len(num3)):
            
            l3.next = ListNode(val = int(num3[i]))
            
            l3 = l3.next
        
        return dummy
