class Solution:
    def longestConsecutive(self, nums):
        nums.sort()
        longest = 1
        maxLen = 0

        if nums:
            maxLen = 1
            for i in range(1, len(nums)):
                if nums[i] == nums[i - 1] + 1:
                    longest += 1
                    maxLen = max(maxLen, longest)
                elif nums[i] == nums[i-1]:
                    continue
                else:
                    longest = 1

        return maxLen