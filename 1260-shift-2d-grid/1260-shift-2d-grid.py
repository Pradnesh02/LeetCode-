class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        # Optimize shift count to avoid redundant full rotations
        k = k % total_elements
        
        # Initialize the result grid with zeroes
        res = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                # Convert 2D coordinate (r, c) to a 1D index
                one_d_idx = r * n + c
                
                # Calculate the new shifted 1D index
                new_idx = (one_d_idx + k) % total_elements
                
                # Convert the new 1D index back to 2D coordinates (new_r, new_c)
                new_r = new_idx // n
                new_c = new_idx % n
                
                res[new_r][new_c] = grid[r][c]
                
        return res