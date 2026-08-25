class Solution(object):
    def countPathsWithXorValue(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        
        # 3D DP table: m x n x 16
        dp = [[[0] * 16 for _ in range(n)] for _ in range(m)]
        
        # Set start cell
        start_val = grid[0][0]
        dp[0][0][start_val] = 1
        
        for r in range(m):
            for c in range(n):
                for x in range(16):
                    ways = dp[r][c][x]
                    if ways == 0:
                        continue
                    
                    # Move Right
                    if c + 1 < n:
                        nxt_x = x ^ grid[r][c + 1]
                        dp[r][c + 1][nxt_x] = (dp[r][c + 1][nxt_x] + ways) % MOD
                        
                    # Move Down
                    if r + 1 < m:
                        nxt_x = x ^ grid[r + 1][c]
                        dp[r + 1][c][nxt_x] = (dp[r + 1][c][nxt_x] + ways) % MOD
        
        return dp[m - 1][n - 1][k] if k < 16 else 0