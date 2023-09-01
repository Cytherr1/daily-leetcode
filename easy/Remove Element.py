class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while nums:
            if val in nums:
                nums.remove(val)
            else:
                break

        k = len(nums)

        return k