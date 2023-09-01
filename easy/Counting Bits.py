class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        onesList = [0]
        for i in range(1, n + 1):
            if i % 2 == 1:
                onesList.append(onesList[i - 1] + 1)
            else:
                onesList.append(onesList[i // 2])

        return onesList