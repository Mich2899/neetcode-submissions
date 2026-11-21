# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        dummy = ListNode(0, next=head)
        slow = dummy
        fast = dummy
        count = 0 

        if(head.next == None):
            return None

        while(count<=n):
            fast = fast.next;
            count+= 1

        while(fast!=None):
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        head = dummy.next

        return head
