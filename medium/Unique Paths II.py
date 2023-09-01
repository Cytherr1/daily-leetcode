class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        emptyMatrix = [[0] * n for _ in range(m)]

        emptyMatrix[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for row in range(m):
            for column in range(n):
                if obstacleGrid[row][column] == 1:
                    emptyMatrix[row][column] = 0
                else:
                    if row > 0:
                        emptyMatrix[row][column] += emptyMatrix[row - 1][column]
                    if column > 0:
                        emptyMatrix[row][column] += emptyMatrix[row][column - 1]
        
        return emptyMatrix[-1][-1]