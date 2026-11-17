class Node:
    def __init__(self, key:int = -1, value:int =-1, next:"Node" = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.primary = [Node() for _ in range(10000)]

    def find(self, key:int):
        previous = self.primary[key%10000]
        current = previous.next

        while current and current.key !=key:
            previous = current
            current = current.next

        return previous

    def put(self, key: int, value: int) -> None:
        prev = self.find(key)

        if prev.next:
            prev.next.value = value
        else:
            prev.next = Node(key, value)

    def get(self, key: int) -> int:
        prev = self.find(key)

        if prev.next:
            return prev.next.value
        
        else:
            return -1

    def remove(self, key: int) -> None:
        prev = self.find(key)

        if prev.next:
            prev.next = prev.next.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)