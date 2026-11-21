# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow = head
        sizeLL = 0

        if(head.next==None):
            return None

        while(slow!=None):
            slow = slow.next
            sizeLL += 1

        nodeBfr = sizeLL - n
        slow = head
        while(nodeBfr>1):
            slow = slow.next
            nodeBfr-=1

        if(nodeBfr==0):
            head=head.next
        
        slow.next = slow.next.next
        return head