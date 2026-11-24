# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if(head.next == None):
            return True

        # loop through the LL to find the length
        length = 0
        slow = head
        
        while(slow!=None):
            slow = slow.next
            length+=1

        #find the middle
        slow = head
        fast = head

        while(fast.next!=None and fast.next.next!=None):
            slow = slow.next
            fast = fast.next.next

        #reverse the second half
        prev = None
        current = slow.next
        fast = slow.next.next

        while(current!=None):
            current.next = prev
            prev = current
            current = fast
            if(fast!=None):
                fast=fast.next

        slow.next = None

        #compare both the halves
        slow = head
        fast = prev
        counter = 0

        while(fast!=None):
            if(slow.val==fast.val):
                counter+=1
            slow = slow.next
            fast = fast.next

        if(counter==length//2):
            return True
        else:
            return False


