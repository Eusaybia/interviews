class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        y = m
        x = n
        matrix = [[0 for i in range(x)] for j in range(y)]

        # initalise all values in the first row to 1
        for i in range(0, x):
            matrix[0][i] = 1

        # initialise all the values in the first column to 1
        for i in range(0, y):
            matrix[i][0] = 1

        # calculate the number of paths based on the x - 1 coordinate and the y - 1 coordinate
        for i in range(1, y):
            for j in range(1, x):
                matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]

        return matrix[y - 1][x - 1]
