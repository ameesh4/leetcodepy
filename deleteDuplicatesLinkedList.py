class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        if head.next == None:
            return head
        
        while head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next