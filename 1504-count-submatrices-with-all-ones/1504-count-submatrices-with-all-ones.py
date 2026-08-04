class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows, cols = len(mat), len(mat[0])
        
        # Precompute consecutive 1s to the left for each cell
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1 and c > 0:
                    mat[r][c] += mat[r][c - 1]
                    
        total_submatrices = 0
        
        # Count valid submatrices ending at each cell (r, c)
        for r in range(rows):
            for c in range(cols):
                min_width = mat[r][c]
                
                # Check all possible heights extending upward
                for k in range(r, -1, -1):
                    min_width = min(min_width, mat[k][c])
                    if min_width == 0:
                        break
                    total_submatrices += min_width
                    
        return total_submatrices