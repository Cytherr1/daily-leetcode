import heapq

class Solution:
    def kWeakestRows(self, mat, k):

        minHeap = []
        weakRows = []

        for i, row in enumerate(mat):
            pow = row.count(1)
            item = [pow ,i]
            heapq.heappush(minHeap, item)
        
        i = 0
        while i < k:
            weakRows.append(heapq.heappop(minHeap)[1])
            i += 1

        return weakRows