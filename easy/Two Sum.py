class Solution:
    def twoSum(self, nums, target):
        hashMap = {i: e for i, e in enumerate(nums)}
        hm = sorted(hashMap.items(), key=lambda x: x[1])
        r, l = len(nums) - 1, 0

        while l < r:
            if hm[l][1] + hm[r][1] == target:
                return [hm[l][0], hm[r][0]]
            elif hm[l][1] + hm[r][1] < target:
                l += 1
            elif hm[l][1] + hm[r][1] > target:
                r -= 1