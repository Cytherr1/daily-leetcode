class Solution:
    def sortArrayByParity(self, nums):
        
        numbers = []
        for num in nums:
            if num % 2 == 0:
                numbers.insert(0, num)
            else:
                numbers.append(num)

        return numbers
