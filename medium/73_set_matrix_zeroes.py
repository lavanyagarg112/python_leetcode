class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        copy = []
        for i in range(rows):
            copy.append([])
            for j in range(cols):
                copy[i].append(matrix[i][j])

        for i in range(rows):
            for j in range(cols):

                if copy[i][j] == 0:
                    
                    for k in range(cols):
                        matrix[i][k] = 0
                    
                    for k in range(rows):
                        matrix[k][j] = 0

        return matrix
        