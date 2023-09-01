class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        words = s.split()
        print(words)

        return len(words[-1])
    
element = Solution()
element.lengthOfLastWord("Hello World")