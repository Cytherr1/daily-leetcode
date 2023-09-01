class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        columnName =""
        digits = []

        for i in range(7, -1, -1):

            if columnNumber >= 26**i:
                    a = columnNumber // 26**i
                    digits.append(a % 26)

        while 0 in digits:
            index = digits.index(0)
            if index == 0:
                digits.pop(0)
            else:
                digits[index - 1] -= 1
                digits[index] = 26 

        for i in digits:
            columnName += chr(64 + i)

        return columnName