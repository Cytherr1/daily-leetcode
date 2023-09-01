import random

class Solution(object):
    def search(self, nums, target):
        pivot = random.randint(0, len(nums))
        index = 0

        def rotateNums(nums, pivot, index):
            if index == pivot:
                return nums
            else:
                newElement = nums[index]
                nums.append(newElement)
                nums.remove(newElement)
                return rotateNums(nums, pivot, index + 1)
            
        def contains(nums, target, index):
            if nums[index] == target:
                return True
            else:
                try:
                    return contains(nums, target, index + 1)
                except:
                    return False
            
        return contains(rotateNums(nums, pivot, index), target, index)




