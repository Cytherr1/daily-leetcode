class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        substring = s[0]
        s = s[1:]
        while s:
            l = len(substring)
            split = [s[i : i + l] for i in range(0, len(s), l)]
            sSet = set(split)

            if len(sSet) == 1 and substring in sSet:
                return True
                    
            substring += s[0]
            s = s[1:]
        return False

