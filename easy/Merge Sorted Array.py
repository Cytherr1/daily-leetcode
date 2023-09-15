class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num2Index = 0
        if n != 0:
            for i in range(m, m + n):
                nums1[i] = nums2[num2Index]
                num2Index += 1

        nums1.sort()