class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum = ""

        iStr = str(int(a) + int(b))

        strList = [int(i) for i in iStr]

        strList.insert(0, 0)

        if 2 in strList:
            for i in range(len(strList) - 1, -1, -1):

                if strList[i] == 2:
                    strList[i - 1] += 1
                    strList[i] = 0

                elif strList[i] == 3:
                    strList[i - 1] += 1
                    strList[i] = 1

        if strList[0] == 0:
            strList.remove(0)
        
        for i in strList:
            sum += str(i)

        return sum