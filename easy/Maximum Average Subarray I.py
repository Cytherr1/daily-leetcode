class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        l = len(nums)
        wSum = sum(nums[:k])
        res = wSum / k

        for i in range(l - k):
            wSum = wSum - nums[i] + nums[i + k]
            res = max(res, wSum / k)

        return res