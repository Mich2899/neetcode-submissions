# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # prev  -> NULL
        # current -> current node pointer
        # leftPoint1 -> leftPointer-1
        # nex -> next node pointer
        
        if(head == None):
            return None

        current = head
        nex = head.next
        countLeft = 1
        rightPointer = head
        leftPoint1 = head

        while(countLeft<left):
            leftPoint1 = current
            current = current.next
            nex = nex.next
            countLeft += 1
        
        countRight = 1
        while(countRight<=right):
            rightPointer = rightPointer.next
            countRight += 1

        prev = rightPointer
        counter=0
        while(counter<=(right-left)):
            counter += 1
            current.next = prev
            prev = current
            current = nex
            if nex!=rightPointer: 
                nex = nex.next

        if leftPoint1 == head and left==1:
            return prev
        
        leftPoint1.next = prev

        return head       