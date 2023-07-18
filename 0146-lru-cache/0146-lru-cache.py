class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.ma=OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.ma:
            return -1
        self.ma.move_to_end(key)
        return self.ma[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.ma:
            del self.ma[key]
        elif len(self.ma)==self.cap:
            self.ma.popitem(last=False)
        self.ma[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)