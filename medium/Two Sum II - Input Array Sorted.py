class Solution:
    def twoSum(self, numbers, target):
    
        for i in range(len(numbers)):
            r = target - numbers[i]
            if r in numbers[i:]:
                return [i + 1, numbers.index(r) + 1]
            

"""
Also consider this for better runtime O(n):

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1
        
        while numbers[i] + numbers[j]!=target:
            s = numbers[i] + numbers[j]        
            if s > target:
                j-=1
            else:
               i+=1 
        
        return [i + 1 , j + 1]
"""

