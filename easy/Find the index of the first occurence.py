class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            n = len(needle)
            index = haystack.index(needle[0])
            while True:

                if haystack[index: index + n] == needle:
                    return index
                else:
                    index = haystack.find(needle[0], index + 1)
                    if index == -1:
                        break

        return -1
