class Solution(object):
    def lengthOfLongestSubstring(self, s):
        
        highest = 0
        index = 0
        for char in s:
            substring = list()
            for x in range(index, len(s)):
                substring.append(s[x])
                if substring.index(s[x]) != (len(substring) - 1):
                    substring.pop()
                    break

                if len(substring) > highest:
                    highest = len(substring)
            index += 1
        
        return highest