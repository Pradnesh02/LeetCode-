class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        total_area = 0

        for r in range(n):
            for c in range(n):
                height = grid[r][c]
                if height > 0:
                    # Top and bottom faces
                    total_area += 2
                    
                    # 4 side faces minus occluded faces by adjacent towers
                    # Up
                    up = grid[r - 1][c] if r > 0 else 0
                    total_area += max(0, height - up)
                    
                    # Down
                    down = grid[r + 1][c] if r + 1 < n else 0
                    total_area += max(0, height - down)
                    
                    # Left
                    left = grid[r][c - 1] if c > 0 else 0
                    total_area += max(0, height - left)
                    
                    # Right
                    right = grid[r][c + 1] if c + 1 < n else 0
                    total_area += max(0, height - right)

        return total_area