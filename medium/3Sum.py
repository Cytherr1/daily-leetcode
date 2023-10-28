class Solution:
    def threeSum(self, nums):
        triplets, l = [], len(nums) - 1
        nums.sort()

        for i in range(l - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, l

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    triplets.append(triplet)
                    while j < k and nums[j] == triplet[1]:
                        j += 1
                    while j < k and nums[k] == triplet[2]:
                        k -= 1
        
        return triplets
            
    