class Solution:
    def pivotIndex(self, nums) -> int:
        ls, rs = 0, sum(nums[1:])
        
        if ls == rs:
            return 0
        else:
            for i in range(1, len(nums)):
                ls += nums[i - 1]
                rs -= nums[i]
                if ls == rs:
                    return i  
        
        return -1