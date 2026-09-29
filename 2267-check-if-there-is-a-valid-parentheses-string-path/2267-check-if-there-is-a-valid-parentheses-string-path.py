from functools import lru_cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Any valid path has length m + n - 1; a valid parentheses string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
        
        # Must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
            
        @lru_cache(None)
        def dfs(r: int, c: int, bal: int) -> bool:
            # If remaining steps to destination are fewer than balance, it can't reach 0
            remaining_steps = (m - 1 - r) + (n - 1 - c)
            if bal > remaining_steps:
                return False
                
            # Base case: reached bottom-right cell
            if r == m - 1 and c == n - 1:
                return bal == 0
                
            # Explore down and right
            for dr, dc in ((1, 0), (0, 1)):
                nr, nc = r + dr, c + dc
                if nr < m and nc < n:
                    delta = 1 if grid[nr][nc] == '(' else -1
                    new_bal = bal + delta
                    if new_bal >= 0 and dfs(nr, nc, new_bal):
                        return True
                        
            return False

        return dfs(0, 0, 1)