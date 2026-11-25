class MyCircularQueue:
        def __init__(self, k: int):
            self.size = k
            self.head = 0
            self.tail = 0
            self.myCirQ = [-1]*self.size

        def Front(self)->int:
            return self.myCirQ[self.head]

        def Rear(self)->int:
            if(self.tail==0):
                return self.myCirQ[self.size - 1]
            else:
                return self.myCirQ[self.tail-1]

        def enQueue(self, value: int)->bool:
            #check if queue is full
            if(self.isFull()):
                return False
            elif(self.tail == (self.size-1)):
                self.myCirQ[self.tail] = value
                self.tail=0
                return True
            else:
                self.myCirQ[self.tail] = value
                self.tail+=1
                return True
        
        def deQueue(self)->bool:
            if(self.myCirQ[self.head]!=-1):
                self.myCirQ[self.head]=-1
                if(self.head+1 == (self.size)):
                    self.head = 0
                else:
                    self.head+=1
                return True
            else:
                return False

        def isEmpty(self)->bool:
            if(self.head==self.tail and (self.myCirQ[self.head]==-1)):
                return True
            
            return False

        def isFull(self)->bool:
            if((self.tail+1) == self.head) and (self.myCirQ[self.tail]!=-1):
                return True
            elif((self.tail==self.head) and self.myCirQ[self.tail]!=-1):
                return True
            else:
                return False

# class MyCircularQueue:

#     def __init__(self, k: int):
        

#     def enQueue(self, value: int) -> bool:
        

#     def deQueue(self) -> bool:
        

#     def Front(self) -> int:
        

#     def Rear(self) -> int:
        

#     def isEmpty(self) -> bool:
        

#     def isFull(self) -> bool:
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()