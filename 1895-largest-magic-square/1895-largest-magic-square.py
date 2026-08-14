class Solution(object):
    def largestMagicSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        # Prefix sums for rows
        row_pref = [[0] * (n + 1) for _ in range(m)]
        for r in range(m):
            for c in range(n):
                row_pref[r][c + 1] = row_pref[r][c] + grid[r][c]

        # Prefix sums for columns
        col_pref = [[0] * (n) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                col_pref[r + 1][c] = col_pref[r][c] + grid[r][c]

        def is_magic(r, c, k):
            # 1. Check Diagonals
            d1 = sum(grid[r + i][c + i] for i in range(k))
            d2 = sum(grid[r + i][c + k - 1 - i] for i in range(k))
            if d1 != d2:
                return False

            target = d1

            # 2. Check Row Sums
            for i in range(k):
                r_sum = row_pref[r + i][c + k] - row_pref[r + i][c]
                if r_sum != target:
                    return False

            # 3. Check Column Sums
            for j in range(k):
                c_sum = col_pref[r + k][c + j] - col_pref[r][c + j]
                if c_sum != target:
                    return False

            return True

        # Check from maximum possible size down to 2
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k

        return 1