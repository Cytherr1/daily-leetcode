class RecentCounter:

    def __init__(self):
        self.start = -3000
        self.end = 0
        self.counter = []

    def ping(self, t: int) -> int:
        self.start = t - 3000
        self.end += t 
        self.counter.append(t)

        while self.counter and self.counter[0] < self.start:
            self.counter.pop(0)
            
        return len(self.counter)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)