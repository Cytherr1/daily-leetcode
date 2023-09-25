class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        totalS = 0
        totalT = 0

        for i in s:
            totalS += ord(i)
        
        for i in t:
            totalT += ord(i)

        return chr(totalT - totalS)