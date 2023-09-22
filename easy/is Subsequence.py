class Solution:
    def isSubsequence(self, s, t):

        if s in t:
            return True
        
        else:
            subHave = ""
            
            for i in t:
                if i in s:
                    subHave = subHave + i
                    if subHave not in s:
                        subHave = subHave[:-1]

            if s == subHave:
                return True
            
            return False
