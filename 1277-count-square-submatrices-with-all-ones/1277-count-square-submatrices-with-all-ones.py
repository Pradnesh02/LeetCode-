class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        total_squares = 0

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1:
                    if r > 0 and c > 0:
                        matrix[r][c] += min(
                            matrix[r - 1][c],
                            matrix[r][c - 1],
                            matrix[r - 1][c - 1]
                        )
                    total_squares += matrix[r][c]

        return total_squares