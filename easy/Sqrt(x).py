class Solution:
    def mySqrt(self, x):

        if x != 0:
            for i in range(int(x / 1000000), x + 1):
                if i * i == x:
                    return i
                elif i * i <= x and (i + 1) * (i + 1) > x:
                    return i
        
        return 0