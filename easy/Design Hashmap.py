class MyHashMap:

    def __init__(self):
        self.map = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key] if self.map[key] != None else -1
    
    def remove(self, key: int) -> None:
        self.map[key] = None

"""
class ListNode:
    def __init__(self, key=-1, val=-1,next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = ListNode()

    def put(self, key: int, value: int) -> None:
        curr = self.map
        lastNode = curr
        have = False
        while curr != None:
            if curr.key == key:
                curr.val = value
                have = True

            lastNode = curr
            curr = curr.next
        
        if not have:
            lastNode.next = ListNode(key, value)

    def get(self, key: int) -> int:
        curr = self.map
        while curr != None:
            if curr.key == key:
                return curr.val
        
            curr = curr.next

        return -1

    def remove(self, key: int) -> None:
        curr = self.map
        prev = curr

        while curr != None:
            if curr.key == key and prev == curr:
                self.map = self.map.next
                break
            elif curr.key == key:
                if curr.next == None:
                    prev.next = None

                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
"""

"""
class MyHashMap:

    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        have = False
        for i in self.hashMap:
            if key == i[0]:
                have = True
                i[1] = value
        
        if not have:
            self.hashMap.append([key, value])

    def get(self, key: int) -> int:
        for i in self.hashMap:
            if i[0] == key:
                return i[1]
        
        return -1

    def remove(self, key: int) -> None:
        for i in self.hashMap:
            if i[0] == key:
                self.hashMap.remove(i)
"""

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)