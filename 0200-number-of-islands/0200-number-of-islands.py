class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        islands_count = 0

        def dfs(r, c):
            # Check for out-of-bounds or water cells ('0')
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return

            # Mark the current land cell as visited by converting it to water ('0')
            grid[r][c] = "0"

            # Explore all 4 adjacent directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        for r in range(m):
            for c in range(n):
                # When an unvisited land cell ('1') is found, a new island is discovered
                if grid[r][c] == "1":
                    islands_count += 1
                    dfs(r, c)  # Sink the entire connected island

        return islands_count