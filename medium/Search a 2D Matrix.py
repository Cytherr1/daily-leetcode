class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        m = list()

        for i in matrix:
            if target < i[-1]:
                m = i
                break

        l = 0
        r = len(m) - 1

        while l <= r:
            i = l + (r - l) // 2

            if m[i] == target:
                return True
            elif m[i] < target:
                l = i + 1
            elif m[i] > target:
                r = i - 1
            
        return False
