class Solution:
    def kidsWithCandies(self, candies, extraCandies: int):

        g = max(candies)
        l = []

        for i in candies:
            if i + extraCandies >= g:
                l.append(True)
            else:
                l.append(False)
        
        return l