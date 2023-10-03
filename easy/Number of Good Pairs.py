class Solution:
    def numIdenticalPairs(self, nums) -> int:
        
        pairs = 0

        for i, e in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if e == nums[j]:
                    pairs += 1

        return pairs