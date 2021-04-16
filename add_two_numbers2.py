# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        
        #and create first number
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        
        #create second number
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        

      
        #convert them to integers and add them
        
        sum_num = str(int(num1) + int(num2))
        
        #convert it back to a string
        sum_ll = ListNode(val = int(sum_num[0]))
        
        #store a dummy head
        dummy = sum_ll
        #capture edge case where sum is one digit long
        if len(sum_num) == 1:
            return sum_ll
        
        #loop thru sum_num started at the second letter(if it exists)
        for i in sum_num[1:]:
            sum_ll.next = ListNode(val = int(i))
            
            sum_ll = sum_ll.next
            
        #return the dummy
        
        return dummy
        
