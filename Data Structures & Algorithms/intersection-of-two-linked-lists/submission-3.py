# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#LL A = 4,1,8,4,5
#LL B = 5,6,1,8,4,5
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        listA = headA
        lenA = 0  
        listB = headB
        lenB = 0

        while(listA.next!=None):
            listA = listA.next
            lenA += 1

        while(listB.next!=None):
            listB = listB.next
            lenB += 1

        if(listA !=listB):
            return None

        listA = headA
        listB = headB
        startComp = 0

        if(lenA>lenB):
            startComp = lenA-lenB
            while(startComp>0):
                listA = listA.next
                startComp -=1
        else:
            startComp = lenB-lenA
            while(startComp>0):
                listB = listB.next
                startComp -=1

        while(listA!=None and listB!=None):
            if(listA == listB):
                return listA
            listA = listA.next
            listB = listB.next
