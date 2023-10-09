class Solution:
    def singleNumber(self, nums):
        numbers = {}
        for i in nums:
            if i in numbers.keys():
                numbers.update({i: 2})
            else:
                numbers.update({i: 1})

        return min(numbers.keys(), key = lambda x : numbers.get(x))