class MyHashSet:

    def __init__(self):
        self.primary = [None]*1000              

    def add(self, key: int) -> None:
        p_index = key % 1000
        if self.primary[p_index] is None:
            if p_index == 0:
                self.primary[p_index] = [False]*1001
            else:
                self.primary[p_index] = [False]*1000

        s_index = key // 1000
        self.primary[p_index][s_index] = True
        return

    def remove(self, key: int) -> None:
        p_index = key % 1000
        s_index = key // 1000

        if self.primary[p_index] is not None:
           self.primary[p_index][s_index] = False 
        return

    def contains(self, key: int) -> bool:
        p_index = key % 1000
        s_index = key // 1000        
        
        if self.primary[p_index] is not None:
            if self.primary[p_index][s_index] == True :
                return True
            else :
                return False
        else :
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)