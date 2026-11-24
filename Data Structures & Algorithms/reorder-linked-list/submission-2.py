# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle
        slow = head
        fast = head

        if(head.next==None):
            return None

        while(fast.next!=None and fast.next.next!=None):
            slow = slow.next
            fast = fast.next.next

        #reverse the second half
        prev = None
        current = slow.next
        fast = slow.next.next
        #point the end of first half to None
        slow.next = None

        while(current!=None):
            current.next = prev
            prev = current
            current = fast
            if(fast!=None):
                fast = fast.next

        slow = head
        fast = prev
        #merge the list
        while(fast!=None):
            temp = slow.next
            slow.next = fast
            fast = fast.next
            slow.next.next = temp
            slow = temp



