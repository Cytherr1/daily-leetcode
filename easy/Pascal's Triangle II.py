import math

class Solution:
    def getRow(self, rowIndex):
        
        x = rowIndex

        row = [math.comb(rowIndex, i) for i in range(x, -1, -1)]

        return row