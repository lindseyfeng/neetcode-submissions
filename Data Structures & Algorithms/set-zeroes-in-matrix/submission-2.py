class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        for j in range(col):
            if matrix[0][j] == 0:
                first_row_zero = True

        for i in range(row):
            if matrix[i][0] == 0:
                first_col_zero = True

        # mark
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # zero inner matrix
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # first row
        if first_row_zero:
            for j in range(col):
                matrix[0][j] = 0

        # first col
        if first_col_zero:
            for i in range(row):
                matrix[i][0] = 0