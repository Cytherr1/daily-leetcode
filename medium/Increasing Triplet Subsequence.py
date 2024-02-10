import heapq as hq

class Solution:
    def increasingTriplet(self, nums) -> bool:
        
        minHeap = []

        for i, e in enumerate(nums):
            hq.heappush(minHeap, (i, e))
        print(minHeap)
        i, j, k = hq.heappop(minHeap), hq.heappop(minHeap), hq.heappop(minHeap)
        print(i, j, k)

        while minHeap:
            if i[1] < j[1] < k[1]:
                return True
            else:
                if i[1] > j[1]:
                    i = min(i, j, key=lambda x: x[1])
                    j = min(j, k, key=lambda x: x[1])
                    k = hq.heappop(minHeap)
                else:
                    if j[1] > k[1]:
                        j = min(j, k, key=lambda x: x[1])
                        k = hq.heappop(minHeap)
        
        return False