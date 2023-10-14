class Solution:
    def isAnagram(self, s, t):

        sSet = set(s)
        tSet = set(t)
        
        dictS = {i: s.count(i) for i in sSet}
        dictT = {i: t.count(i) for i in tSet}

        return dictS == dictT