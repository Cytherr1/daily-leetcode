class Solution:
    def containsDuplicate(self, nums):

        check = set(nums)

        return len(nums) > len(check)