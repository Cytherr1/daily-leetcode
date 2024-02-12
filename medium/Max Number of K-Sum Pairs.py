class Solution:
    def maxOperations(self, nums, k: int) -> int:
        l, r, n = 0, len(nums) - 1, 0
        nums.sort()
        while l < r:
            if nums[l] + nums[r] == k:
                n += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                l += 1
        
        return n