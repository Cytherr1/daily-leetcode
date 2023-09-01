class Solution(object):
    def removeDuplicates(self, nums):

        a = [i for i in set(nums)]
        a.sort()
        
        for i , e in enumerate(a):
            nums.remove(e)
            nums.insert(i,e)

        nums = nums[:len(a)]
        
        k = len(nums)
        return k
