class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])

        rowZero = False
        colZero = False

        for j in range(cols):
            if matrix[0][j] == 0:
                rowZero = True

        for i in range(rows):
            if matrix[i][0] == 0:
                colZero = True

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if rowZero:
            for j in range(cols):
                matrix[0][j] = 0

        if colZero:
            for i in range(rows):
                matrix[i][0] = 0