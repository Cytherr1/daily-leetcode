import heapq as hq

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        hq.heappush(nums, target)
        nums.sort()
        print(nums)

        return nums.index(target)
