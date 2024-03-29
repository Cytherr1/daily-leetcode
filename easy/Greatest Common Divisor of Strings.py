class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1 = min(str1, str2, key=lambda x: len(x))

        if str1 == str2:
            return str1
        else:
            while s1:
                if len(str1) / len(s1) == str1.count(s1) and len(str2) / len(s1) == str2.count(s1):
                    return s1
                else:
                    s1 = s1[:-1]

            return ""