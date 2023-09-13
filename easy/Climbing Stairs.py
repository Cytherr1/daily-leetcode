from math import comb as c

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        total = 0
        iteration = n // 2
        curr = 0

        while curr <= iteration:
            total += c(n - curr, curr)
            curr += 1

        return total