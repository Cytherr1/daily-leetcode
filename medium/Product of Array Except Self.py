import numpy as np

class Solution1:
    def productExceptSelf(self, nums):
        
        l = len(nums)

        res = np.array([1] * l)

        for i in range(l):
            res[:i] = res[:i] * nums[i]
            res[i+1:] = res[i+1:] * nums[i]
            
        return res

class Solution2:
    def productExceptSelf(self, nums):

        length = len(nums)

        products = []
        prefixProduct, suffixProduct = [1] * length, [1] * length
        prefixProduct[0] = nums[0]
        suffixProduct[-1] = nums[-1]

        for i in range(1, length):
            prefixProduct[i] = prefixProduct[i - 1] * nums[i]

        for i in range(length - 2, -1, -1):
            suffixProduct[i] = suffixProduct[i + 1] * nums[i]

        for i in range(length):
            if i == 0:
                products.append(suffixProduct[1])
            elif i == length - 1:
                products.append(prefixProduct[length - 2])
            else:
                products.append(prefixProduct[i - 1] * suffixProduct[i + 1])

        return products