# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev  -> NULL
        # current -> current node pointer
        # nex -> next node pointer

        if(head == None):
            return None

        prev = None
        current = head
        nex = head.next

        while(nex!=None):
            current.next = prev
            prev = current
            current = nex 
            nex = nex.next

        current.next = prev
        return current