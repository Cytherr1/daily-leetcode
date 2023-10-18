from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):

        hashed = Counter(nums)

        hashed = dict(sorted(hashed.items(), reverse=True, key=lambda x : x[1]))
        elements = list(hashed.keys())

        return elements[:k]