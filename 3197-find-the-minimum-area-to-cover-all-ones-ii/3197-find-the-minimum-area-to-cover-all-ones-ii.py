from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        
        # Helper to compute the minimum bounding box area of 1s within grid[r1..r2][c1..c2]
        def get_area(r1: int, r2: int, c1: int, c2: int) -> int:
            min_r, max_r = R, -1
            min_c, max_c = C, -1
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if grid[r][c] == 1:
                        min_r = min(min_r, r)
                        max_r = max(max_r, r)
                        min_c = min(min_c, c)
                        max_c = max(max_c, c)
            if max_r == -1:
                return 0
            return (max_r - min_r + 1) * (max_c - min_c + 1)
        
        ans = R * C
        
        # 1. Three horizontal strips
        for i1 in range(R - 2):
            for i2 in range(i1 + 1, R - 1):
                a1 = get_area(0, i1, 0, C - 1)
                a2 = get_area(i1 + 1, i2, 0, C - 1)
                a3 = get_area(i2 + 1, R - 1, 0, C - 1)
                ans = min(ans, a1 + a2 + a3)
                
        # 2. Three vertical strips
        for j1 in range(C - 2):
            for j2 in range(j1 + 1, C - 1):
                a1 = get_area(0, R - 1, 0, j1)
                a2 = get_area(0, R - 1, j1 + 1, j2)
                a3 = get_area(0, R - 1, j2 + 1, C - 1)
                ans = min(ans, a1 + a2 + a3)
                
        # 3. Horizontal split then vertical split bottom
        # 4. Horizontal split then vertical split top
        for i in range(R - 1):
            for j in range(C - 1):
                # Top full, Bottom split (left/right)
                a_top = get_area(0, i, 0, C - 1)
                a_bot_l = get_area(i + 1, R - 1, 0, j)
                a_bot_r = get_area(i + 1, R - 1, j + 1, C - 1)
                ans = min(ans, a_top + a_bot_l + a_bot_r)
                
                # Bottom full, Top split (left/right)
                a_bot = get_area(i + 1, R - 1, 0, C - 1)
                a_top_l = get_area(0, i, 0, j)
                a_top_r = get_area(0, i, j + 1, C - 1)
                ans = min(ans, a_bot + a_top_l + a_top_r)
                
        # 5. Vertical split then horizontal split right
        # 6. Vertical split then horizontal split left
        for j in range(C - 1):
            for i in range(R - 1):
                # Left full, Right split (top/bottom)
                a_left = get_area(0, R - 1, 0, j)
                a_right_t = get_area(0, i, j + 1, C - 1)
                a_right_b = get_area(i + 1, R - 1, j + 1, C - 1)
                ans = min(ans, a_left + a_right_t + a_right_b)
                
                # Right full, Left split (top/bottom)
                a_right = get_area(0, R - 1, j + 1, C - 1)
                a_left_t = get_area(0, i, 0, j)
                a_left_b = get_area(i + 1, R - 1, 0, j)
                ans = min(ans, a_right + a_left_t + a_left_b)
                
        return ans