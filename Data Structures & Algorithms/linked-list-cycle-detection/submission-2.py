# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #if the cycle exists in the linked list
        slow = head
        fast = head

        while(slow!=None and fast!=None):
            if((fast.next==None) or (fast.next.next==None)):
                return False
            else:
                slow = slow.next
                fast = fast.next.next

            if(slow==fast):
                return True

        return False        