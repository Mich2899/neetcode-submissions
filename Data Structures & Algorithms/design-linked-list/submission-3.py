class Node:

    def __init__(self):
        self.val = -1
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.track = 0

    def get(self, index: int) -> int:
        if(index<0 or index>(self.track-1)):
            return -1

        count = 0
        current = self.head

        while(count!=index):
            current = current.next
            count += 1
        
        return current.val

    def addAtHead(self, val: int) -> None:
        newHead = Node()
        newHead.val = val
        current = self.head

        if (current.val == -1):
            self.head = newHead
        else:
            newHead.next = current
            self.head = newHead
        self.track += 1

    def addAtTail(self, val: int) -> None:
        newTail = Node()
        newTail.val = val
        newTail.next = None
        current = self.head
        while(current.next!=None):
            current = current.next

        current.next = newTail
        self.track += 1

    def addAtIndex(self, index: int, val: int) -> None:
        newIndex = Node()
        newIndex.val = val
        count = 0 
        current = self.head
        while(count!=index-1):
            current = current.next
            count+=1

        newIndex.next = current.next
        current.next = newIndex
        self.track += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if(index<0 or index>(self.track-1)):
            return

        count = 0
        current = self.head

        while(count!= index-1):
            current = current.next
            count+=1

        current.next = current.next.next    
        self.track -=1    


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)