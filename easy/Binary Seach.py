class Solution:
    def search(self, nums, target) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            i = l + (r - l) // 2

            if nums[i] == target:
                return i
            elif nums[i] < target:
                l = i + 1
            elif nums[i] > target:
                r = i - 1
            
        return -1
