class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr != None and curr.next!=None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
