class Solution:
    def findDifference(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        share = nums1 & nums2

        return [list(nums1 - share), list(nums2 - share)]
    

