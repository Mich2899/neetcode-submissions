class LRUDLL:
    def __init__(self):
        self.key = -1
        self.val = -1
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.lruHash = {}
        self.dummy = LRUDLL()
        self.MRU = None
        self.LRU = None
        self.maxSize = capacity       

    def get(self, key: int) -> int:
        if key in self.lruHash:
            node = self.lruHash[key]

            # Only move node if there are >1 items AND it isn't already MRU
            if(self.LRU!=self.MRU and node!=self.MRU):
                # 1. If it was the LRU, advance LRU first
                if(node == self.LRU):
                    self.LRU = node.next

                # 2. Unlink node from its current position
                node.prev.next = node.next
                if(node.next!=None):
                    node.next.prev = node.prev

                # 3. Attach node after current MRU
                node.next = self.MRU.next
                self.MRU.next = node
                node.prev = self.MRU
                self.MRU = node

            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.lruHash:
            node = self.lruHash[key]
            node.val = value
            node.key = key
            
            if(self.LRU != self.MRU and node!=self.MRU):
                if (node == self.LRU):
                    #Advance LRU to next node
                    self.LRU = node.next

                #detach from the current position
                node.prev.next = node.next # LRU
                if(node.next!=None):
                    node.next.prev = node.prev

                #Attach to tail
                node.next = self.MRU.next
                self.MRU.next = node
                node.prev = self.MRU
                self.MRU = node

        else:

            if (self.size==0):
                newNode = LRUDLL()
                newNode.val = value
                newNode.key = key
                newNode.prev = self.dummy
                newNode.next = self.dummy.next
                self.dummy.next = newNode
                self.MRU = newNode
                self.LRU = newNode
                
                self.lruHash[key] = newNode
                self.size += 1
            
            elif (self.size==self.maxSize):

                if(self.LRU==self.MRU):
                    #Find the key related to LRU node and delete it from Hash Map                 
                    if self.LRU.key in self.lruHash:
                        del self.lruHash[self.LRU.key]

                    newNode = LRUDLL()
                    newNode.val = value
                    newNode.key = key
                    self.lruHash[key] = newNode

                    self.dummy.next = newNode
                    newNode.next = None
                    newNode.prev = self.dummy

                    self.LRU = newNode
                    self.MRU = newNode                    

                else:

                    #Find the key related to LRU node and delete it from Hash Map                 
                    if self.LRU.key in self.lruHash:
                        del self.lruHash[self.LRU.key]

                    newNode = LRUDLL()
                    newNode.val = value
                    newNode.key = key

                    self.lruHash[key] = newNode

                    if(self.LRU.next !=None):
                        self.LRU.next.prev = self.LRU.prev
                    self.LRU.prev.next = self.LRU.next
                    self.LRU = self.LRU.next
                    
                    newNode.next = self.MRU.next
                    self.MRU.next = newNode
                    newNode.prev = self.MRU

                    self.MRU = newNode
                

            else:
                newNode = LRUDLL()
                newNode.val = value
                newNode.key = key

                #Add the new key in hash map
                self.lruHash[key] = newNode

                newNode.next = self.MRU.next
                self.MRU.next = newNode
                newNode.prev = self.MRU

                self.MRU = newNode
                self.size += 1




            