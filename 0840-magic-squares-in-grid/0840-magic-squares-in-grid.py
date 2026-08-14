class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        count = 0

        def is_magic(r, c):
            # Center must be 5
            if grid[r + 1][c + 1] != 5:
                return False

            # Check if all numbers from 1 to 9 are present uniquely
            vals = [grid[r + i][c + j] for i in range(3) for j in range(3)]
            if sorted(vals) != list(range(1, 10)):
                return False

            # Check rows
            if (grid[r][c] + grid[r][c + 1] + grid[r][c + 2] != 15 or
                grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2] != 15 or
                grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2] != 15):
                return False

            # Check columns
            if (grid[r][c] + grid[r + 1][c] + grid[r + 2][c] != 15 or
                grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1] != 15 or
                grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2] != 15):
                return False

            # Check diagonals
            if (grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15 or
                grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15):
                return False

            return True

        # Check every 3x3 window
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic(r, c):
                    count += 1

        return count