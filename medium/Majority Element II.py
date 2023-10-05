class Solution:
    def majorityElement(self, nums):
        
        elements = []
        minR = int(len(nums) / 3)
        thisdict = dict.fromkeys(nums, 0)

        for i in thisdict:
            thisdict[i] = nums.count(i)
            if thisdict[i] > minR:
                elements.append(i)

        return elements