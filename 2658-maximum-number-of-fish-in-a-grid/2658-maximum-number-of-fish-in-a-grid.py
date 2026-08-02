class Solution(object):
    def findMaxFish(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        max_fish = 0

        def dfs(r, c):
            # Out of bounds or land cell (0 fish)
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            # Catch the fish at the current cell
            fish_count = grid[r][c]
            grid[r][c] = 0  # Mark as visited by setting to 0

            # Explore all 4 adjacent directions (Down, Up, Right, Left)
            fish_count += dfs(r + 1, c)
            fish_count += dfs(r - 1, c)
            fish_count += dfs(r, c + 1)
            fish_count += dfs(r, c - 1)

            return fish_count

        # Iterate through every cell in the grid
        for r in range(m):
            for c in range(n):
                # If we find a water cell with fish, start a DFS traversal
                if grid[r][c] > 0:
                    max_fish = max(max_fish, dfs(r, c))

        return max_fish