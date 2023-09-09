class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for i in range(1 ,numRows + 1):
            if i == 1:
                triangle.append([1])
            elif i == 2:
                triangle.append([1,1])
            else:
                row = []
                for e in range(1, 4):
                    if e == 3 or e == 1:
                        row.append(1)
                    else:
                        for index, element in enumerate(triangle[i - 2]):
                            if index == len(triangle[i - 2]) - 1:
                                break
                            else:
                                row.append(element + triangle[i - 2][index + 1])
                triangle.append(row)

        return triangle