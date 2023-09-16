https://app.codesignal.com/interview-practice/question/5vcioHMkhGqkaQQYt/description
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, n):
    
    if n == 0:
        return l
    slow,fast = l,l
    
    for i in range(n+1):
        if fast:
            fast = fast.next
        else:
            return l
    
    #now move up the slow pointer and fast pointer at the same rate, this will position
    #the slow pointer n from the back
    while fast:
        fast = fast.next
        slow = slow.next 
    
    second_part = slow.next 
    
    #detach lists
    slow.next = None
    
    #iterate till last node
    dummy = second_part 
    while second_part.next:
        second_part = second_part.next
    
    #attach end to start of the list
    second_part.next = l 
    
    
    return dummy
