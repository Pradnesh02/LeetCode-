class Solution(object):
    def numberOfSubmatrices(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        
        cntX = [[0] * cols for _ in range(rows)]
        cntY = [[0] * cols for _ in range(rows)]
        
        valid_submatrices = 0
        
        for r in range(rows):
            for c in range(cols):
                is_x = 1 if grid[r][c] == 'X' else 0
                is_y = 1 if grid[r][c] == 'Y' else 0
                
                # 2D prefix sum calculation
                x_top = cntX[r-1][c] if r > 0 else 0
                x_left = cntX[r][c-1] if c > 0 else 0
                x_diag = cntX[r-1][c-1] if (r > 0 and c > 0) else 0
                
                y_top = cntY[r-1][c] if r > 0 else 0
                y_left = cntY[r][c-1] if c > 0 else 0
                y_diag = cntY[r-1][c-1] if (r > 0 and c > 0) else 0
                
                cntX[r][c] = is_x + x_top + x_left - x_diag
                cntY[r][c] = is_y + y_top + y_left - y_diag
                
                # Check required conditions
                if cntX[r][c] > 0 and cntX[r][c] == cntY[r][c]:
                    valid_submatrices += 1
                    
        return valid_submatrices