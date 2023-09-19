# Lesser Runtime higher Memory consumption
class Solution1:
    def findDuplicate(self, nums):

        cache = dict()

        for i in nums:
            if not cache.get(i):
                cache.update({i: 1})
            else:
                return i
        print(cache)

# Longer Runtime lesser Memory consumption
class Solution2:
    def findDuplicate(self, nums):

        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]   