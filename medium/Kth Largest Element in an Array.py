from heapq import heappush, heappop

class Solution:
  def findKthLargest(self, nums: list[int], k: int) -> int:
    minHeap = []

    for num in nums:
      heappush(minHeap, num)
      if len(minHeap) > k:
        heappop(minHeap)

    return minHeap[0]

# FAIL
"""
a = sorted({i : nums.count(i) for i in nums}.items(), reverse=True)
        
    total = 0
        
    for i, e in enumerate(a):
        count = e[1]
        total += count
        if total >= k:
            return e[0]
"""    

# FAIL
"""
total = total
        numset = set(nums)
        number = max(numset)
        total += nums.count(max(numset))

        if total >= k:
            return number
        else:
            numset = numset.remove(max(numset))
            return self.findKthLargest(nums, k, total)
"""

# FAIL
"""
total = 0
        number = int()
        numset = set(nums)

        while total < k:
            number = max(numset)
            total += nums.count(max(numset))
            numset.remove(max(numset))

        return number
"""
