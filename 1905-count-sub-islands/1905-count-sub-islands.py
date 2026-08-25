class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        m, n = len(grid1), len(grid1[0])
        
        def dfs(r, c):
            # Mark cell as visited by setting it to 0
            grid2[r][c] = 0
            is_sub = True
            
            # If corresponding cell in grid1 is water (0), it cannot be a sub-island
            if grid1[r][c] == 0:
                is_sub = False
                
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid2[nr][nc] == 1:
                    # Explore the entire island in grid2, even if already determined invalid
                    if not dfs(nr, nc):
                        is_sub = False
                        
            return is_sub

        sub_island_count = 0
        
        for r in range(m):
            for c in range(n):
                if grid2[r][c] == 1:
                    if dfs(r, c):
                        sub_island_count += 1
                        
        return sub_island_count