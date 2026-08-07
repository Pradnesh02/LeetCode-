class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        rows, cols = len(grid), len(grid[0])
        
        # left[r][c]: consecutive 1s to the left ending at (r, c)
        # top[r][c]: consecutive 1s to the top ending at (r, c)
        left = [[0] * cols for _ in range(rows)]
        top = [[0] * cols for _ in range(rows)]
        
        # Step 1: Precompute left and top consecutive 1s
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    left[r][c] = (left[r][c - 1] + 1) if c > 0 else 1
                    top[r][c] = (top[r - 1][c] + 1) if r > 0 else 1
                    
        max_len = 0
        
        # Step 2: Iterate over each cell treating it as bottom-right corner
        for r in range(rows):
            for c in range(cols):
                # Maximum possible side length using current cell as bottom-right
                max_side = min(left[r][c], top[r][c])
                
                # Check side lengths in descending order
                for k in range(max_side, max_len, -1):
                    # Check top border and left border of the k x k square
                    if left[r - k + 1][c] >= k and top[r][c - k + 1] >= k:
                        max_len = k
                        break
                        
        return max_len * max_len